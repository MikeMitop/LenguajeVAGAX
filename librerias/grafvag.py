# librerias/grafvag.py
# Motor gráfico VAGAX — Genera imágenes PPM sin dependencias externas
from librerias.MATHVAG import MATHVAG

class GRAFVAG:
    # --- MEMORIA DEL MOTOR (Variables de Estado) ---
    titulo = "GRAFICO VAGAX"
    label_x = "EJE X"
    label_y = "EJE Y"
    
    # Colores por defecto (RGB)
    color_barras = (50, 100, 255)  # Azul VAGAX
    color_linea = (255, 0, 0)      # Rojo fuerte
    color_fondo = (255, 255, 255)  # Blanco
    color_texto = (0, 0, 0)        # Negro

    # Paleta de colores automática para múltiples series
    PALETA = [
        (50, 100, 255), (255, 80, 80), (80, 200, 80), (255, 200, 50),
        (180, 80, 220), (255, 140, 50), (80, 220, 220), (200, 200, 200),
        (150, 50, 50), (50, 150, 50), (50, 50, 150), (200, 150, 50),
    ]

    # Diccionario de fuentes Bitmap 3x5 (Números, Letras y Espacio)
    FONTS = {
        '0': [[1,1,1],[1,0,1],[1,0,1],[1,0,1],[1,1,1]], '1': [[0,1,0],[1,1,0],[0,1,0],[0,1,0],[1,1,1]],
        '2': [[1,1,1],[0,0,1],[1,1,1],[1,0,0],[1,1,1]], '3': [[1,1,1],[0,0,1],[1,1,1],[0,0,1],[1,1,1]],
        '4': [[1,0,1],[1,0,1],[1,1,1],[0,0,1],[0,0,1]], '5': [[1,1,1],[1,0,0],[1,1,1],[0,0,1],[1,1,1]],
        '6': [[1,1,1],[1,0,0],[1,1,1],[1,0,1],[1,1,1]], '7': [[1,1,1],[0,0,1],[0,1,0],[1,0,0],[1,0,0]],
        '8': [[1,1,1],[1,0,1],[1,1,1],[1,0,1],[1,1,1]], '9': [[1,1,1],[1,0,1],[1,1,1],[0,0,1],[0,0,1]],
        'A': [[0,1,0],[1,0,1],[1,1,1],[1,0,1],[1,0,1]], 'B': [[1,1,0],[1,0,1],[1,1,0],[1,0,1],[1,1,1]],
        'C': [[1,1,1],[1,0,0],[1,0,0],[1,0,0],[1,1,1]], 'D': [[1,1,0],[1,0,1],[1,0,1],[1,0,1],[1,1,0]],
        'E': [[1,1,1],[1,0,0],[1,1,1],[1,0,0],[1,1,1]], 'F': [[1,1,1],[1,0,0],[1,1,0],[1,0,0],[1,0,0]],
        'G': [[1,1,1],[1,0,0],[1,0,1],[1,0,1],[1,1,1]], 'H': [[1,0,1],[1,0,1],[1,1,1],[1,0,1],[1,0,1]],
        'I': [[1,1,1],[0,1,0],[0,1,0],[0,1,0],[1,1,1]], 'J': [[0,0,1],[0,0,1],[0,0,1],[1,0,1],[1,1,1]],
        'K': [[1,0,1],[1,0,1],[1,1,0],[1,0,1],[1,0,1]], 'L': [[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,1,1]],
        'M': [[1,0,1],[1,1,1],[1,1,1],[1,0,1],[1,0,1]], 'N': [[1,1,1],[1,0,1],[1,0,1],[1,0,1],[1,0,1]],
        'O': [[1,1,1],[1,0,1],[1,0,1],[1,0,1],[1,1,1]], 'P': [[1,1,1],[1,0,1],[1,1,1],[1,0,0],[1,0,0]],
        'Q': [[1,1,1],[1,0,1],[1,1,1],[0,1,1],[0,0,1]], 'R': [[1,1,1],[1,0,1],[1,1,0],[1,0,1],[1,0,1]],
        'S': [[1,1,1],[1,0,0],[1,1,1],[0,0,1],[1,1,1]], 'T': [[1,1,1],[0,1,0],[0,1,0],[0,1,0],[0,1,0]],
        'U': [[1,0,1],[1,0,1],[1,0,1],[1,0,1],[1,1,1]], 'V': [[1,0,1],[1,0,1],[1,0,1],[0,1,0],[0,1,0]],
        'W': [[1,0,1],[1,0,1],[1,1,1],[1,1,1],[1,0,1]], 'X': [[1,0,1],[1,0,1],[0,1,0],[1,0,1],[1,0,1]],
        'Y': [[1,0,1],[1,0,1],[0,1,0],[0,1,0],[0,1,0]], 'Z': [[1,1,1],[0,0,1],[0,1,0],[1,0,0],[1,1,1]],
        ' ': [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],
        '.': [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,1,0]],
        '-': [[0,0,0],[0,0,0],[1,1,1],[0,0,0],[0,0,0]],
        ':': [[0,0,0],[0,1,0],[0,0,0],[0,1,0],[0,0,0]],
        '%': [[1,0,1],[0,0,1],[0,1,0],[1,0,0],[1,0,1]],
    }

    # --- SETTERS (CONFIGURACIÓN DE TEXTO) ---
    @staticmethod
    def set_title(texto):
        GRAFVAG.titulo = str(texto).upper()

    @staticmethod
    def set_xlabel(texto):
        GRAFVAG.label_x = str(texto).upper()

    @staticmethod
    def set_ylabel(texto):
        GRAFVAG.label_y = str(texto).upper()

    # --- SETTERS (CONFIGURACIÓN DE COLORES) ---
    @staticmethod
    def set_bar_color(r, g, b):
        GRAFVAG.color_barras = (r, g, b)

    @staticmethod
    def set_line_color(r, g, b):
        GRAFVAG.color_linea = (r, g, b)

    @staticmethod
    def set_bg_color(r, g, b):
        GRAFVAG.color_fondo = (r, g, b)

    @staticmethod
    def set_text_color(r, g, b):
        GRAFVAG.color_texto = (r, g, b)

    # --- DIBUJO DE TEXTO ---
    @staticmethod
    def dibujar_texto(imagen, x_pos, y_pos, texto, color=None):
        if color is None: color = GRAFVAG.color_texto
        for char in str(texto).upper():
            if char in GRAFVAG.FONTS:
                matriz = GRAFVAG.FONTS[char]
                for f in range(5):
                    for c in range(3):
                        if matriz[f][c] == 1:
                            for df in range(2):
                                for dc in range(2):
                                    py, px = y_pos + (f*2) + df, x_pos + (c*2) + dc
                                    if 0 <= py < len(imagen) and 0 <= px < len(imagen[0]):
                                        imagen[py][px] = color
            x_pos += 10

    # --- DIBUJO DE LÍNEA (Bresenham) ---
    @staticmethod
    def _dibujar_linea(img, x0, y0, x1, y1, color, alto=None, ancho=None):
        if alto is None: alto = len(img)
        if ancho is None: ancho = len(img[0])
        dx = MATHVAG.abs_val(x1 - x0)
        dy = -MATHVAG.abs_val(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx + dy
        while True:
            if 0 <= y0 < alto and 0 <= x0 < ancho:
                img[y0][x0] = color
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x0 += sx
            if e2 <= dx:
                err += dx
                y0 += sy

    # --- DIBUJO DE CÍRCULO RELLENO ---
    @staticmethod
    def _dibujar_circulo(img, cx, cy, r, color, alto=None, ancho=None):
        if alto is None: alto = len(img)
        if ancho is None: ancho = len(img[0])
        for y in range(cy - r, cy + r + 1):
            for x in range(cx - r, cx + r + 1):
                if (x - cx) ** 2 + (y - cy) ** 2 <= r * r:
                    if 0 <= y < alto and 0 <= x < ancho:
                        img[y][x] = color

    # --- PREPARACIÓN DEL LIENZO ---
    @staticmethod
    def _preparar_lienzo(max_val):
        ancho, alto = 650, 500
        m_inf, m_izq, m_sup, m_der = 80, 80, 70, 50
        img = [[GRAFVAG.color_fondo for _ in range(ancho)] for _ in range(alto)]

        GRAFVAG.dibujar_texto(img, (ancho // 2) - (len(GRAFVAG.titulo) * 5), 25, GRAFVAG.titulo)
        GRAFVAG.dibujar_texto(img, 10, m_sup - 30, GRAFVAG.label_y)
        GRAFVAG.dibujar_texto(img, (ancho // 2) - (len(GRAFVAG.label_x) * 5), alto - 35, GRAFVAG.label_x)

        for y in range(m_sup, alto - m_inf): img[y][m_izq] = GRAFVAG.color_texto
        for x in range(m_izq, ancho - m_der): img[alto - m_inf][x] = GRAFVAG.color_texto

        for i in range(0, 6):
            val_ref = int((i * 0.2) * max_val)
            y_p = (alto - m_inf) - int((i * 0.2) * (alto - m_inf - m_sup - 20))
            GRAFVAG.dibujar_texto(img, m_izq - 50, y_p - 5, val_ref)
            for x in range(m_izq, ancho - m_der):
                if x % 6 == 0: img[y_p][x] = (220, 220, 220)
        
        return img, ancho, alto, m_inf, m_izq, m_sup, m_der

    # ==========================================
    # PLOT BARRAS
    # ==========================================
    @staticmethod
    def plot_barras(etiquetas, valores, colores_personalizados=None):
        if not valores: return
        max_v = valores[0]
        for v in valores:
            if v > max_v: max_v = v
        if max_v == 0: max_v = 1
        img, anc, alt, m_inf, m_izq, m_sup, m_der = GRAFVAG._preparar_lienzo(max_v)
        
        n = len(valores)
        ancho_secc = (anc - m_izq - m_der) // n

        for i, v in enumerate(valores):
            h = int((v / max_v) * (alt - m_inf - m_sup - 20))
            x_c = m_izq + (i * ancho_secc) + (ancho_secc // 2)
            x_i, x_f = x_c - (ancho_secc // 3), x_c + (ancho_secc // 3)
            
            if colores_personalizados and i < len(colores_personalizados):
                color_actual = colores_personalizados[i]
            else:
                color_actual = GRAFVAG.PALETA[i % len(GRAFVAG.PALETA)]

            for y in range((alt - m_inf) - h, alt - m_inf):
                for x in range(x_i, x_f):
                    if 0 <= y < alt and 0 <= x < anc: 
                        img[y][x] = color_actual
        
        GRAFVAG._guardar(img, anc, alt, "salida_barras.ppm")

    # ==========================================
    # PLOT LINEAL
    # ==========================================
    @staticmethod
    def plot_lineal(etiquetas, valores):
        if not valores: return
        max_v = valores[0]
        for v in valores:
            if v > max_v: max_v = v
        if max_v == 0: max_v = 1
        img, anc, alt, m_inf, m_izq, m_sup, m_der = GRAFVAG._preparar_lienzo(max_v)
        
        n = len(valores)
        ancho_secc = (anc - m_izq - m_der) // n
        puntos = []

        for i, v in enumerate(valores):
            h = int((v / max_v) * (alt - m_inf - m_sup - 20))
            x_p = m_izq + (i * ancho_secc) + (ancho_secc // 2)
            y_p = (alt - m_inf) - h
            puntos.append((x_p, y_p))
            
            GRAFVAG._dibujar_circulo(img, x_p, y_p, 3, GRAFVAG.color_linea, alt, anc)
        
        for i in range(len(puntos) - 1):
            x0, y0 = puntos[i]
            x1, y1 = puntos[i + 1]
            GRAFVAG._dibujar_linea(img, x0, y0, x1, y1, GRAFVAG.color_linea, alt, anc)

        GRAFVAG._guardar(img, anc, alt, "salida_lineal.ppm")

    # ==========================================
    # PLOT PASTEL
    # ==========================================
    @staticmethod
    def plot_pastel(etiquetas, valores, colores_personalizados=None):
        if not valores: return
        ancho, alto = 650, 500
        img = [[GRAFVAG.color_fondo for _ in range(ancho)] for _ in range(alto)]
        
        cx, cy = ancho // 2, alto // 2
        radio = 150
        total = MATHVAG._sum(valores)
        angulo_inicio = 0

        GRAFVAG.dibujar_texto(img, (ancho // 2) - (len(GRAFVAG.titulo) * 5), 25, GRAFVAG.titulo)

        for i, v in enumerate(valores):
            porcentaje_str = str(int((v / total) * 100)) + "%"
            
            angulo_barrido = (v / total) * 2 * MATHVAG.PI
            if colores_personalizados:
                color = colores_personalizados[i % len(colores_personalizados)]
            else:
                color = GRAFVAG.PALETA[i % len(GRAFVAG.PALETA)]

            # Rellenar tajada
            for y in range(cy - radio, cy + radio):
                for x in range(cx - radio, cx + radio):
                    dx, dy = x - cx, y - cy
                    distancia = MATHVAG.sqrt(dx ** 2 + dy ** 2)
                    if distancia <= radio:
                        angulo_pixel = MATHVAG.atan2(dy, dx)
                        if angulo_pixel < 0: angulo_pixel += 2 * MATHVAG.PI
                        if angulo_inicio <= angulo_pixel <= (angulo_inicio + angulo_barrido):
                            img[y][x] = color
            
            # Etiqueta afuera
            angulo_medio = angulo_inicio + (angulo_barrido / 2)
            tx = int(cx + (radio + 25) * MATHVAG.cos(angulo_medio))
            ty = int(cy + (radio + 25) * MATHVAG.sin(angulo_medio))
            GRAFVAG.dibujar_texto(img, tx, ty, etiquetas[i])

            # Porcentaje adentro
            px = int(cx + (radio * 0.6) * MATHVAG.cos(angulo_medio))
            py = int(cy + (radio * 0.6) * MATHVAG.sin(angulo_medio))
            GRAFVAG.dibujar_texto(img, px - 10, py - 5, porcentaje_str, color=(255, 255, 255))

            angulo_inicio += angulo_barrido

        GRAFVAG._guardar(img, ancho, alto, "salida_pastel.ppm")

    # ==========================================
    # PLOT SCATTER (DISPERSIÓN)
    # ==========================================
    @staticmethod
    def plot_scatter(x_vals, y_vals, color=None):
        if not x_vals or not y_vals: return
        if len(x_vals) != len(y_vals):
            raise Exception("x_vals y y_vals deben tener el mismo tamaño")

        min_x = x_vals[0]
        max_x = x_vals[0]
        min_y = y_vals[0]
        max_y = y_vals[0]
        for v in x_vals:
            if v < min_x: min_x = v
            if v > max_x: max_x = v
        for v in y_vals:
            if v < min_y: min_y = v
            if v > max_y: max_y = v

        rango_x = max_x - min_x if max_x != min_x else 1
        rango_y = max_y - min_y if max_y != min_y else 1

        ancho, alto = 650, 500
        m_inf, m_izq, m_sup, m_der = 80, 80, 70, 50
        img = [[GRAFVAG.color_fondo for _ in range(ancho)] for _ in range(alto)]

        GRAFVAG.dibujar_texto(img, (ancho // 2) - (len(GRAFVAG.titulo) * 5), 25, GRAFVAG.titulo)
        GRAFVAG.dibujar_texto(img, 10, m_sup - 30, GRAFVAG.label_y)
        GRAFVAG.dibujar_texto(img, (ancho // 2) - (len(GRAFVAG.label_x) * 5), alto - 35, GRAFVAG.label_x)

        # Ejes
        for y in range(m_sup, alto - m_inf): img[y][m_izq] = GRAFVAG.color_texto
        for x in range(m_izq, ancho - m_der): img[alto - m_inf][x] = GRAFVAG.color_texto

        plot_w = ancho - m_izq - m_der
        plot_h = alto - m_inf - m_sup

        punto_color = color if color else (50, 100, 255)

        for i in range(len(x_vals)):
            px = m_izq + int(((x_vals[i] - min_x) / rango_x) * plot_w)
            py = (alto - m_inf) - int(((y_vals[i] - min_y) / rango_y) * plot_h)
            GRAFVAG._dibujar_circulo(img, px, py, 4, punto_color, alto, ancho)

        GRAFVAG._guardar(img, ancho, alto, "salida_scatter.ppm")

    # ==========================================
    # PLOT HEATMAP
    # ==========================================
    @staticmethod
    def plot_heatmap(matrix, labels=None):
        if not matrix: return
        filas = len(matrix)
        cols = len(matrix[0])

        # Encontrar min/max
        min_v = matrix[0][0]
        max_v = matrix[0][0]
        for fila in matrix:
            for v in fila:
                if v < min_v: min_v = v
                if v > max_v: max_v = v
        rango = max_v - min_v if max_v != min_v else 1

        ancho, alto = 500, 500
        margen = 60
        img = [[GRAFVAG.color_fondo for _ in range(ancho)] for _ in range(alto)]

        GRAFVAG.dibujar_texto(img, (ancho // 2) - (len(GRAFVAG.titulo) * 5), 15, GRAFVAG.titulo)

        cell_w = (ancho - 2 * margen) // cols
        cell_h = (alto - 2 * margen) // filas

        for i in range(filas):
            for j in range(cols):
                val = matrix[i][j]
                t = (val - min_v) / rango
                # Gradiente azul -> rojo
                r = int(t * 255)
                g = int((1 - MATHVAG.abs_val(t - 0.5) * 2) * 100)
                b = int((1 - t) * 255)

                x0 = margen + j * cell_w
                y0 = margen + i * cell_h
                for y in range(y0, y0 + cell_h):
                    for x in range(x0, x0 + cell_w):
                        if 0 <= y < alto and 0 <= x < ancho:
                            img[y][x] = (r, g, b)

                # Valor en la celda
                val_str = str(int(val))
                GRAFVAG.dibujar_texto(img, x0 + cell_w // 4, y0 + cell_h // 3, val_str, (255, 255, 255))

        # Labels
        if labels:
            for i, lbl in enumerate(labels):
                GRAFVAG.dibujar_texto(img, margen + i * cell_w + 5, margen - 15, str(lbl))
                GRAFVAG.dibujar_texto(img, 5, margen + i * cell_h + cell_h // 3, str(lbl))

        GRAFVAG._guardar(img, ancho, alto, "salida_heatmap.ppm")

    # ==========================================
    # PLOT LOSS (HISTORIAL DE ENTRENAMIENTO)
    # ==========================================
    @staticmethod
    def plot_loss(history, nombre="salida_loss.ppm"):
        if not history: return
        GRAFVAG.set_title("LOSS HISTORY")
        GRAFVAG.set_xlabel("EPOCH")
        GRAFVAG.set_ylabel("LOSS")
        GRAFVAG.set_line_color(255, 80, 80)
        GRAFVAG.plot_lineal(list(range(len(history))), history)
        # Renombrar
        try:
            contenido = ""
            with open("salida_lineal.ppm", "r") as f:
                contenido = f.read()
            with open(nombre, "w") as f:
                f.write(contenido)
        except:
            pass

    # ==========================================
    # PLOT HISTOGRAM
    # ==========================================
    @staticmethod
    def plot_histogram(values, bins=10):
        if not values: return
        min_v = values[0]
        max_v = values[0]
        for v in values:
            if v < min_v: min_v = v
            if v > max_v: max_v = v

        rango = max_v - min_v if max_v != min_v else 1
        bin_width = rango / bins

        # Contar frecuencias
        counts = [0] * bins
        for v in values:
            idx = int((v - min_v) / bin_width)
            if idx >= bins: idx = bins - 1
            counts[idx] += 1

        # Crear etiquetas
        etiquetas = []
        for i in range(bins):
            etiquetas.append(str(int(min_v + i * bin_width)))

        GRAFVAG.set_title("HISTOGRAMA")
        GRAFVAG.plot_barras(etiquetas, counts)

    # ==========================================
    # GUARDAR PPM
    # ==========================================
    @staticmethod
    def _guardar(imagen, ancho, alto, nombre):
        with open(nombre, "w") as f:
            f.write("P3\n" + str(ancho) + " " + str(alto) + "\n255\n")
            for fila in imagen:
                f.write(" ".join(str(r) + " " + str(g) + " " + str(b) for r, g, b in fila) + "\n")
        print("![GRAFVAG]: Generado " + nombre)