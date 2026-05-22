# librerias/VAGML/Losses.py
# Funciones de pérdida para VAGML — CERO imports nativos
from librerias.VAGML.Tensor import Tensor
from librerias.MATHVAG import MATHVAG


class Loss:

    def __init__(self):
        self.name = "Loss"

    def forward(self, y_pred, y_true):
        raise NotImplementedError

    def backward(self, y_pred, y_true):
        raise NotImplementedError

    def __repr__(self):
        return self.name


# =====================================
# MSE (Mean Squared Error)
# =====================================
class MSE(Loss):
    """Ideal para regresión"""

    def __init__(self):
        super().__init__()
        self.name = "MSE"

    def forward(self, y_pred, y_true):
        diff = y_pred - y_true
        error = diff * diff
        return error.mean()

    def backward(self, y_pred, y_true):
        filas, columnas = y_pred.shape
        n = filas * columnas
        diff = y_pred - y_true
        return diff * (2.0 / n)


# =====================================
# MAE (Mean Absolute Error)
# =====================================
class MAE(Loss):
    """Más robusta a outliers que MSE"""

    def __init__(self):
        super().__init__()
        self.name = "MAE"

    def forward(self, y_pred, y_true):
        diff = y_pred - y_true
        return diff.abs().mean()

    def backward(self, y_pred, y_true):
        filas, columnas = y_pred.shape
        n = filas * columnas
        grad = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                diff = y_pred.data[i][j] - y_true.data[i][j]
                if diff > 0:
                    fila.append(1.0 / n)
                elif diff < 0:
                    fila.append(-1.0 / n)
                else:
                    fila.append(0.0)
            grad.append(fila)
        return Tensor(grad)


# =====================================
# BCE (Binary Cross Entropy)
# =====================================
class BCE(Loss):
    """Ideal para clasificación binaria"""

    def __init__(self):
        super().__init__()
        self.name = "BCE"
        self.eps = 1e-7

    def forward(self, y_pred, y_true):
        filas, columnas = y_pred.shape
        total = 0
        for i in range(filas):
            for j in range(columnas):
                yp = y_pred.data[i][j]
                yt = y_true.data[i][j]
                if yp < self.eps: yp = self.eps
                if yp > 1 - self.eps: yp = 1 - self.eps
                loss = -(
                    yt * MATHVAG.log(yp)
                    + (1 - yt) * MATHVAG.log(1 - yp)
                )
                total += loss
        return Tensor(total / (filas * columnas))

    def backward(self, y_pred, y_true):
        filas, columnas = y_pred.shape
        grad = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                yp = y_pred.data[i][j]
                yt = y_true.data[i][j]
                if yp < self.eps: yp = self.eps
                if yp > 1 - self.eps: yp = 1 - self.eps
                derivada = (yp - yt) / (yp * (1 - yp))
                fila.append(derivada)
            grad.append(fila)
        return Tensor(grad)


# =====================================
# CROSS ENTROPY LOSS
# =====================================
class CrossEntropyLoss(Loss):
    """
    Ideal para clasificación multiclase.
    Espera y_pred con probabilidades (post-softmax) y
    y_true como one-hot encoded.
    """

    def __init__(self):
        super().__init__()
        self.name = "CrossEntropy"
        self.eps = 1e-7

    def forward(self, y_pred, y_true):
        filas, columnas = y_pred.shape
        total = 0
        for i in range(filas):
            for j in range(columnas):
                yp = y_pred.data[i][j]
                yt = y_true.data[i][j]
                if yp < self.eps: yp = self.eps
                if yp > 1.0: yp = 1.0
                if yt > 0:
                    total -= yt * MATHVAG.log(yp)
        return Tensor(total / filas)

    def backward(self, y_pred, y_true):
        """
        Cuando se usa con Softmax, el gradiente simplificado es:
        grad = y_pred - y_true (dividido por batch_size)
        """
        filas, columnas = y_pred.shape
        grad = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                yp = y_pred.data[i][j]
                yt = y_true.data[i][j]
                if yp < self.eps: yp = self.eps
                fila.append((yp - yt) / filas)
            grad.append(fila)
        return Tensor(grad)