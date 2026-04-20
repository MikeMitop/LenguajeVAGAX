# librerias/grafvag.py
import math

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

    # --- PLOTS ---
    @staticmethod
    def plot_barras(etiquetas, valores, colores_personalizados=None):
        if not valores: return
        max_v = max(valores) if valores else 1
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
                color_actual = GRAFVAG.color_barras

            for y in range((alt - m_inf) - h, alt - m_inf):
                for x in range(x_i, x_f):
                    if 0 <= y < alt and 0 <= x < anc: 
                        img[y][x] = color_actual
        
        GRAFVAG._guardar(img, anc, alt, "salida_barras_multicolor.ppm")

    @staticmethod
    def plot_lineal(etiquetas, valores):
        if not valores: return
        max_v = max(valores) if valores else 1
        img, anc, alt, m_inf, m_izq, m_sup, m_der = GRAFVAG._preparar_lienzo(max_v)
        
        n = len(valores)
        ancho_secc = (anc - m_izq - m_der) // n
        puntos = []

        for i, v in enumerate(valores):
            h = int((v / max_v) * (alt - m_inf - m_sup - 20))
            x_p = m_izq + (i * ancho_secc) + (ancho_secc // 2)
            y_p = (alt - m_inf) - h
            puntos.append((x_p, y_p))
            
            for dy in range(-3, 3):
                for dx in range(-3, 3):
                    if 0 <= y_p+dy < alt and 0 <= x_p+dx < anc:
                        img[y_p+dy][x_p+dx] = GRAFVAG.color_linea
        
        for i in range(len(puntos) - 1):
            x0, y0 = puntos[i]; x1, y1 = puntos[i+1]
            dx = abs(x1 - x0); dy = -abs(y1 - y0)
            sx = 1 if x0 < x1 else -1; sy = 1 if y0 < y1 else -1
            err = dx + dy
            while True:
                if 0 <= y0 < alt and 0 <= x0 < anc: img[y0][x0] = GRAFVAG.color_linea
                if x0 == x1 and y0 == y1: break
                e2 = 2 * err
                if e2 >= dy: err += dy; x0 += sx
                if e2 <= dx: err += dx; y0 += sy

        GRAFVAG._guardar(img, anc, alt, "salida_lineal.ppm")

    @staticmethod
    def plot_pastel(etiquetas, valores, colores_personalizados=None):
        if not valores: return
        ancho, alto = 650, 500
        img = [[GRAFVAG.color_fondo for _ in range(ancho)] for _ in range(alto)]
        
        cx, cy = ancho // 2, alto // 2
        radio = 150
        total = sum(valores)
        angulo_inicio = 0

        GRAFVAG.dibujar_texto(img, (ancho // 2) - (len(GRAFVAG.titulo) * 5), 25, GRAFVAG.titulo)

        for i, v in enumerate(valores):
            # Lógica de porcentaje (autopct)
            porcentaje_str = f"{int((v/total)*100)}%"
            
            angulo_barrido = (v / total) * 2 * math.pi
            color = colores_personalizados[i % len(colores_personalizados)] if colores_personalizados else GRAFVAG.color_barras

            # Rellenar tajada
            for y in range(cy - radio, cy + radio):
                for x in range(cx - radio, cx + radio):
                    dx, dy = x - cx, y - cy
                    distancia = math.sqrt(dx**2 + dy**2)
                    if distancia <= radio:
                        angulo_pixel = math.atan2(dy, dx)
                        if angulo_pixel < 0: angulo_pixel += 2 * math.pi
                        if angulo_inicio <= angulo_pixel <= (angulo_inicio + angulo_barrido):
                            img[y][x] = color
            
            # Etiqueta (Afuera)
            angulo_medio = angulo_inicio + (angulo_barrido / 2)
            tx = int(cx + (radio + 25) * math.cos(angulo_medio))
            ty = int(cy + (radio + 25) * math.sin(angulo_medio))
            GRAFVAG.dibujar_texto(img, tx, ty, etiquetas[i])

            # Porcentaje (Adentro - estilo autopct)
            px = int(cx + (radio * 0.6) * math.cos(angulo_medio))
            py = int(cy + (radio * 0.6) * math.sin(angulo_medio))
            GRAFVAG.dibujar_texto(img, px - 10, py - 5, porcentaje_str, color=(255,255,255))

            angulo_inicio += angulo_barrido

        GRAFVAG._guardar(img, ancho, alto, "salida_pastel.ppm")

    @staticmethod
    def _guardar(imagen, ancho, alto, nombre):
        with open(nombre, "w") as f:
            f.write(f"P3\n{ancho} {alto}\n255\n")
            for fila in imagen:
                f.write(" ".join(f"{r} {g} {b}" for r, g, b in fila) + "\n")
        print(f"![GRAFVAG]: Generado {nombre}")