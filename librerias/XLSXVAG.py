# librerias/XLSXVAG.py
# Lector de archivos .xlsx para VAGAX — sin librerías externas.
#
# XLSX es un archivo ZIP que contiene XML internamente (estándar OOXML).
# Lo leemos usando únicamente:
#   - open()      → built-in de Python (no requiere import)
#   - __import__ encapsulado para zipfile (parte del motor VAGAX,
#     igual que OSVAG usa __import__('os') internamente)
#
# Implementa un parser XML minimalista con búsqueda de patrones
# para extraer filas y valores numéricos de la hoja de cálculo.


class XLSXVAG:
    """
    Lector de archivos Excel (.xlsx) para VAGAX.
    Sin openpyxl, sin pandas, sin xlrd.
    Usa únicamente el motor ZIP+XML estándar encapsulado.
    """

    @staticmethod
    def get_headers(tabla):
        """
        Retorna la lista de nombres de columnas (primera fila de la tabla).
        Útil para mostrar columnas disponibles antes de elegir X e Y.
        """
        if not tabla:
            return []
        return [str(h) for h in tabla[0] if h is not None]

    # =========================================================
    # PARSER XML MINIMALISTA (sin librería xml)
    # =========================================================

    @staticmethod
    def _buscar_entre(texto, inicio_tag, fin_tag, desde=0):
        """
        Encuentra el contenido entre dos tags en un string.
        Retorna (contenido, posicion_fin) o (None, -1) si no encuentra.
        """
        pos_ini = texto.find(inicio_tag, desde)
        if pos_ini < 0:
            return None, -1
        pos_ini += len(inicio_tag)
        pos_fin = texto.find(fin_tag, pos_ini)
        if pos_fin < 0:
            return None, -1
        return texto[pos_ini:pos_fin], pos_fin + len(fin_tag)

    @staticmethod
    def _extraer_todos(texto, inicio_tag, fin_tag):
        """
        Extrae todos los contenidos entre pares de tags.
        Retorna lista de strings.
        """
        resultados = []
        pos = 0
        while True:
            contenido, nueva_pos = XLSXVAG._buscar_entre(texto, inicio_tag, fin_tag, pos)
            if contenido is None:
                break
            resultados.append(contenido)
            pos = nueva_pos
        return resultados

    @staticmethod
    def _leer_atributo(tag_str, nombre_attr):
        """
        Extrae el valor de un atributo XML de un string de apertura de tag.
        Ejemplo: _leer_atributo('<c r="A1" t="s">', 'r') → 'A1'
        """
        clave = nombre_attr + '="'
        pos = tag_str.find(clave)
        if pos < 0:
            return None
        pos += len(clave)
        fin = tag_str.find('"', pos)
        if fin < 0:
            return None
        return tag_str[pos:fin]

    # =========================================================
    # LECTOR DE SHAREDSTRINGS
    # =========================================================

    @staticmethod
    def _leer_shared_strings(ss_xml):
        """
        Parsea xl/sharedStrings.xml y retorna lista de strings.
        Cada <si><t>valor</t></si> es una entrada.
        """
        strings = []
        pos = 0
        while True:
            # Buscar cada <si>
            ini_si = ss_xml.find('<si>', pos)
            if ini_si < 0:
                break
            fin_si = ss_xml.find('</si>', ini_si)
            if fin_si < 0:
                break
            bloque = ss_xml[ini_si:fin_si]

            # Extraer texto del <t>
            ini_t = bloque.find('<t')
            if ini_t >= 0:
                ini_t2 = bloque.find('>', ini_t) + 1
                fin_t = bloque.find('</t>', ini_t2)
                if fin_t >= 0:
                    strings.append(bloque[ini_t2:fin_t])
                else:
                    strings.append('')
            else:
                strings.append('')

            pos = fin_si + 5
        return strings

    # =========================================================
    # LECTOR DE FILAS
    # =========================================================

    @staticmethod
    def _col_a_indice(col_str):
        """
        Convierte columna de letra(s) a índice base-0.
        'A' → 0, 'B' → 1, ..., 'Z' → 25, 'AA' → 26, etc.
        """
        col_str = col_str.upper()
        resultado = 0
        for ch in col_str:
            resultado = resultado * 26 + (ord(ch) - ord('A') + 1)
        return resultado - 1

    @staticmethod
    def _leer_celda(celda_xml, shared_strings):
        """
        Extrae el valor de una celda XML.
        Retorna (columna_idx, valor) donde valor es str o float.
        celda_xml: el contenido entre <c ...> y </c>
        """
        # Extraer atributo r (referencia: 'A1', 'B2', etc.)
        ini_r = celda_xml.find(' r="')
        if ini_r < 0:
            ini_r = celda_xml.find('"')  # fallback
            return None, None

        ini_r += 4
        fin_r = celda_xml.find('"', ini_r)
        ref = celda_xml[ini_r:fin_r]

        # Separar letra(s) de número(s) de la referencia (ej: 'AB12' → 'AB', '12')
        col_str = ''
        for ch in ref:
            if ch.isalpha():
                col_str += ch
            else:
                break
        col_idx = XLSXVAG._col_a_indice(col_str)

        # ¿Es tipo string (t="s")?
        es_string = 't="s"' in celda_xml

        # Extraer <v>valor</v>
        ini_v = celda_xml.find('<v>')
        if ini_v < 0:
            return col_idx, None
        ini_v += 3
        fin_v = celda_xml.find('</v>', ini_v)
        if fin_v < 0:
            return col_idx, None
        valor_raw = celda_xml[ini_v:fin_v].strip()

        if es_string:
            try:
                idx = int(valor_raw)
                return col_idx, shared_strings[idx] if idx < len(shared_strings) else ''
            except Exception:
                return col_idx, valor_raw
        else:
            try:
                if '.' in valor_raw:
                    return col_idx, float(valor_raw)
                else:
                    return col_idx, int(valor_raw)
            except Exception:
                return col_idx, valor_raw

    @staticmethod
    def _leer_fila(fila_xml, shared_strings):
        """
        Parsea una <row>...</row> y retorna dict {col_idx: valor}.
        """
        celdas = {}
        pos = 0
        while True:
            # Encontrar apertura de celda <c ...>
            ini_c = fila_xml.find('<c ', pos)
            if ini_c < 0:
                break
            # Encontrar cierre </c>
            fin_c = fila_xml.find('</c>', ini_c)
            if fin_c < 0:
                # Intentar celda de autocierre <c ... />
                fin_c2 = fila_xml.find('/>', ini_c)
                if fin_c2 < 0:
                    break
                pos = fin_c2 + 2
                continue

            celda_xml = fila_xml[ini_c: fin_c]
            col_idx, valor = XLSXVAG._leer_celda(celda_xml, shared_strings)
            if col_idx is not None and valor is not None:
                celdas[col_idx] = valor

            pos = fin_c + 4
        return celdas

    # =========================================================
    # API PÚBLICA
    # =========================================================

    @staticmethod
    def leer_xlsx(ruta_xlsx, hoja=0):
        """
        Lee un archivo .xlsx y retorna una lista de listas (tabla).
        La primera fila contiene los nombres de columnas (strings).
        Las siguientes filas contienen los valores (str o float).

        ruta_xlsx : ruta al archivo .xlsx
        hoja      : índice de hoja (0 = primera hoja)
        """
        # Abrir como ZIP (built-in encapsulado)
        _zip = __import__('zipfile')

        with _zip.ZipFile(ruta_xlsx, 'r') as z:
            # Leer shared strings
            if 'xl/sharedStrings.xml' in z.namelist():
                ss_bytes = z.read('xl/sharedStrings.xml')
                ss_xml = ss_bytes.decode('utf-8', errors='replace')
                shared_strings = XLSXVAG._leer_shared_strings(ss_xml)
            else:
                shared_strings = []

            # Determinar nombre de la hoja
            hoja_nombre = 'xl/worksheets/sheet' + str(hoja + 1) + '.xml'
            if hoja_nombre not in z.namelist():
                raise Exception('[XLSXVAG] Hoja no encontrada: ' + hoja_nombre)

            sheet_bytes = z.read(hoja_nombre)
            sheet_xml = sheet_bytes.decode('utf-8', errors='replace')

        # Extraer todas las filas
        tabla = []
        pos = 0
        n_cols_max = 0

        while True:
            ini_row = sheet_xml.find('<row ', pos)
            if ini_row < 0:
                break
            fin_row = sheet_xml.find('</row>', ini_row)
            if fin_row < 0:
                break

            fila_xml = sheet_xml[ini_row: fin_row]
            celdas = XLSXVAG._leer_fila(fila_xml, shared_strings)

            if celdas:
                max_col = max(celdas.keys()) + 1
                if max_col > n_cols_max:
                    n_cols_max = max_col

            tabla.append(celdas)
            pos = fin_row + 6

        # Convertir dicts a listas alineadas (None para celdas vacías)
        resultado = []
        for celdas in tabla:
            fila = []
            for c in range(n_cols_max):
                fila.append(celdas.get(c, None))
            resultado.append(fila)

        return resultado

    @staticmethod
    def leer_xlsx_auto(ruta_xlsx, hoja=0):
        """
        Igual que leer_xlsx pero resuelve la ruta automáticamente.
        Prueba en este orden:
          1. Ruta tal cual (puede ser absoluta o relativa al cwd)
          2. Con prefijo 'ejemplos/'
          3. Con prefijo 'ejemplos/machinelearning/'
        Si ninguna funciona, lanza el error con todas las rutas intentadas.
        """
        ruta = str(ruta_xlsx).strip()

        # Limpiar barra inicial accidental si el usuario escribió /data.xlsx
        if ruta.startswith('/') and not __import__('os').path.isabs(ruta):
            ruta = ruta[1:]

        candidatos = [
            ruta,
            'ejemplos/' + ruta,
            'ejemplos/machinelearning/' + ruta,
        ]

        # Quitar duplicados manteniendo orden
        vistos = set()
        sin_dup = []
        for c in candidatos:
            if c not in vistos:
                vistos.add(c)
                sin_dup.append(c)

        ultimo_error = None
        for candidato in sin_dup:
            try:
                tabla = XLSXVAG.leer_xlsx(candidato, hoja)
                print('[XLSXVAG] Archivo encontrado: ' + candidato)
                return tabla
            except FileNotFoundError:
                ultimo_error = candidato
                continue
            except Exception as e:
                raise  # Error real (no es "archivo no encontrado")

        raise Exception(
            '[XLSXVAG] Archivo no encontrado. Rutas intentadas:\n' +
            '\n'.join('  - ' + c for c in sin_dup) +
            '\nIngrese la ruta completa, por ejemplo: ejemplos/data.xlsx'
        )

    @staticmethod
    def obtener_columna(tabla, nombre_col):
        """
        Extrae una columna por nombre del header (primera fila de tabla).
        Retorna lista de valores numéricos (omite None y strings).
        """
        if not tabla:
            raise Exception('[XLSXVAG] Tabla vacía')

        header = tabla[0]
        col_idx = -1
        for i, h in enumerate(header):
            if str(h).strip().lower() == str(nombre_col).strip().lower():
                col_idx = i
                break

        if col_idx < 0:
            raise Exception('[XLSXVAG] Columna no encontrada: ' + str(nombre_col) +
                            ' | Disponibles: ' + str([str(h) for h in header]))

        valores = []
        for fila in tabla[1:]:
            if col_idx < len(fila) and fila[col_idx] is not None:
                v = fila[col_idx]
                if isinstance(v, (int, float)):
                    valores.append(float(v))
                # Ignorar strings y None
        return valores

    @staticmethod
    def obtener_columnas_numericas(tabla, nombres_cols):
        """
        Extrae múltiples columnas numéricas por nombre.
        Retorna lista de listas alineadas (una por columna).
        Solo incluye filas donde TODAS las columnas son numéricas.
        """
        if not tabla:
            raise Exception('[XLSXVAG] Tabla vacía')

        header = tabla[0]
        indices = []
        for nombre in nombres_cols:
            col_idx = -1
            for i, h in enumerate(header):
                if str(h).strip().lower() == str(nombre).strip().lower():
                    col_idx = i
                    break
            if col_idx < 0:
                raise Exception('[XLSXVAG] Columna no encontrada: ' + str(nombre))
            indices.append(col_idx)

        columnas = [[] for _ in nombres_cols]

        for fila in tabla[1:]:
            # Verificar que todos los valores son numéricos en esta fila
            validos = True
            vals = []
            for ci in indices:
                if ci < len(fila) and isinstance(fila[ci], (int, float)):
                    vals.append(float(fila[ci]))
                else:
                    validos = False
                    break
            if validos:
                for j, v in enumerate(vals):
                    columnas[j].append(v)

        return columnas

    @staticmethod
    def resumen(tabla):
        """
        Imprime un resumen del contenido de la tabla.
        """
        if not tabla:
            print('[XLSXVAG] Tabla vacía')
            return
        header = tabla[0]
        print('[XLSXVAG] Columnas (' + str(len(header)) + '): ' +
              ', '.join([str(h) for h in header]))
        print('[XLSXVAG] Filas de datos: ' + str(len(tabla) - 1))
        # Muestra las primeras 3 filas
        for i, fila in enumerate(tabla[1:4]):
            print('  Fila ' + str(i + 1) + ': ' + str(fila))
