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

    # --- REDONDEO Y CONTROL (Faltantes para el test.py) ---
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
