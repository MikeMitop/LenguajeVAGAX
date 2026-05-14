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
# MSE
# =====================================
class MSE(Loss):

    """
    Mean Squared Error
    Ideal para regresión
    """

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
# BCE
# =====================================
class BCE(Loss):

    """
    Binary Cross Entropy
    Ideal para clasificación binaria
    """

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

                # Evitar log(0)
                if yp < self.eps:
                    yp = self.eps

                if yp > 1 - self.eps:
                    yp = 1 - self.eps

                loss = -(
                    yt * MATHVAG.log(yp)
                    +
                    (1 - yt) *
                    MATHVAG.log(1 - yp)
                )

                total += loss

        return Tensor(
            total / (filas * columnas)
        )

    def backward(self, y_pred, y_true):

        filas, columnas = y_pred.shape

        grad = []

        for i in range(filas):

            fila = []

            for j in range(columnas):

                yp = y_pred.data[i][j]
                yt = y_true.data[i][j]

                if yp < self.eps:
                    yp = self.eps

                if yp > 1 - self.eps:
                    yp = 1 - self.eps

                derivada = (
                    (yp - yt)
                    /
                    (yp * (1 - yp))
                )

                fila.append(derivada)

            grad.append(fila)

        return Tensor(grad)