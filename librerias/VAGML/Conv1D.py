# librerias/VAGML/Conv1D.py
# Capa Convolucional 1D para VAGML — CERO imports nativos
from librerias.VAGML.Tensor import Tensor


class Conv1D:
    """
    Convolución 1D: aplica filtros sobre secuencias.
    Input shape:  (batch, input_length)
    Output shape: (batch, output_length) donde output_length = input_length - kernel_size + 1
    """

    def __init__(self, in_channels, out_channels, kernel_size):
        self.name = "Conv1D"
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.trainable = True
        self.input = None
        self.output = None

        # Pesos: out_channels filtros, cada uno de tamaño kernel_size
        limite = (2 / kernel_size) ** 0.5
        self.filters = []
        for _ in range(out_channels):
            filtro = []
            for _ in range(kernel_size):
                filtro.append(Tensor._uniform(-limite, limite))
            self.filters.append(filtro)

        # Bias: uno por filtro
        self.bias = [0.0] * out_channels

        self.params = {}

    def forward(self, input_tensor):
        """
        input_tensor: Tensor de shape (batch, seq_len)
        retorna: Tensor de shape (batch, out_channels * output_length)
        """
        self.input = input_tensor
        batch_size, seq_len = input_tensor.shape
        out_len = seq_len - self.kernel_size + 1

        if out_len <= 0:
            raise Exception(
                f"Conv1D: kernel_size={self.kernel_size} > seq_len={seq_len}"
            )

        resultado = []
        for b in range(batch_size):
            fila = []
            for f in range(self.out_channels):
                for i in range(out_len):
                    conv_sum = self.bias[f]
                    for k in range(self.kernel_size):
                        conv_sum += input_tensor.data[b][i + k] * self.filters[f][k]
                    fila.append(conv_sum)
            resultado.append(fila)

        self.output = Tensor(resultado)
        return self.output

    def backward(self, grad):
        """Backward pass: calcula gradientes para filtros y propaga"""
        batch_size, seq_len = self.input.shape
        out_len = seq_len - self.kernel_size + 1

        # Gradientes de filtros
        d_filters = []
        for f in range(self.out_channels):
            d_f = [0.0] * self.kernel_size
            for b in range(batch_size):
                for i in range(out_len):
                    g = grad.data[b][f * out_len + i]
                    for k in range(self.kernel_size):
                        d_f[k] += g * self.input.data[b][i + k]
            d_filters.append(d_f)

        # Gradiente de bias
        d_bias = [0.0] * self.out_channels
        for f in range(self.out_channels):
            for b in range(batch_size):
                for i in range(out_len):
                    d_bias[f] += grad.data[b][f * out_len + i]

        # Gradiente de input
        grad_input = [[0.0] * seq_len for _ in range(batch_size)]
        for b in range(batch_size):
            for f in range(self.out_channels):
                for i in range(out_len):
                    g = grad.data[b][f * out_len + i]
                    for k in range(self.kernel_size):
                        grad_input[b][i + k] += g * self.filters[f][k]

        # Actualizar gradientes almacenados
        self._grad_filters = d_filters
        self._grad_bias = d_bias

        return Tensor(grad_input)

    def parameters(self):
        return []  # Manejados internamente

    def update(self, lr):
        """Actualización manual de pesos"""
        if hasattr(self, '_grad_filters'):
            for f in range(self.out_channels):
                for k in range(self.kernel_size):
                    self.filters[f][k] -= lr * self._grad_filters[f][k]
                self.bias[f] -= lr * self._grad_bias[f]

    def __repr__(self):
        return (
            f"Conv1D(in={self.in_channels}, out={self.out_channels}, "
            f"kernel={self.kernel_size})"
        )
