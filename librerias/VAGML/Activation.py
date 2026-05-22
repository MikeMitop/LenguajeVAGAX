# librerias/VAGML/Activation.py
# Funciones de activación para VAGML — CERO imports nativos
from librerias.VAGML.Tensor import Tensor
from librerias.MATHVAG import MATHVAG


class Activation:

    def __init__(self):
        self.input = None
        self.output = None
        self.name = "Activation"

    def forward(self, input):
        raise NotImplementedError

    def backward(self, grad):
        raise NotImplementedError

    def parameters(self):
        return []

    def __repr__(self):
        return self.name


# ==========================================
# RELU
# ==========================================
class ReLU(Activation):

    def __init__(self):
        super().__init__()
        self.name = "ReLU"

    def forward(self, input):
        self.input = input
        self.output = input.relu()
        return self.output

    def backward(self, grad):
        filas, columnas = self.input.shape
        nuevo_grad = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                x = self.input.data[i][j]
                derivada = 1 if x > 0 else 0
                fila.append(grad.data[i][j] * derivada)
            nuevo_grad.append(fila)
        return Tensor(nuevo_grad)


# ==========================================
# LEAKY RELU
# ==========================================
class LeakyReLU(Activation):

    def __init__(self, alpha=0.01):
        super().__init__()
        self.name = "LeakyReLU"
        self.alpha = alpha

    def forward(self, input):
        self.input = input
        self.output = input.leaky_relu(self.alpha)
        return self.output

    def backward(self, grad):
        filas, columnas = self.input.shape
        nuevo_grad = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                x = self.input.data[i][j]
                derivada = 1 if x > 0 else self.alpha
                fila.append(grad.data[i][j] * derivada)
            nuevo_grad.append(fila)
        return Tensor(nuevo_grad)

    def __repr__(self):
        return f"LeakyReLU(alpha={self.alpha})"


# ==========================================
# SIGMOID
# ==========================================
class Sigmoid(Activation):

    def __init__(self):
        super().__init__()
        self.name = "Sigmoid"

    def forward(self, input):
        self.input = input
        self.output = input.sigmoid()
        return self.output

    def backward(self, grad):
        filas, columnas = self.output.shape
        nuevo_grad = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                y = self.output.data[i][j]
                derivada = y * (1 - y)
                fila.append(grad.data[i][j] * derivada)
            nuevo_grad.append(fila)
        return Tensor(nuevo_grad)


# ==========================================
# TANH
# ==========================================
class Tanh(Activation):

    def __init__(self):
        super().__init__()
        self.name = "Tanh"

    def forward(self, input):
        self.input = input
        self.output = input.tanh()
        return self.output

    def backward(self, grad):
        filas, columnas = self.output.shape
        nuevo_grad = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                y = self.output.data[i][j]
                derivada = 1 - (y * y)
                fila.append(grad.data[i][j] * derivada)
            nuevo_grad.append(fila)
        return Tensor(nuevo_grad)


# ==========================================
# SOFTMAX
# ==========================================
class Softmax(Activation):

    def __init__(self):
        super().__init__()
        self.name = "Softmax"

    def forward(self, input):
        self.input = input
        self.output = input.softmax()
        return self.output

    def backward(self, grad):
        """
        Backward para softmax: grad_input[i][j] = sum_k(grad[i][k] * (softmax[i][k] * (delta_jk - softmax[i][j])))
        Simplificación cuando se usa con CrossEntropy: grad ya contiene (y_pred - y_true)
        """
        filas, columnas = self.output.shape
        nuevo_grad = []
        for i in range(filas):
            fila_grad = [0.0] * columnas
            for j in range(columnas):
                for k in range(columnas):
                    s_k = self.output.data[i][k]
                    delta = 1.0 if j == k else 0.0
                    fila_grad[j] += grad.data[i][k] * s_k * (delta - self.output.data[i][j])
            nuevo_grad.append(fila_grad)
        return Tensor(nuevo_grad)