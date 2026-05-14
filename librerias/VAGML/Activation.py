from librerias.VAGML.Tensor import Tensor


class Activation:

    def __init__(self):

        self.input = None

        self.output = None

        self.name = "Activation"

    def forward(self, input):

        raise NotImplementedError

    def backward(self, grad):

        raise NotImplementedError

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

                # Derivada ReLU
                derivada = 1 if x > 0 else 0

                fila.append(
                    grad.data[i][j] * derivada
                )

            nuevo_grad.append(fila)

        return Tensor(nuevo_grad)


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

                # sigmoid'(x)
                derivada = y * (1 - y)

                fila.append(
                    grad.data[i][j] * derivada
                )

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

                # tanh'(x)
                derivada = 1 - (y * y)

                fila.append(
                    grad.data[i][j] * derivada
                )

            nuevo_grad.append(fila)

        return Tensor(nuevo_grad)