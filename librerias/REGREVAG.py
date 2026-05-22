# librerias/REGREVAG.py
# Regresión completa para VAGAX — CERO imports nativos
from librerias.MATHVAG import MATHVAG
from librerias.MATRXVAG import MATRXVAG


class REGREVAG:

    # ==========================================
    # REGRESIÓN LINEAL SIMPLE
    # ==========================================
    @staticmethod
    def lin_reg_fit(x_list, y_list):
        if len(x_list) != len(y_list):
            raise Exception("Regresión Lineal: x_list y y_list deben tener la misma longitud")
        if len(x_list) == 0:
            raise Exception("Regresión Lineal: Las listas no pueden estar vacías")
        
        n = len(x_list)
        sum_x = MATHVAG._sum(x_list)
        sum_y = MATHVAG._sum(y_list)
        sum_xy = MATHVAG._sum_product(x_list, y_list)

        sum_x2 = 0
        for x in x_list:
            sum_x2 += x * x

        denominator = (n * sum_x2 - sum_x * sum_x)
        if denominator == 0:
            raise Exception("Regresión Lineal: Varianza cero en x_list")
            
        m = (n * sum_xy - sum_x * sum_y) / denominator
        b = (sum_y - m * sum_x) / n

        return [m, b]

    @staticmethod
    def lin_reg_predict(model, x):
        if len(model) != 2:
            raise Exception("Regresión Lineal: El modelo debe tener 2 coeficientes [m, b]")
        return model[0] * x + model[1]

    @staticmethod
    def lin_reg_r2(x_list, y_list, model):
        """Coeficiente de determinación R²"""
        y_mean = MATHVAG.mean(y_list)
        ss_tot = 0
        ss_res = 0
        for i in range(len(x_list)):
            pred = REGREVAG.lin_reg_predict(model, x_list[i])
            ss_res += (y_list[i] - pred) ** 2
            ss_tot += (y_list[i] - y_mean) ** 2
        if ss_tot == 0: return 1.0
        return 1 - (ss_res / ss_tot)

    # ==========================================
    # REGRESIÓN LOGÍSTICA
    # ==========================================
    @staticmethod
    def log_reg_fit(x_list, y_list, lr, epochs):
        if len(x_list) != len(y_list):
            raise Exception("Regresión Logística: x_list y y_list deben tener la misma longitud")
        if len(x_list) == 0:
            raise Exception("Regresión Logística: Las listas no pueden estar vacías")

        n = len(x_list)
        w = 0.0
        b = 0.0

        for _ in range(int(epochs)):
            dw = 0.0
            db = 0.0
            for i in range(n):
                z = w * x_list[i] + b
                p = MATHVAG.sigmoid(z)
                dz = p - y_list[i]
                dw += dz * x_list[i]
                db += dz
                
            w -= lr * (dw / n)
            b -= lr * (db / n)
            
        return [w, b]

    @staticmethod
    def log_reg_predict(model, x):
        if len(model) != 2:
            raise Exception("Regresión Logística: El modelo debe tener 2 coeficientes [w, b]")
        z = model[0] * x + model[1]
        return MATHVAG.sigmoid(z)

    # ==========================================
    # REGRESIÓN POLINOMIAL
    # ==========================================
    @staticmethod
    def poly_reg_fit(x_list, y_list, degree):
        """
        Ajusta y = a0 + a1*x + a2*x^2 + ... + ad*x^d
        Usa ecuaciones normales: (X^T * X)^-1 * X^T * y
        """
        n = len(x_list)
        if n == 0:
            raise Exception("Regresión Polinomial: Listas vacías")
        if len(x_list) != len(y_list):
            raise Exception("Regresión Polinomial: x y y deben tener la misma longitud")

        # Construir la matriz de Vandermonde X
        X = []
        for i in range(n):
            row = []
            for j in range(degree + 1):
                row.append(MATHVAG.power(x_list[i], j))
            X.append(row)

        # X^T
        Xt = MATRXVAG.mat_transpose(X)

        # X^T * X
        XtX = MATRXVAG.mat_mul(Xt, X)

        # X^T * y
        y_col = [[y_list[i]] for i in range(n)]
        Xty = MATRXVAG.mat_mul(Xt, y_col)

        # Resolver (X^T * X) * coefs = X^T * y
        b_flat = [Xty[i][0] for i in range(len(Xty))]
        coefs = MATRXVAG.mat_solve(XtX, b_flat)

        return coefs

    @staticmethod
    def poly_reg_predict(model, x):
        """Evalúa el polinomio con los coeficientes del modelo"""
        result = 0
        for i in range(len(model)):
            result += model[i] * MATHVAG.power(x, i)
        return result

    # ==========================================
    # REGRESIÓN LINEAL MULTIVARIABLE
    # ==========================================
    @staticmethod
    def multi_lin_reg_fit(X_matrix, y_list):
        """
        Regresión lineal multivariable: y = X * beta
        X_matrix: lista de listas (cada fila = muestra, cada col = feature)
        y_list: lista de valores objetivo
        Agrega columna de 1s (intercepto) automáticamente.
        Usa ecuaciones normales: beta = (X^T * X)^-1 * X^T * y
        """
        n = len(X_matrix)
        if n == 0:
            raise Exception("Regresión Multi: Datos vacíos")

        # Agregar columna de 1s (intercepto)
        X = []
        for i in range(n):
            row = [1.0]
            for v in X_matrix[i]:
                row.append(float(v))
            X.append(row)

        Xt = MATRXVAG.mat_transpose(X)
        XtX = MATRXVAG.mat_mul(Xt, X)
        
        y_col = [[float(y_list[i])] for i in range(n)]
        Xty = MATRXVAG.mat_mul(Xt, y_col)

        b_flat = [Xty[i][0] for i in range(len(Xty))]
        beta = MATRXVAG.mat_solve(XtX, b_flat)

        return beta

    @staticmethod
    def multi_lin_reg_predict(model, x_vec):
        """Predicción multivariable: y = b0 + b1*x1 + b2*x2 + ..."""
        result = model[0]  # intercepto
        for i in range(len(x_vec)):
            result += model[i + 1] * x_vec[i]
        return result
