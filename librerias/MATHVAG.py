# librerias/MATHVAG.py

class MATHVAG:
    # Constantes calculadas manualmente
    PI = 3.14159265358979323846
    E  = 2.71828182845904523536

    # --- BÁSICAS ---
    @staticmethod
    def abs_val(x):
        return x if x >= 0 else -x

    @staticmethod
    def factorial(n):
        if n < 0: return None
        res = 1
        for i in range(2, int(n) + 1):
            res *= i
        return res

    # --- POTÊNCIAS E RAÍZES ---
    @staticmethod
    def power(base, exp):
        if exp == 0: return 1
        if exp < 0: return 1 / MATHVAG.power(base, -exp)
        # Para expoentes inteiros
        if int(exp) == exp:
            res = 1
            for _ in range(int(exp)):
                res *= base
            return res
        # Para expoentes fracionários, usamos a série de Taylor via exp(log)
        return MATHVAG.exp(exp * MATHVAG.log(base))

    @staticmethod
    def sqrt(x):
        if x < 0: raise Exception("Raiz de número negativo")
        if x == 0: return 0
        res = x
        for _ in range(10): # Newton-Raphson
            res = 0.5 * (res + x / res)
        return res

    @staticmethod
    def cbrt(x):
        return MATHVAG.power(x, 1/3) if x >= 0 else -MATHVAG.power(-x, 1/3)

    @staticmethod
    def nroot(x, n):
        return MATHVAG.power(x, 1/n)

    # --- EXPONENCIAL E LOGARITMOS ---
    @staticmethod
    def exp(x):
        # Série de Taylor: 1 + x + x^2/2! + x^3/3! ...
        res = 1.0
        termo = 1.0
        for i in range(1, 20):
            termo *= x / i
            res += termo
        return res

    @staticmethod
    def log(x):
        if x <= 0: raise Exception("Logaritmo de número <= 0")
        # Algoritmo de alta precisão (transformação para convergir rápido)
        n = 0
        while x > 2:
            x /= MATHVAG.E
            n += 1
        while x < 0.5:
            x *= MATHVAG.E
            n -= 1
        # Série para ln(x) em torno de 1
        z = (x - 1) / (x + 1)
        res = 0
        termo = z
        z2 = z * z
        for i in range(1, 20, 2):
            res += termo / i
            termo *= z2
        return 2 * res + n

    @staticmethod
    def log10(x): return MATHVAG.log(x) / MATHVAG.log(10)
    @staticmethod
    def log2(x): return MATHVAG.log(x) / MATHVAG.log(2)
    @staticmethod
    def logb(x, b): return MATHVAG.log(x) / MATHVAG.log(b)

    # --- TRIGONOMETRIA ---
    @staticmethod
    def sin(x):
        x = x % (2 * MATHVAG.PI)
        res = 0
        termo = x
        for i in range(1, 20, 2):
            res += termo
            termo *= -x * x / ((i + 1) * (i + 2))
        return res

    @staticmethod
    def cos(x):
        x = x % (2 * MATHVAG.PI)
        res = 0
        termo = 1
        for i in range(0, 20, 2):
            res += termo
            termo *= -x * x / ((i + 1) * (i + 2))
        return res

    @staticmethod
    def tan(x): return MATHVAG.sin(x) / MATHVAG.cos(x)

    # --- ARCO E HIPERBÓLICAS ---
    @staticmethod
    def sinh(x): return (MATHVAG.exp(x) - MATHVAG.exp(-x)) / 2
    @staticmethod
    def cosh(x): return (MATHVAG.exp(x) + MATHVAG.exp(-x)) / 2
    @staticmethod
    def tanh(x): return MATHVAG.sinh(x) / MATHVAG.cosh(x)

    @staticmethod
    def atan2(y, x):
        if x > 0: return MATHVAG.atan_aprox(y / x)
        if x < 0 and y >= 0: return MATHVAG.atan_aprox(y / x) + MATHVAG.PI
        if x < 0 and y < 0: return MATHVAG.atan_aprox(y / x) - MATHVAG.PI
        if x == 0 and y > 0: return MATHVAG.PI / 2
        if x == 0 and y < 0: return -MATHVAG.PI / 2
        return 0

    @staticmethod
    def atan_aprox(x):
        # Aproximação polinomial para convergir rápido
        if MATHVAG.abs_val(x) > 1:
            return (MATHVAG.PI/2 - MATHVAG.atan_aprox(1/x)) if x > 0 else (-MATHVAG.PI/2 - MATHVAG.atan_aprox(1/x))
        res = 0
        for n in range(15):
            signo = 1 if n % 2 == 0 else -1
            res += signo * (MATHVAG.power(x, 2*n + 1) / (2*n + 1))
        return res

    # --- TEORIA DE NÚMEROS ---
    @staticmethod
    def gcd(a, b):
        a, b = int(MATHVAG.abs_val(a)), int(MATHVAG.abs_val(b))
        while b: a, b = b, a % b
        return a

    @staticmethod
    def lcm(a, b):
        if a == 0 or b == 0: return 0
        return int(MATHVAG.abs_val(a * b) / MATHVAG.gcd(a, b))

    @staticmethod
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(MATHVAG.sqrt(n)) + 1):
            if n % i == 0: return False
        return True

    # --- REDONDEO ---
    @staticmethod
    def floor_val(x): return int(x) if x >= 0 or x == int(x) else int(x) - 1
    @staticmethod
    def ceil_val(x): return int(x) if x <= 0 or x == int(x) else int(x) + 1
    @staticmethod
    def clamp(x, lo, hi): return lo if x < lo else (hi if x > hi else x)
    @staticmethod
    def degrees(r): return r * 180 / MATHVAG.PI
    @staticmethod
    def radians(d): return d * MATHVAG.PI / 180

    @staticmethod
    def mean(lista):
        if not lista: return 0
        return sum(lista) / len(lista)

   
    #aqui se agregaran todas las funciones de estadistica
    @staticmethod
    def median(lista):
        if not lista: return 0
        n = len(lista)
        # Ordenamiento manual (Bubble sort para no usar sort de Python)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        
        if n % 2 == 0:
            return (lista[n//2 - 1] + lista[n//2]) / 2
        return lista[n//2]

    
    #aqui se agregaran todas las funciones de estadistica
    @staticmethod
    def variance(lista):
        if len(lista) < 2: return 0
        m = MATHVAG.mean(lista)
        return sum((x - m)**2 for x in lista) / (len(lista) - 1)



    #aqui se agregaran todas las funciones de vectores
    @staticmethod
    def dot_product(v1, v2):
        if len(v1) != len(v2): raise Exception("Vectores de diferente tamaño")
        return sum(x * y for x, y in zip(v1, v2))

    @staticmethod
    def norm(v):
        # Magnitud de un vector usando tu sqrt manual
        return MATHVAG.sqrt(sum(x*x for x in v))


    #aqui se agregaran todas las funciones de combinatoria
    @staticmethod
    def combinations(n, k):
        # nCr = n! / (k! * (n-k)!)
        return MATHVAG.factorial(n) // (MATHVAG.factorial(k) * MATHVAG.factorial(n - k))


# --- ARCOS (Faltantes para completar el test.py) ---
    @staticmethod
    def asin(x):
        if MATHVAG.abs_val(x) > 1: raise Exception("Error: Dominio de asin")
        # Usamos la relación: asin(x) = atan(x / sqrt(1 - x^2))
        return MATHVAG.atan_aprox(x / MATHVAG.sqrt(1 - x*x))

    @staticmethod
    def acos(x):
        if MATHVAG.abs_val(x) > 1: raise Exception("Error: Dominio de acos")
        # Usamos la relación: acos(x) = PI/2 - asin(x)
        return (MATHVAG.PI / 2) - MATHVAG.asin(x)

    @staticmethod
    def atan(x):
        # Mapeamos 'atan' al nombre que ya tienes programado
        return MATHVAG.atan_aprox(x)
        
    @staticmethod
    def permutations(n, k):
        # nPr = n! / (n-k)!
        return MATHVAG.factorial(n) // MATHVAG.factorial(n - k)

    # --- REDONDEO Y CONTROL  ---
    @staticmethod
    def round_val(x, dec=0):
        # Redondeo manual sin usar round() de Python
        factor = 10**dec
        return int(x * factor + 0.5) / factor

    @staticmethod
    def permutations(n, k):
        # nPr = n! / (n-k)!
        return MATHVAG.factorial(n) // MATHVAG.factorial(n - k)

    @staticmethod
    def e_val():
        return MATHVAG.E

    @staticmethod
    def pi_val():
        return MATHVAG.PI

    # --- ARCOS (Para que no fallen asin/acos/atan) ---
    @staticmethod
    def asin(x):
        if MATHVAG.abs_val(x) > 1: raise Exception("Error: Dominio de asin")
        return MATHVAG.atan_aprox(x / MATHVAG.sqrt(1 - x*x))

    @staticmethod
    def acos(x):
        return (MATHVAG.PI / 2) - MATHVAG.asin(x)

    @staticmethod
    def atan(x):
        return MATHVAG.atan_aprox(x)


    @staticmethod
    def standard_deviation(lista):
        """Calcula la desviación estándar usando la varianza y la raíz de la propia librería"""
        if not lista: return 0
        v = MATHVAG.variance(lista)
        return MATHVAG.sqrt(v)

    @staticmethod
    def sigmoid(x):
        """Función Sigmoide (útil para lógica de redes neuronales)"""
        return 1 / (1 + MATHVAG.exp(-x))

    @staticmethod
    def root(x, n):
        """Raíz n-ésima genérica"""
        if x < 0 and n % 2 == 0: raise Exception("Raíz par de número negativo")
        return x**(1/n) if x >= 0 else -((-x)**(1/n))

    @staticmethod
    def _sum(lista):
        """Suma manual de colecciones para soporte interno del motor gráfico"""
        total = 0
        for x in lista:
            total += x
        return total# librerias/MATHVAG.py
# Runtime matemático completo para VAGAX — CERO imports nativos

class MATHVAG:
    # =========================================
    # CONSTANTES
    # =========================================
    PI = 3.14159265358979323846
    E  = 2.71828182845904523536
    INF = float('inf')
    NEG_INF = float('-inf')

    # =========================================
    # BÁSICAS
    # =========================================
    @staticmethod
    def abs_val(x):
        return x if x >= 0 else -x

    @staticmethod
    def max_val(a, b):
        return a if a >= b else b

    @staticmethod
    def min_val(a, b):
        return a if a <= b else b

    @staticmethod
    def sign(x):
        if x > 0: return 1
        if x < 0: return -1
        return 0

    @staticmethod
    def factorial(n):
        if n < 0: return None
        res = 1
        for i in range(2, int(n) + 1):
            res *= i
        return res

    # =========================================
    # SUMATORIAS MANUALES (sin built-in sum)
    # =========================================
    @staticmethod
    def _sum(lista):
        s = 0
        for x in lista:
            s += x
        return s

    @staticmethod
    def _sum_product(a, b):
        s = 0
        for i in range(len(a)):
            s += a[i] * b[i]
        return s

    # =========================================
    # POTENCIAS Y RAÍCES
    # =========================================
    @staticmethod
    def power(base, exp):
        if exp == 0: return 1
        if exp < 0: return 1 / MATHVAG.power(base, -exp)
        if int(exp) == exp:
            res = 1
            for _ in range(int(exp)):
                res *= base
            return res
        return MATHVAG.exp(exp * MATHVAG.log(base))

    @staticmethod
    def sqrt(x):
        if x < 0: raise Exception("Raíz de número negativo")
        if x == 0: return 0.0
        res = x
        for _ in range(50):
            res = 0.5 * (res + x / res)
        return res

    @staticmethod
    def cbrt(x):
        return MATHVAG.power(x, 1/3) if x >= 0 else -MATHVAG.power(-x, 1/3)

    @staticmethod
    def nroot(x, n):
        return MATHVAG.power(x, 1/n)

    # =========================================
    # EXPONENCIAL Y LOGARITMOS
    # =========================================
    @staticmethod
    def exp(x):
        # Manejo de overflow
        if x > 700: return float('inf')
        if x < -700: return 0.0
        # Range reduction: exp(x) = exp(k) * exp(r) donde x = k + r
        k = int(x)
        r = x - k
        # exp(r) por Taylor (|r| < 1)
        res = 1.0
        termo = 1.0
        for i in range(1, 30):
            termo *= r / i
            res += termo
        # exp(k) por cuadrado iterado
        if k >= 0:
            base = MATHVAG.E
            ek = 1.0
            for _ in range(k):
                ek *= base
        else:
            base = MATHVAG.E
            ek = 1.0
            for _ in range(-k):
                ek *= base
            ek = 1.0 / ek
        return ek * res

    @staticmethod
    def log(x):
        if x <= 0: raise Exception("Logaritmo de número <= 0")
        n = 0
        while x > 2:
            x /= MATHVAG.E
            n += 1
        while x < 0.5:
            x *= MATHVAG.E
            n -= 1
        z = (x - 1) / (x + 1)
        res = 0
        termo = z
        z2 = z * z
        for i in range(1, 40, 2):
            res += termo / i
            termo *= z2
        return 2 * res + n

    @staticmethod
    def log10(x): return MATHVAG.log(x) / MATHVAG.log(10)

    @staticmethod
    def log2(x): return MATHVAG.log(x) / MATHVAG.log(2)

    @staticmethod
    def logb(x, b): return MATHVAG.log(x) / MATHVAG.log(b)

    # =========================================
    # TRIGONOMETRÍA
    # =========================================
    @staticmethod
    def sin(x):
        x = x % (2 * MATHVAG.PI)
        res = 0
        termo = x
        for i in range(1, 30, 2):
            res += termo
            termo *= -x * x / ((i + 1) * (i + 2))
        return res

    @staticmethod
    def cos(x):
        x = x % (2 * MATHVAG.PI)
        res = 0
        termo = 1
        for i in range(0, 30, 2):
            res += termo
            termo *= -x * x / ((i + 1) * (i + 2))
        return res

    @staticmethod
    def tan(x): return MATHVAG.sin(x) / MATHVAG.cos(x)

    # =========================================
    # HIPERBÓLICAS
    # =========================================
    @staticmethod
    def sinh(x): return (MATHVAG.exp(x) - MATHVAG.exp(-x)) / 2

    @staticmethod
    def cosh(x): return (MATHVAG.exp(x) + MATHVAG.exp(-x)) / 2

    @staticmethod
    def tanh(x): return MATHVAG.sinh(x) / MATHVAG.cosh(x)

    # =========================================
    # ARCO-TRIGONOMÉTRICAS
    # =========================================
    @staticmethod
    def atan_aprox(x):
        if MATHVAG.abs_val(x) > 1:
            if x > 0:
                return MATHVAG.PI / 2 - MATHVAG.atan_aprox(1 / x)
            else:
                return -MATHVAG.PI / 2 - MATHVAG.atan_aprox(1 / x)
        res = 0
        for n in range(20):
            signo = 1 if n % 2 == 0 else -1
            res += signo * (MATHVAG.power(x, 2 * n + 1) / (2 * n + 1))
        return res

    @staticmethod
    def atan(x):
        return MATHVAG.atan_aprox(x)

    @staticmethod
    def atan2(y, x):
        if x > 0: return MATHVAG.atan_aprox(y / x)
        if x < 0 and y >= 0: return MATHVAG.atan_aprox(y / x) + MATHVAG.PI
        if x < 0 and y < 0: return MATHVAG.atan_aprox(y / x) - MATHVAG.PI
        if x == 0 and y > 0: return MATHVAG.PI / 2
        if x == 0 and y < 0: return -MATHVAG.PI / 2
        return 0

    @staticmethod
    def asin(x):
        if MATHVAG.abs_val(x) > 1: raise Exception("Error: Dominio de asin")
        return MATHVAG.atan_aprox(x / MATHVAG.sqrt(1 - x * x))

    @staticmethod
    def acos(x):
        if MATHVAG.abs_val(x) > 1: raise Exception("Error: Dominio de acos")
        return (MATHVAG.PI / 2) - MATHVAG.asin(x)

    # =========================================
    # TEORÍA DE NÚMEROS
    # =========================================
    @staticmethod
    def gcd(a, b):
        a, b = int(MATHVAG.abs_val(a)), int(MATHVAG.abs_val(b))
        while b: a, b = b, a % b
        return a

    @staticmethod
    def lcm(a, b):
        if a == 0 or b == 0: return 0
        return int(MATHVAG.abs_val(a * b) / MATHVAG.gcd(a, b))

    @staticmethod
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(MATHVAG.sqrt(n)) + 1):
            if n % i == 0: return False
        return True

    # =========================================
    # COMBINATORIA
    # =========================================
    @staticmethod
    def combinations(n, k):
        return MATHVAG.factorial(n) // (MATHVAG.factorial(k) * MATHVAG.factorial(n - k))

    @staticmethod
    def permutations(n, k):
        return MATHVAG.factorial(n) // MATHVAG.factorial(n - k)

    # =========================================
    # REDONDEO Y CONVERSIONES
    # =========================================
    @staticmethod
    def floor_val(x):
        return int(x) if x >= 0 or x == int(x) else int(x) - 1

    @staticmethod
    def ceil_val(x):
        return int(x) if x <= 0 or x == int(x) else int(x) + 1

    @staticmethod
    def round_val(x, dec=0):
        factor = MATHVAG.power(10, dec)
        return MATHVAG.floor_val(x * factor + 0.5) / factor

    @staticmethod
    def clamp(x, lo, hi):
        return lo if x < lo else (hi if x > hi else x)

    @staticmethod
    def degrees(r):
        return r * 180 / MATHVAG.PI

    @staticmethod
    def radians(d):
        return d * MATHVAG.PI / 180

    # =========================================
    # VECTORES
    # =========================================
    @staticmethod
    def dot_product(v1, v2):
        if len(v1) != len(v2): raise Exception("Vectores de diferente tamaño")
        return MATHVAG._sum_product(v1, v2)

    @staticmethod
    def norm(v):
        s = 0
        for x in v:
            s += x * x
        return MATHVAG.sqrt(s)

    @staticmethod
    def cross_product(v1, v2):
        if len(v1) != 3 or len(v2) != 3:
            raise Exception("Producto cruz requiere vectores de 3 dimensiones")
        return [
            v1[1] * v2[2] - v1[2] * v2[1],
            v1[2] * v2[0] - v1[0] * v2[2],
            v1[0] * v2[1] - v1[1] * v2[0]
        ]

    @staticmethod
    def normalize_vector(v):
        n = MATHVAG.norm(v)
        if n == 0: raise Exception("No se puede normalizar vector cero")
        return [x / n for x in v]

    # =========================================
    # ESTADÍSTICA
    # =========================================
    @staticmethod
    def mean(lista):
        if not lista: return 0
        return MATHVAG._sum(lista) / len(lista)

    @staticmethod
    def median(lista):
        if not lista: return 0
        n = len(lista)
        ordered = MATHVAG._sort(lista[:])
        if n % 2 == 0:
            return (ordered[n // 2 - 1] + ordered[n // 2]) / 2
        return ordered[n // 2]

    @staticmethod
    def variance(lista):
        if len(lista) < 2: return 0
        m = MATHVAG.mean(lista)
        s = 0
        for x in lista:
            s += (x - m) ** 2
        return s / (len(lista) - 1)

    @staticmethod
    def std_dev(lista):
        return MATHVAG.sqrt(MATHVAG.variance(lista))

    @staticmethod
    def covariance(x, y):
        if len(x) != len(y):
            raise Exception("Listas deben tener el mismo tamaño")
        n = len(x)
        if n < 2: return 0
        mx = MATHVAG.mean(x)
        my = MATHVAG.mean(y)
        s = 0
        for i in range(n):
            s += (x[i] - mx) * (y[i] - my)
        return s / (n - 1)

    @staticmethod
    def correlation(x, y):
        cov = MATHVAG.covariance(x, y)
        sx = MATHVAG.std_dev(x)
        sy = MATHVAG.std_dev(y)
        if sx == 0 or sy == 0: return 0
        return cov / (sx * sy)

    @staticmethod
    def percentile(lista, p):
        if not lista: return 0
        ordered = MATHVAG._sort(lista[:])
        n = len(ordered)
        k = (p / 100) * (n - 1)
        f = MATHVAG.floor_val(k)
        c = MATHVAG.ceil_val(k)
        if f == c:
            return ordered[int(k)]
        d0 = ordered[int(f)] * (c - k)
        d1 = ordered[int(c)] * (k - f)
        return d0 + d1

    @staticmethod
    def iqr(lista):
        return MATHVAG.percentile(lista, 75) - MATHVAG.percentile(lista, 25)

    # =========================================
    # FUNCIONES ML
    # =========================================
    @staticmethod
    def sigmoid(x):
        if x < -500: return 0.0
        if x > 500: return 1.0
        return 1.0 / (1.0 + MATHVAG.exp(-x))

    @staticmethod
    def sigmoid_derivative(x):
        s = MATHVAG.sigmoid(x)
        return s * (1 - s)

    @staticmethod
    def relu(x):
        return x if x > 0 else 0

    @staticmethod
    def relu_derivative(x):
        return 1 if x > 0 else 0

    @staticmethod
    def softmax(lista):
        if not lista: return []
        max_v = lista[0]
        for x in lista:
            if x > max_v:
                max_v = x
        exps = []
        for x in lista:
            exps.append(MATHVAG.exp(x - max_v))
        total = MATHVAG._sum(exps)
        result = []
        for e in exps:
            result.append(e / total)
        return result

    @staticmethod
    def entropy(probs):
        h = 0
        for p in probs:
            if p > 1e-15:
                h -= p * MATHVAG.log(p)
        return h

    @staticmethod
    def kl_divergence(p, q):
        if len(p) != len(q):
            raise Exception("Distribuciones de diferente tamaño")
        kl = 0
        for i in range(len(p)):
            if p[i] > 1e-15 and q[i] > 1e-15:
                kl += p[i] * MATHVAG.log(p[i] / q[i])
        return kl

    # =========================================
    # UTILIDADES
    # =========================================
    @staticmethod
    def linspace(start, end, n):
        if n <= 1: return [start]
        step = (end - start) / (n - 1)
        result = []
        for i in range(n):
            result.append(start + i * step)
        return result

    @staticmethod
    def _sort(lista):
        """Bubble sort manual"""
        n = len(lista)
        for i in range(n):
            for j in range(0, n - i - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        return lista

    @staticmethod
    def _argsort(lista):
        """Retorna índices que ordenarían la lista"""
        indices = list(range(len(lista)))
        n = len(indices)
        for i in range(n):
            for j in range(0, n - i - 1):
                if lista[indices[j]] > lista[indices[j + 1]]:
                    indices[j], indices[j + 1] = indices[j + 1], indices[j]
        return indices

    # =========================================
    # CONSTANTES COMO FUNCIONES
    # =========================================
    @staticmethod
    def e_val():
        return MATHVAG.E

    @staticmethod
    def pi_val():
        return MATHVAG.PI







    @staticmethod
    def mean(lista):
        if not lista: return 0
        return MATHVAG._sum(lista) / len(lista)

    @staticmethod
    def variance(lista):
        if len(lista) < 2: return 0
        m = MATHVAG.mean(lista)
        s = 0
        for x in lista:
            s += (x - m) ** 2
        return s / (len(lista) - 1)

    @staticmethod
    def std_dev(lista):
        return MATHVAG.sqrt(MATHVAG.variance(lista))

    @staticmethod
    def covariance(x, y):
        if len(x) != len(y): raise Exception("Listas deben tener el mismo tamaño")
        n = len(x)
        if n < 2: return 0
        mx, my = MATHVAG.mean(x), MATHVAG.mean(y)
        s = 0
        for i in range(n):
            s += (x[i] - mx) * (y[i] - my)
        return s / (n - 1)

    @staticmethod
    def correlation(x, y):
        cov = MATHVAG.covariance(x, y)
        sx, sy = MATHVAG.std_dev(x), MATHVAG.std_dev(y)
        if sx == 0 or sy == 0: return 0
        return cov / (sx * sy)

    @staticmethod
    def percentile(lista, p):
        if not lista: return 0
        ordered = MATHVAG._sort(lista[:])
        n = len(ordered)
        k = (p / 100) * (n - 1)
        f = MATHVAG.floor_val(k)
        c = MATHVAG.ceil_val(k)
        if f == c: return ordered[int(k)]
        return (ordered[int(f)] * (c - k)) + (ordered[int(c)] * (k - f))

    @staticmethod
    def iqr(lista):
        return MATHVAG.percentile(lista, 75) - MATHVAG.percentile(lista, 25)

    @staticmethod
    def minimo(lista):
        if len(lista) == 0: return 0.0
        m = lista[0]
        for x in lista:
            if x < m: m = x
        return float(m)

    @staticmethod
    def maximo(lista):
        if len(lista) == 0: return 0.0
        m = lista[0]
        for x in lista:
            if x > m: m = x
        return float(m)

    @staticmethod
    def rango(lista):
        if len(lista) == 0: return 0.0
        return MATHVAG.maximo(lista) - MATHVAG.minimo(lista)

    @staticmethod
    def promedio(lista):
        if len(lista) == 0: return 0.0
        return MATHVAG._sum(lista) / len(lista)

    @staticmethod
    def mediana(lista):
        n = len(lista)
        if n == 0: return 0.0
        lista_ordenada = MATHVAG._sort(lista[:])
        mitad = n // 2
        if n % 2 != 0: return float(lista_ordenada[mitad])
        return (lista_ordenada[mitad - 1] + lista_ordenada[mitad]) / 2.0

    @staticmethod
    def _raiz_cuadrada(x):
        if x < 0: return 0.0
        if x == 0: return 0.0
        estimacion = x / 2.0
        while True:
            mejor_estimacion = 0.5 * (estimacion + x / estimacion)
            diferencia = mejor_estimacion - estimacion
            if diferencia < 0: diferencia = -diferencia
            if diferencia < 1e-10: return mejor_estimacion
            estimacion = mejor_estimacion

    @staticmethod
    def varianza(lista):
        n = len(lista)
        if n == 0: return 0.0
        media_val = MATHVAG.promedio(lista)
        suma_cuadrados = 0
        for x in lista:
            suma_cuadrados += (x - media_val) ** 2
        return suma_cuadrados / n

    @staticmethod
    def desviacion_estandar(lista):
        return MATHVAG._raiz_cuadrada(MATHVAG.varianza(lista))

    @staticmethod
    def moda(lista):
        if len(lista) == 0: return []
        frecuencias = {}
        for x in lista:
            frecuencias[x] = frecuencias.get(x, 0) + 1
        max_frecuencia = MATHVAG.maximo(list(frecuencias.values()))
        return [k for k, v in frecuencias.items() if v == max_frecuencia]


class VAGRandom:

    _seed = 123456789

    # =====================================================
    # CONTROL DE SEMILLA
    # =====================================================

    @staticmethod
    def set_seed(seed):
        """
        Establece la semilla global.
        """

        if not isinstance(seed, int):
            raise ValueError(
                "La semilla debe ser un entero"
            )

        VAGRandom._seed = seed

    @staticmethod
    def get_seed():
        """
        Retorna la semilla actual.
        """

        return VAGRandom._seed

    # =====================================================
    # GENERADOR LCG
    # =====================================================

    @staticmethod
    def _next():

        a = 1664525
        c = 1013904223
        m = 2**32

        VAGRandom._seed = (
            a * VAGRandom._seed + c
        ) % m

        return VAGRandom._seed

    # =====================================================
    # ENTEROS ALEATORIOS
    # =====================================================

    @staticmethod
    def randint(minimo, maximo):

        if minimo > maximo:
            raise ValueError(
                "minimo no puede ser mayor que maximo"
            )

        rango = maximo - minimo + 1

        return minimo + (
            VAGRandom._next() % rango
        )

    # =====================================================
    # FLOAT ALEATORIO [0,1]
    # =====================================================

    @staticmethod
    def random():

        return VAGRandom._next() / (2**32)

    # =====================================================
    # FLOAT EN RANGO
    # =====================================================

    @staticmethod
    def uniform(minimo, maximo):

        if minimo > maximo:
            raise ValueError(
                "minimo no puede ser mayor que maximo"
            )

        r = VAGRandom.random()

        return minimo + (
            (maximo - minimo) * r
        )

    # =====================================================
    # SELECCIÓN ALEATORIA
    # =====================================================

    @staticmethod
    def choice(lista):

        if len(lista) == 0:
            raise ValueError(
                "La lista no puede estar vacía"
            )

        indice = VAGRandom.randint(
            0,
            len(lista) - 1
        )

        return lista[indice]

    # =====================================================
    # SHUFFLE
    # =====================================================

    @staticmethod
    def shuffle(lista, inplace=True):

        if not inplace:
            lista = lista.copy()

        n = len(lista)

        for i in range(n - 1, 0, -1):

            j = VAGRandom.randint(0, i)

            lista[i], lista[j] = (
                lista[j],
                lista[i]
            )

        return lista