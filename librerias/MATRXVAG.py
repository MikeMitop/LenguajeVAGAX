# librerias/MATRXVAG.py

class MATRXVAG:

    # --- CONSTRUCTORES ---
    @staticmethod
    def mat_zeros(filas, columnas):
        return [[0.0 for _ in range(columnas)] for _ in range(filas)]

    @staticmethod
    def mat_ones(filas, columnas):
        return [[1.0 for _ in range(columnas)] for _ in range(filas)]

    @staticmethod
    def mat_identity(n):
        res = MATRXVAG.mat_zeros(n, n)
        for i in range(n):
            res[i][i] = 1.0
        return res

    # --- ACCESO Y MODIFICACIÓN ---
    @staticmethod
    def mat_set(matriz, i, j, valor):
        # Crea una copia para mantener la inmutabilidad si se desea
        nueva = [fila[:] for fila in matriz]
        nueva[int(i)][int(j)] = float(valor)
        return nueva

    @staticmethod
    def mat_get(matriz, i, j):
        return matriz[int(i)][int(j)]

    @staticmethod
    def mat_row(matriz, i):
        return matriz[int(i)]

    @staticmethod
    def mat_col(matriz, j):
        return [fila[int(j)] for fila in matriz]

    @staticmethod
    def mat_shape(matriz):
        if not matriz: return [0, 0]
        return [len(matriz), len(matriz[0])]

    # --- OPERACIONES BÁSICAS ---
    @staticmethod
    def mat_add(A, B):
        f, c = len(A), len(A[0])
        res = MATRXVAG.mat_zeros(f, c)
        for i in range(f):
            for j in range(c):
                res[i][j] = A[i][j] + B[i][j]
        return res

    @staticmethod
    def mat_sub(A, B):
        f, c = len(A), len(A[0])
        res = MATRXVAG.mat_zeros(f, c)
        for i in range(f):
            for j in range(c):
                res[i][j] = A[i][j] - B[i][j]
        return res

    @staticmethod
    def mat_scalar(A, k):
        f, c = len(A), len(A[0])
        res = MATRXVAG.mat_zeros(f, c)
        for i in range(f):
            for j in range(c):
                res[i][j] = A[i][j] * k
        return res

    # --- ÁLGEBRA LINEAL ---
    @staticmethod
    def mat_transpose(A):
        f, c = len(A), len(A[0])
        res = MATRXVAG.mat_zeros(c, f)
        for i in range(f):
            for j in range(c):
                res[j][i] = A[i][j]
        return res

    @staticmethod
    def mat_mul(A, B):
        f1, c1 = len(A), len(A[0])
        f2, c2 = len(B), len(B[0])
        if c1 != f2: raise Exception("Dimensiones incompatibles para multiplicar")
        res = MATRXVAG.mat_zeros(f1, c2)
        for i in range(f1):
            for j in range(c2):
                suma = 0
                for k in range(c1):
                    suma += A[i][k] * B[k][j]
                res[i][j] = suma
        return res

    @staticmethod
    def mat_dot(v1, v2):
        # Producto punto de vectores (listas simples)
        return sum(x * y for x, y in zip(v1, v2))

    @staticmethod
    def mat_trace(A):
        n = min(len(A), len(A[0]))
        return sum(A[i][i] for i in range(n))

    @staticmethod
    def mat_norm(A):
        from librerias.MATHVAG import MATHVAG
        suma = 0
        for fila in A:
            for elem in fila:
                suma += elem**2
        return MATHVAG.sqrt(suma)

    # --- AVANZADAS (Determinante e Inversa) ---
    @staticmethod
    def mat_det(A):
        n = len(A)
        if n == 1: return A[0][0]
        if n == 2: return A[0][0]*A[1][1] - A[0][1]*A[1][0]
        
        det = 0
        for c in range(n):
            # Cofactores
            sub = [fila[:c] + fila[c+1:] for fila in A[1:]]
            det += ((-1)**c) * A[0][c] * MATRXVAG.mat_det(sub)
        return det

    @staticmethod
    def mat_inverse(A):
        n = len(A)
        det = MATRXVAG.mat_det(A)
        if det == 0: raise Exception("Matriz no invertible")
        
        if n == 2:
            res = [[A[1][1]/det, -A[0][1]/det], [-A[1][0]/det, A[0][0]/det]]
            return res

        # Matriz de cofactores adjunta
        adjunta = MATRXVAG.mat_zeros(n, n)
        for i in range(n):
            for j in range(n):
                sub = [fila[:j] + fila[j+1:] for fila in (A[:i] + A[i+1:])]
                adjunta[j][i] = ((-1)**(i+j)) * MATRXVAG.mat_det(sub) / det
        return adjunta