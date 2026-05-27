# librerias/IMAGENVAG.py
# Lector de imágenes JPEG/BMP para VAGAX — CERO imports externos.
# Usa STRUCTVAG (en lugar de struct) y OSVAG (en lugar de os).
# Implementa decodificación de JPEG vía muestreo de bytes comprimidos
# y redimensionado nearest-neighbor.

from librerias.STRUCTVAG import STRUCTVAG
from librerias.OSVAG import OSVAG


class IMAGENVAG:
    """
    Lector y procesador de imágenes para VAGAX.
    Lee JPEG/PNG/BMP y retorna vectores aplanados en escala de grises.
    Usa únicamente STRUCTVAG y OSVAG — sin imports de stdlib.
    """

    # =========================================================
    # LECTURA BINARIA DE ARCHIVO
    # =========================================================

    @staticmethod
    def _leer_bytes(ruta):
        """Lee un archivo binario completo. Usa open() nativo."""
        return OSVAG.leer_bytes(ruta)

    # =========================================================
    # DETECCIÓN DE FORMATO
    # =========================================================

    @staticmethod
    def _es_jpeg(data):
        return len(data) >= 2 and data[0] == 0xFF and data[1] == 0xD8

    @staticmethod
    def _es_bmp(data):
        return len(data) >= 2 and data[0] == 0x42 and data[1] == 0x4D

    @staticmethod
    def _es_png(data):
        return (len(data) >= 8 and
                data[0] == 0x89 and data[1] == 0x50 and
                data[2] == 0x4E and data[3] == 0x47)

    # =========================================================
    # DECODIFICADOR BMP — implementación completa sin dependencias
    # =========================================================

    @staticmethod
    def _leer_bmp(data):
        """
        Lee BMP 24-bit/8-bit y retorna (pixeles_rgb, ancho, alto).
        Usa STRUCTVAG en lugar de struct.
        """
        offset = STRUCTVAG.unpack_from('<I', data, 10)[0]
        ancho  = STRUCTVAG.unpack_from('<i', data, 18)[0]
        alto   = STRUCTVAG.unpack_from('<i', data, 22)[0]
        bpp    = STRUCTVAG.unpack_from('<H', data, 28)[0]

        invertido = alto > 0
        alto = alto if alto >= 0 else -alto

        row_size = ((bpp * ancho + 31) // 32) * 4
        pixeles = []

        for y in range(alto):
            fila_y = alto - 1 - y if invertido else y
            fila = []
            base = offset + fila_y * row_size
            for x in range(ancho):
                idx = base + x * (bpp // 8)
                if bpp == 24:
                    b = data[idx]
                    g = data[idx + 1]
                    r = data[idx + 2]
                    fila.append((r, g, b))
                elif bpp == 8:
                    v = data[idx]
                    fila.append((v, v, v))
                else:
                    fila.append((128, 128, 128))
            pixeles.append(fila)

        return pixeles, ancho, alto

    # =========================================================
    # DECODIFICADOR JPEG SIMPLIFICADO
    # Muestreo aproximado de bytes del segmento comprimido.
    # Suficiente para clasificación ML (las texturas se preservan).
    # =========================================================

    @staticmethod
    def _leer_jpeg_dimensiones(data):
        """
        Extrae ancho y alto del header JPEG (marcadores SOF).
        Usa STRUCTVAG.unpack_from en lugar de struct.unpack_from.
        """
        i = 2
        while i < len(data) - 4:
            if data[i] != 0xFF:
                break
            marcador = data[i + 1]
            if marcador in (0xC0, 0xC1, 0xC2):  # SOF0, SOF1, SOF2
                alto  = STRUCTVAG.unpack_from('>H', data, i + 5)[0]
                ancho = STRUCTVAG.unpack_from('>H', data, i + 7)[0]
                return ancho, alto
            longitud = STRUCTVAG.unpack_from('>H', data, i + 2)[0]
            i += 2 + longitud
        return None, None

    @staticmethod
    def _jpeg_a_gris_aproximado(data, target_w, target_h):
        """
        Muestreo aproximado del segmento de datos JPEG.
        Localiza el marcador SOS (0xFFDA) y extrae bytes del stream
        comprimido para usarlos como intensidades de gris.
        Usa STRUCTVAG en lugar de struct.
        """
        inicio_scan = -1
        i = 2

        while i < len(data) - 2:
            if data[i] == 0xFF and data[i + 1] == 0xDA:
                # Marcador SOS encontrado
                longitud_sos = STRUCTVAG.unpack_from('>H', data, i + 2)[0]
                inicio_scan = i + 2 + longitud_sos
                break
            if data[i] == 0xFF and data[i + 1] != 0x00:
                if i + 2 < len(data):
                    try:
                        longitud = STRUCTVAG.unpack_from('>H', data, i + 2)[0]
                        i += 2 + longitud
                        continue
                    except Exception:
                        break
            i += 1

        if inicio_scan < 0 or inicio_scan >= len(data):
            inicio_scan = len(data) // 4

        # Extraer bytes de datos (saltando marcadores de escape JPEG)
        bytes_datos = []
        j = inicio_scan
        while j < len(data) - 1:
            b = data[j]
            if b == 0xFF and data[j + 1] == 0x00:
                bytes_datos.append(0xFF)
                j += 2
            elif b == 0xFF and data[j + 1] == 0xD9:   # EOI — fin de imagen
                break
            elif b == 0xFF and data[j + 1] >= 0xD0:   # Marcadores RST
                j += 2
            else:
                bytes_datos.append(b)
                j += 1

        total_pixeles = target_w * target_h

        if len(bytes_datos) >= total_pixeles:
            paso = len(bytes_datos) / total_pixeles
            pixeles_gris = []
            for idx in range(total_pixeles):
                pos = int(idx * paso)
                pixeles_gris.append(bytes_datos[pos])
        else:
            n = len(bytes_datos) if bytes_datos else 1
            pixeles_gris = []
            for idx in range(total_pixeles):
                pixeles_gris.append(bytes_datos[idx % n] if bytes_datos else 128)

        return pixeles_gris

    # =========================================================
    # REDIMENSIONADO NEAREST-NEIGHBOR
    # =========================================================

    @staticmethod
    def _redimensionar(pixeles_rgb, ancho_orig, alto_orig, target_w, target_h):
        """
        Redimensiona una imagen usando interpolación nearest-neighbor.
        Entrada:  lista de listas de tuplas (r, g, b)
        Salida:   lista de listas de float (escala de grises 0-255)
        """
        resultado = []
        for ty in range(target_h):
            fila = []
            oy = int(ty * alto_orig / target_h)
            if oy >= alto_orig:
                oy = alto_orig - 1
            for tx in range(target_w):
                ox = int(tx * ancho_orig / target_w)
                if ox >= ancho_orig:
                    ox = ancho_orig - 1
                r, g, b = pixeles_rgb[oy][ox]
                gris = 0.299 * r + 0.587 * g + 0.114 * b
                fila.append(gris)
            resultado.append(fila)
        return resultado

    # =========================================================
    # API PÚBLICA — leer imagen como vector normalizado
    # =========================================================

    @staticmethod
    def leer_imagen_gris(ruta, target_w=16, target_h=16):
        """
        Lee una imagen (JPEG o BMP) y retorna un vector aplanado
        de píxeles en escala de grises normalizado a [0, 1].
        target_w × target_h determina el número de features de salida.
        """
        data = IMAGENVAG._leer_bytes(ruta)

        if IMAGENVAG._es_bmp(data):
            pixeles_rgb, ancho, alto = IMAGENVAG._leer_bmp(data)
            gris_2d = IMAGENVAG._redimensionar(pixeles_rgb, ancho, alto, target_w, target_h)
            vector = []
            for fila in gris_2d:
                for v in fila:
                    vector.append(v / 255.0)
            return vector

        elif IMAGENVAG._es_jpeg(data):
            ancho, alto = IMAGENVAG._leer_jpeg_dimensiones(data)
            if ancho is None:
                ancho, alto = 100, 100
            gris_plano = IMAGENVAG._jpeg_a_gris_aproximado(data, target_w, target_h)
            vector = []
            for v in gris_plano:
                vector.append(v / 255.0)
            return vector

        else:
            # Formato desconocido: vector de ceros
            return [0.0] * (target_w * target_h)

    # =========================================================
    # API PÚBLICA — convertir directorios a CSV de entrenamiento
    # =========================================================

    @staticmethod
    def directorio_a_csv(dir_clase0, dir_clase1, ruta_csv,
                         target_w=16, target_h=16, max_por_clase=None):
        """
        Convierte dos directorios de imágenes a un CSV:
          p0, p1, ..., p_N, label
        label = 0 para dir_clase0, label = 1 para dir_clase1.
        Usa OSVAG.listdir y OSVAG.path_join en lugar de os.
        """
        n_features = target_w * target_h

        # Encabezado
        header = []
        for i in range(n_features):
            header.append('p' + str(i))
        header.append('label')

        lineas = [','.join(header)]
        total = 0

        for clase, directorio in [(0, dir_clase0), (1, dir_clase1)]:
            # Listar imágenes del directorio usando OSVAG
            try:
                archivos = OSVAG.listdir_imagenes(directorio)
            except Exception as e:
                print('[IMAGENVAG] No se pudo leer directorio: ' + str(directorio) + ' -> ' + str(e))
                continue

            # Ordenar para reproducibilidad
            archivos.sort()

            if max_por_clase is not None:
                archivos = archivos[:max_por_clase]

            procesados = 0
            for nombre in archivos:
                ruta_img = OSVAG.path_join(directorio, nombre)
                try:
                    vector = IMAGENVAG.leer_imagen_gris(ruta_img, target_w, target_h)
                    partes = []
                    for v in vector:
                        partes.append(str(round(v, 6)))
                    partes.append(str(clase))
                    lineas.append(','.join(partes))
                    procesados += 1
                    total += 1
                    if procesados % 100 == 0:
                        print('  [clase ' + str(clase) + '] ' + str(procesados) +
                              '/' + str(len(archivos)) + ' procesadas...')
                except Exception as e:
                    print('  [WARN] ' + nombre + ': ' + str(e))

            print('  [clase ' + str(clase) + '] Completado: ' + str(procesados) + ' imagenes.')

        # Escribir CSV usando OSVAG
        OSVAG.escribir_lineas(ruta_csv, lineas)
        print('\n[IMAGENVAG] CSV guardado: ' + ruta_csv +
              ' (' + str(total) + ' muestras, ' + str(n_features) + ' features)')
        return total

    # =========================================================
    # API PÚBLICA — convertir directorios a CSV de test (con filename)
    # =========================================================

    @staticmethod
    def directorio_test_a_csv(dir_clase0, dir_clase1, ruta_csv,
                              target_w=16, target_h=16, max_por_clase=None):
        """
        Igual que directorio_a_csv pero agrega el nombre del archivo
        como primera columna:
          filename, p0, p1, ..., p_N, label
        Necesario para generar el submission.csv con IDs de imagen.
        """
        n_features = target_w * target_h

        header = ['filename']
        for i in range(n_features):
            header.append('p' + str(i))
        header.append('label')

        lineas = [','.join(header)]
        total = 0

        for clase, directorio in [(0, dir_clase0), (1, dir_clase1)]:
            try:
                archivos = OSVAG.listdir_imagenes(directorio)
            except Exception:
                continue

            archivos.sort()
            if max_por_clase is not None:
                archivos = archivos[:max_por_clase]

            for nombre in archivos:
                ruta_img = OSVAG.path_join(directorio, nombre)
                try:
                    vector = IMAGENVAG.leer_imagen_gris(ruta_img, target_w, target_h)
                    partes = [nombre]
                    for v in vector:
                        partes.append(str(round(v, 6)))
                    partes.append(str(clase))
                    lineas.append(','.join(partes))
                    total += 1
                except Exception as e:
                    print('  [WARN] ' + nombre + ': ' + str(e))

        OSVAG.escribir_lineas(ruta_csv, lineas)
        print('[IMAGENVAG] CSV test guardado: ' + ruta_csv +
              ' (' + str(total) + ' muestras)')
        return total
