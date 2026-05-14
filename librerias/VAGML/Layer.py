from librerias.VAGML.Tensor import Tensor


class Layer:

    def __init__(self):

        # Parámetros entrenables
        self.params = {}

        # Nombre de capa
        self.name = "Layer"

        # Si la capa puede entrenarse
        self.trainable = True

        # Última entrada recibida
        self.input = None

        # Última salida generada
        self.output = None

    # Forward obligatorio
    def forward(self, input):

        raise NotImplementedError(
            "forward() no implementado"
        )

    # Backward placeholder
    def backward(self, grad):

        raise NotImplementedError(
            "backward() no implementado"
        )

    # Retorna parámetros
    def parameters(self):

        return list(self.params.values())

    def __repr__(self):

        return self.name


class Dense(Layer):

    def __init__(
        self,
        input_dim,
        output_dim,
        activation=None,
        use_bias=True
    ):

        super().__init__()

        self.name = "Dense"

        self.input_dim = input_dim
        self.output_dim = output_dim

        self.activation = activation

        self.use_bias = use_bias

        limite = (
            2 / input_dim
        ) ** 0.5

        self.W = Tensor.random(
            input_dim,
            output_dim,
            -limite,
            limite
        )

        if use_bias:

            self.B = Tensor.zeros(
                1,
                output_dim
            )

        else:

            self.B = None

        self.params["W"] = self.W

        if use_bias:
            self.params["B"] = self.B

    # =====================================
    # ACTIVACIONES
    # =====================================
    def _apply_activation(self, x):

        if self.activation is None:
            return x

        if self.activation == "relu":
            return x.relu()

        if self.activation == "sigmoid":
            return x.sigmoid()

        if self.activation == "tanh":
            return x.tanh()

        raise Exception(
            f"Activación inválida: "
            f"{self.activation}"
        )

    # =====================================
    # FORWARD
    # =====================================
    def forward(self, input):

        self.input = input

        out = input @ self.W

        if self.use_bias:

            out = out.add_bias(self.B)

        out = self._apply_activation(out)

        self.output = out

        return out

    # =====================================
    # BACKWARD
    # =====================================
    def backward(self, grad):

        input_t = self.input.transpose()

        dW = input_t @ grad

        filas, columnas = grad.shape

        bias_grad = []

        fila_bias = []

        for j in range(columnas):

            suma = 0

            for i in range(filas):

                suma += grad.data[i][j]

            fila_bias.append(suma)

        bias_grad.append(fila_bias)

        dB = Tensor(bias_grad)

        self.W.grad = dW

        if self.use_bias:

            self.B.grad = dB

        w_t = self.W.transpose()

        grad_input = grad @ w_t

        return grad_input

    # =====================================
    # REPRESENTACION
    # =====================================
    def __repr__(self):

        return (
            f"Dense("
            f"in={self.input_dim}, "
            f"out={self.output_dim}, "
            f"activation={self.activation}"
            f")"
        )