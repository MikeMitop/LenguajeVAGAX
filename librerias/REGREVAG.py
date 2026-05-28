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
    # REGRESIÓN LOGÍSTICA MULTIVARIABLE
    # Para datasets de +10.000 filas.
    # Usa mini-batch SGD + normalización Z-score.
    # ==========================================

    @staticmethod
    def log_reg_normalizar(X_matrix):
        """
        Normalización Z-score sobre cada columna feature.
        Retorna (X_norm, medias, desv_std).
        X_matrix : lista de listas  [[x1,x2,...], ...]
        """
        if not X_matrix:
            raise Exception("log_reg_normalizar: matriz vacía")
        n = len(X_matrix)
        k = len(X_matrix[0])

        # Calcular media y std por columna
        medias = []
        stds   = []
        for j in range(k):
            col = [X_matrix[i][j] for i in range(n)]
            mu  = MATHVAG.mean(col)
            sd  = MATHVAG.std_dev(col)
            medias.append(mu)
            stds.append(sd if sd != 0 else 1.0)

        # Normalizar
        X_norm = []
        for i in range(n):
            fila = [(X_matrix[i][j] - medias[j]) / stds[j] for j in range(k)]
            X_norm.append(fila)

        return [X_norm, medias, stds]

    @staticmethod
    def log_reg_normalizar_con(X_matrix, medias, stds):
        """
        Aplica normalización Z-score usando medias y stds ya calculados.
        Útil para normalizar datos de prueba con los parámetros de entrenamiento.
        """
        k = len(medias)
        X_norm = []
        for fila in X_matrix:
            f_norm = [(fila[j] - medias[j]) / stds[j] for j in range(k)]
            X_norm.append(f_norm)
        return X_norm

    @staticmethod
    def log_reg_multi_fit(X_matrix, y_list, lr=0.1, epochs=100, batch_size=64, verbose=True):
        """
        Entrena regresión logística multivariable usando mini-batch SGD.
        Apto para datasets de +10.000 filas.

        X_matrix  : lista de listas [[x1, x2, ...], ...]  (ya normalizados)
        y_list    : lista de etiquetas binarias [0, 1, ...]
        lr        : tasa de aprendizaje (default 0.1)
        epochs    : número de épocas (default 100)
        batch_size: tamaño de mini-lote (default 64)
        verbose   : imprime pérdida cada 10 épocas

        Retorna lista de pesos [w1, w2, ..., wk, bias]
        """
        n = len(X_matrix)
        if n == 0:
            raise Exception("log_reg_multi_fit: datos vacíos")
        if len(X_matrix) != len(y_list):
            raise Exception("log_reg_multi_fit: X e y deben tener la misma longitud")

        k = len(X_matrix[0])  # número de features
        lr    = float(lr)
        epochs = int(epochs)
        batch_size = int(batch_size)
        if batch_size <= 0 or batch_size > n:
            batch_size = n  # batch completo

        # Inicializar pesos (ceros)
        pesos = [0.0] * k
        bias  = 0.0

        for epoch in range(epochs):
            # Mini-batches (orden fijo sin shuffle para reproducibilidad)
            for inicio in range(0, n, batch_size):
                fin = inicio + batch_size if inicio + batch_size < n else n
                b_size = fin - inicio

                dw = [0.0] * k
                db = 0.0

                for i in range(inicio, fin):
                    # z = w · x + b
                    z = bias
                    for j in range(k):
                        z += pesos[j] * X_matrix[i][j]
                    p  = MATHVAG.sigmoid(z)
                    dz = p - y_list[i]

                    for j in range(k):
                        dw[j] += dz * X_matrix[i][j]
                    db += dz

                # Actualizar parámetros
                for j in range(k):
                    pesos[j] -= lr * dw[j] / b_size
                bias -= lr * db / b_size

            # Log-loss cada 10 épocas si verbose
            if verbose and (epoch + 1) % 10 == 0:
                loss = REGREVAG._log_loss_interno(X_matrix, y_list, pesos, bias, n, k)
                print('[LOG_REG] Época ' + str(epoch + 1) +
                      '/' + str(epochs) +
                      '  log-loss: ' + str(round(loss, 6)))

        # Retornar [w1,...,wk, bias] como lista VAGAX
        resultado = list(pesos)
        resultado.append(bias)
        return resultado

    @staticmethod
    def _log_loss_interno(X_matrix, y_list, pesos, bias, n, k):
        """
        Calcula binary cross-entropy (log-loss) internamente.
        """
        eps  = 1e-15
        loss = 0.0
        for i in range(n):
            z = bias
            for j in range(k):
                z += pesos[j] * X_matrix[i][j]
            p    = MATHVAG.sigmoid(z)
            p    = max(eps, min(1 - eps, p))  # clip numérico
            yi   = y_list[i]
            loss -= yi * MATHVAG.log(p) + (1 - yi) * MATHVAG.log(1 - p)
        return loss / n

    @staticmethod
    def log_reg_multi_predict_prob(modelo, x_vec):
        """
        Predice la probabilidad P(y=1) para un vector de features.
        modelo : lista [w1, ..., wk, bias]  (retornado por log_reg_multi_fit)
        x_vec  : lista [x1, x2, ...] con la misma cantidad de features
        """
        k = len(modelo) - 1  # último elemento = bias
        z = modelo[k]        # empieza con el bias
        for j in range(k):
            z += modelo[j] * x_vec[j]
        return MATHVAG.sigmoid(z)

    @staticmethod
    def log_reg_multi_predict(modelo, x_vec, umbral=0.5):
        """
        Clasifica una muestra como 0 o 1 según el umbral.
        umbral : probabilidad de corte (default 0.5)
        """
        prob = REGREVAG.log_reg_multi_predict_prob(modelo, x_vec)
        return 1 if prob >= umbral else 0

    @staticmethod
    def log_reg_multi_predict_batch(modelo, X_matrix, umbral=0.5):
        """
        Clasifica un lote completo de muestras.
        Retorna lista de predicciones [0 o 1].
        """
        return [REGREVAG.log_reg_multi_predict(modelo, fila, umbral)
                for fila in X_matrix]

    @staticmethod
    def log_reg_multi_logloss(modelo, X_matrix, y_list):
        """
        Calcula el log-loss (binary cross-entropy) del modelo sobre los datos.
        """
        n = len(X_matrix)
        k = len(modelo) - 1
        return REGREVAG._log_loss_interno(X_matrix, y_list,
                                         modelo[:k], modelo[k], n, k)

    @staticmethod
    def log_reg_multi_accuracy(modelo, X_matrix, y_list, umbral=0.5):
        """
        Calcula la exactitud (accuracy) del modelo: fracción de predicciones correctas.
        """
        n = len(X_matrix)
        if n == 0:
            return 0.0
        correctos = 0
        for i in range(n):
            pred = REGREVAG.log_reg_multi_predict(modelo, X_matrix[i], umbral)
            if pred == int(y_list[i]):
                correctos += 1
        return correctos / n

    @staticmethod
    def log_reg_multi_confusion(modelo, X_matrix, y_list, umbral=0.5):
        """
        Calcula la matriz de confusión 2x2.
        Retorna [VP, FP, FN, VN].
        """
        vp = fp = fn = vn = 0
        for i in range(len(X_matrix)):
            pred  = REGREVAG.log_reg_multi_predict(modelo, X_matrix[i], umbral)
            real  = int(y_list[i])
            if real == 1 and pred == 1: vp += 1
            elif real == 0 and pred == 1: fp += 1
            elif real == 1 and pred == 0: fn += 1
            else:                         vn += 1
        return [vp, fp, fn, vn]

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

    @staticmethod
    def multi_lin_reg_r2(X_matrix, y_list, model):
        """
        Coeficiente de determinación R² para regresión multivariable.
        X_matrix : lista de listas de features
        y_list   : valores reales objetivo
        model    : lista [b0, b1, b2, ...] retornada por multi_lin_reg_fit
        """
        n = len(y_list)
        if n == 0:
            return 0.0
        y_mean = MATHVAG.mean(y_list)
        ss_tot = 0.0
        ss_res = 0.0
        for i in range(n):
            pred = REGREVAG.multi_lin_reg_predict(model, X_matrix[i])
            ss_res += (y_list[i] - pred) ** 2
            ss_tot += (y_list[i] - y_mean) ** 2
        if ss_tot == 0:
            return 1.0
        return 1.0 - (ss_res / ss_tot)
