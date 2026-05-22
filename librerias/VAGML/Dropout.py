# librerias/VAGML/Dropout.py
# Regularización Dropout para VAGML — CERO imports nativos
from librerias.VAGML.Tensor import Tensor


class Dropout:
    """
    Dropout: apaga neuronas aleatoriamente durante entrenamiento.
    Durante evaluación (training=False), no modifica la entrada.
    """

    def __init__(self, rate=0.5):
        self.name = "Dropout"
        self.rate = rate
        self.training = True
        self.mask = None
        self.input = None
        self.output = None
        self.trainable = False

    def forward(self, input_tensor):
        self.input = input_tensor

        if not self.training:
            self.output = input_tensor
            return input_tensor

        filas, columnas = input_tensor.shape
        mask_data = []
        resultado = []

        for i in range(filas):
            mask_fila = []
            res_fila = []
            for j in range(columnas):
                r = Tensor._rand()
                if r < self.rate:
                    mask_fila.append(0.0)
                    res_fila.append(0.0)
                else:
                    scale = 1.0 / (1.0 - self.rate)
                    mask_fila.append(scale)
                    res_fila.append(input_tensor.data[i][j] * scale)
            mask_data.append(mask_fila)
            resultado.append(res_fila)

        self.mask = Tensor(mask_data)
        self.output = Tensor(resultado)
        return self.output

    def backward(self, grad):
        if not self.training or self.mask is None:
            return grad

        filas, columnas = grad.shape
        resultado = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                fila.append(grad.data[i][j] * self.mask.data[i][j])
            resultado.append(fila)
        return Tensor(resultado)

    def train(self):
        self.training = True

    def eval(self):
        self.training = False

    def parameters(self):
        return []

    def __repr__(self):
        return f"Dropout(rate={self.rate})"
