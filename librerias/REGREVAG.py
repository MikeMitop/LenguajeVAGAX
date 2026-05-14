# librerias/REGREVAG.py
from librerias.MATHVAG import MATHVAG

class REGREVAG:
    @staticmethod
    def lin_reg_fit(x_list, y_list):
        if len(x_list) != len(y_list):
            raise Exception("Regresión Lineal: x_list y y_list deben tener la misma longitud")
        if len(x_list) == 0:
            raise Exception("Regresión Lineal: Las listas no pueden estar vacías")
        
        n = len(x_list)
        sum_x = sum(x_list)
        sum_y = sum(y_list)
        sum_xy = sum(x * y for x, y in zip(x_list, y_list))
        sum_x2 = sum(x * x for x in x_list)

        denominator = (n * sum_x2 - sum_x * sum_x)
        if denominator == 0:
            raise Exception("Regresión Lineal: Varianza cero en x_list, no se puede ajustar")
            
        m = (n * sum_xy - sum_x * sum_y) / denominator
        b = (sum_y - m * sum_x) / n

        return [m, b]

    @staticmethod
    def lin_reg_predict(model, x):
        if len(model) != 2:
            raise Exception("Regresión Lineal: El modelo debe tener 2 coeficientes [m, b]")
        return model[0] * x + model[1]

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
                # Sigmoide con manejo de overflow manual
                if z < -20:
                    p = 0.0
                elif z > 20:
                    p = 1.0
                else:
                    p = 1.0 / (1.0 + MATHVAG.exp(-z))
                
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
        if z < -20:
            return 0.0
        if z > 20:
            return 1.0
        return 1.0 / (1.0 + MATHVAG.exp(-z))
