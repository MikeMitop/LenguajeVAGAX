# librerias/MATRXVAG.py
# Álgebra Lineal completa para VAGAX — CERO imports nativos
from librerias.MATHVAG import MATHVAG


class MATRXVAG:

    # ==========================================
    # CONSTRUCTORES
    # ==========================================
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

    @staticmethod
    def mat_diag(values):
        n = len(values)
        res = MATRXVAG.mat_zeros(n, n)
        for i in range(n):
            res[i][i] = float(values[i])
        return res

    @staticmethod
    def mat_from_vector(v, as_column=True):
        if as_column:
            return [[float(x)] for x in v]
        return [[float(x) for x in v]]

    # ==========================================
    # ACCESO Y MODIFICACIÓN
    # ==========================================
    @staticmethod
    def mat_set(matriz, i, j, valor):
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

    # ==========================================
    # OPERACIONES BÁSICAS
    # ==========================================
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

    @staticmethod
    def mat_hadamard(A, B):
        """Producto elemento a elemento"""
        f, c = len(A), len(A[0])
        res = MATRXVAG.mat_zeros(f, c)
        for i in range(f):
            for j in range(c):
                res[i][j] = A[i][j] * B[i][j]
        return res

    # ==========================================
    # ÁLGEBRA LINEAL BÁSICA
    # ==========================================
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
        s = 0
        for i in range(len(v1)):
            s += v1[i] * v2[i]
        return s

    @staticmethod
    def mat_trace(A):
        n = len(A)
        if len(A[0]) < n: n = len(A[0])
        s = 0
        for i in range(n):
            s += A[i][i]
        return s

    @staticmethod
    def mat_norm(A):
        suma = 0
        for fila in A:
            for elem in fila:
                suma += elem ** 2
        return MATHVAG.sqrt(suma)

    # ==========================================
    # DETERMINANTE E INVERSA
    # ==========================================
    @staticmethod
    def mat_det(A):
        n = len(A)
        if n == 1: return A[0][0]
        if n == 2: return A[0][0] * A[1][1] - A[0][1] * A[1][0]
        det = 0
        for c in range(n):
            sub = [fila[:c] + fila[c+1:] for fila in A[1:]]
            det += ((-1) ** c) * A[0][c] * MATRXVAG.mat_det(sub)
        return det

    @staticmethod
    def mat_inverse(A):
        n = len(A)
        det = MATRXVAG.mat_det(A)
        if det == 0: raise Exception("Matriz no invertible (det=0)")
        if n == 1:
            return [[1.0 / A[0][0]]]
        if n == 2:
            return [
                [A[1][1] / det, -A[0][1] / det],
                [-A[1][0] / det, A[0][0] / det]
            ]
        adjunta = MATRXVAG.mat_zeros(n, n)
        for i in range(n):
            for j in range(n):
                sub = [fila[:j] + fila[j+1:] for fila in (A[:i] + A[i+1:])]
                adjunta[j][i] = ((-1) ** (i + j)) * MATRXVAG.mat_det(sub) / det
        return adjunta

    # ==========================================
    # RESOLUCIÓN DE SISTEMAS (Gauss-Jordan)
    # ==========================================
    @staticmethod
    def mat_solve(A, b):
        """Resuelve Ax = b usando eliminación Gaussiana con pivoteo parcial"""
        n = len(A)
        # Crear matriz aumentada
        aug = []
        for i in range(n):
            row = A[i][:] 
            if isinstance(b[i], list):
                row.append(float(b[i][0]))
            else:
                row.append(float(b[i]))
            aug.append(row)

        # Eliminación hacia adelante con pivoteo parcial
        for col in range(n):
            # Buscar pivote máximo
            max_row = col
            max_val = MATHVAG.abs_val(aug[col][col])
            for row in range(col + 1, n):
                if MATHVAG.abs_val(aug[row][col]) > max_val:
                    max_val = MATHVAG.abs_val(aug[row][col])
                    max_row = row
            aug[col], aug[max_row] = aug[max_row], aug[col]

            if MATHVAG.abs_val(aug[col][col]) < 1e-12:
                raise Exception("Sistema singular o sin solución única")

            # Eliminar columna
            for row in range(col + 1, n):
                factor = aug[row][col] / aug[col][col]
                for j in range(col, n + 1):
                    aug[row][j] -= factor * aug[col][j]

        # Sustitución hacia atrás
        x = [0.0] * n
        for i in range(n - 1, -1, -1):
            s = aug[i][n]
            for j in range(i + 1, n):
                s -= aug[i][j] * x[j]
            x[i] = s / aug[i][i]

        return x

    # ==========================================
    # DESCOMPOSICIÓN LU
    # ==========================================
    @staticmethod
    def mat_lu(A):
        """Descomposición LU: retorna (L, U)"""
        n = len(A)
        L = MATRXVAG.mat_identity(n)
        U = [fila[:] for fila in A]

        for j in range(n):
            for i in range(j + 1, n):
                if MATHVAG.abs_val(U[j][j]) < 1e-12:
                    raise Exception("Pivote cero en LU")
                factor = U[i][j] / U[j][j]
                L[i][j] = factor
                for k in range(j, n):
                    U[i][k] -= factor * U[j][k]

        return L, U

    # ==========================================
    # VALORES PROPIOS (Power Iteration + QR 2x2)
    # ==========================================
    @staticmethod
    def mat_eigenvalues_2x2(A):
        """Valores propios de una matriz 2x2 exactos"""
        a, b = A[0][0], A[0][1]
        c, d = A[1][0], A[1][1]
        tr = a + d
        det = a * d - b * c
        disc = tr * tr - 4 * det
        if disc < 0:
            raise Exception("Valores propios complejos (no soportados)")
        sqrt_disc = MATHVAG.sqrt(disc)
        return [(tr + sqrt_disc) / 2, (tr - sqrt_disc) / 2]

    @staticmethod
    def mat_eigenvalue_dominant(A, iterations=100):
        """Valor propio dominante por power iteration"""
        n = len(A)
        # Vector inicial
        v = [1.0] * n
        for _ in range(iterations):
            # Multiplicar A * v
            new_v = [0.0] * n
            for i in range(n):
                s = 0
                for j in range(n):
                    s += A[i][j] * v[j]
                new_v[i] = s
            # Normalizar
            max_val = MATHVAG.abs_val(new_v[0])
            for x in new_v:
                if MATHVAG.abs_val(x) > max_val:
                    max_val = MATHVAG.abs_val(x)
            if max_val == 0:
                return 0
            for i in range(n):
                v[i] = new_v[i] / max_val
        # Eigenvalue = (Av)·v / v·v
        Av = [0.0] * n
        for i in range(n):
            s = 0
            for j in range(n):
                s += A[i][j] * v[j]
            Av[i] = s
        num = 0
        den = 0
        for i in range(n):
            num += Av[i] * v[i]
            den += v[i] * v[i]
        return num / den if den != 0 else 0

    # ==========================================
    # RANGO
    # ==========================================
    @staticmethod
    def mat_rank(A):
        """Rango de la matriz por eliminación gaussiana"""
        m = len(A)
        n = len(A[0])
        U = [fila[:] for fila in A]
        rank = 0
        for col in range(n):
            # Buscar pivote
            pivot_row = -1
            for row in range(rank, m):
                if MATHVAG.abs_val(U[row][col]) > 1e-10:
                    pivot_row = row
                    break
            if pivot_row == -1:
                continue
            # Intercambiar
            U[rank], U[pivot_row] = U[pivot_row], U[rank]
            # Eliminar
            for row in range(rank + 1, m):
                if MATHVAG.abs_val(U[rank][col]) > 1e-12:
                    factor = U[row][col] / U[rank][col]
                    for k in range(col, n):
                        U[row][k] -= factor * U[rank][k]
            rank += 1
        return rank

    # ==========================================
    # RESHAPE Y FLATTEN
    # ==========================================
    @staticmethod
    def mat_flatten(A):
        result = []
        for fila in A:
            for elem in fila:
                result.append(elem)
        return result

    @staticmethod
    def mat_reshape(flat, filas, cols):
        if len(flat) != filas * cols:
            raise Exception("Dimensiones incompatibles para reshape")
        result = []
        idx = 0
        for i in range(filas):
            row = []
            for j in range(cols):
                row.append(flat[idx])
                idx += 1
            result.append(row)
        return result

    # ==========================================
    # CONCATENACIÓN
    # ==========================================
    @staticmethod
    def mat_vstack(A, B):
        """Apilar verticalmente"""
        if len(A[0]) != len(B[0]):
            raise Exception("Columnas incompatibles para vstack")
        result = [fila[:] for fila in A]
        for fila in B:
            result.append(fila[:])
        return result

    @staticmethod
    def mat_hstack(A, B):
        """Apilar horizontalmente"""
        if len(A) != len(B):
            raise Exception("Filas incompatibles para hstack")
        result = []
        for i in range(len(A)):
            result.append(A[i][:] + B[i][:])
        return result

    # ==========================================
    # SLICING
    # ==========================================
    @staticmethod
    def mat_slice_rows(A, start, end):
        return [fila[:] for fila in A[start:end]]

    @staticmethod
    def mat_slice_cols(A, start, end):
        return [fila[start:end] for fila in A]

    # ==========================================
    # APPLY (map sobre cada elemento)
    # ==========================================
    @staticmethod
    def mat_apply(A, func):
        """Aplica una función a cada elemento de la matriz"""
        f, c = len(A), len(A[0])
        res = MATRXVAG.mat_zeros(f, c)
        for i in range(f):
            for j in range(c):
                res[i][j] = func(A[i][j])
        return res

    # ==========================================
    # ESTADÍSTICAS DE MATRIZ
    # ==========================================
    @staticmethod
    def mat_sum(A):
        s = 0
        for fila in A:
            for v in fila:
                s += v
        return s

    @staticmethod
    def mat_mean(A):
        f, c = len(A), len(A[0])
        return MATRXVAG.mat_sum(A) / (f * c)

    @staticmethod
    def mat_max(A):
        m = A[0][0]
        for fila in A:
            for v in fila:
                if v > m: m = v
        return m

    @staticmethod
    def mat_min(A):
        m = A[0][0]
        for fila in A:
            for v in fila:
                if v < m: m = v
        return m

    @staticmethod
    def mat_sum_rows(A):
        """Suma por filas, retorna vector columna"""
        result = []
        for fila in A:
            s = 0
            for v in fila:
                s += v
            result.append([s])
        return result

    @staticmethod
    def mat_sum_cols(A):
        """Suma por columnas, retorna vector fila"""
        c = len(A[0])
        result = [0.0] * c
        for fila in A:
            for j in range(c):
                result[j] += fila[j]
        return [result]

    @staticmethod
    def mat_copy(A):
        return [fila[:] for fila in A]