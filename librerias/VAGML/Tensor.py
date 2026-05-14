from librerias.MATRXVAG import MATRXVAG
from librerias.MATHVAG import MATHVAG


class Tensor:

    # =====================================
    # GENERADOR PSEUDOALEATORIO INTERNO
    # =====================================
    _seed = 123456789

    @staticmethod
    def _rand():

        # Linear Congruential Generator
        Tensor._seed = (
            1103515245 * Tensor._seed + 12345
        ) % 2147483648

        return Tensor._seed / 2147483648

    @staticmethod
    def _uniform(minimo, maximo):

        r = Tensor._rand()

        return minimo + (
            maximo - minimo
        ) * r

    # =====================================
    # CONSTRUCTOR
    # =====================================
    def __init__(
        self,
        data,
        requires_grad=False
    ):

        # Escalar
        if isinstance(data, (int, float)):

            self.data = [[float(data)]]

        # Lista
        elif isinstance(data, list):

            if len(data) == 0:

                self.data = [[]]

            elif not isinstance(
                data[0],
                list
            ):

                # Vector -> matriz fila
                self.data = [data]

            else:

                self.data = data

        else:

            raise TypeError(
                "Tipo inválido para Tensor"
            )

        # Gradientes
        self.requires_grad = requires_grad

        self.grad = None

        # Historial computacional
        self._prev = []

        self._op = None

    # =====================================
    # REPRESENTACION
    # =====================================
    def __repr__(self):

        filas, columnas = self.shape

        return (
            "Tensor(\n"
            f"  data={self.data},\n"
            f"  shape=({filas}, {columnas}),\n"
            f"  requires_grad="
            f"{self.requires_grad}\n"
            ")"
        )

    # =====================================
    # SHAPE
    # =====================================
    @property
    def shape(self):

        filas = len(self.data)

        columnas = 0

        if filas > 0:

            columnas = len(
                self.data[0]
            )

        return (filas, columnas)

    # =====================================
    # VALIDACIONES
    # =====================================
    def _check_same_shape(
        self,
        other
    ):

        if self.shape != other.shape:

            raise Exception(
                f"Shapes incompatibles: "
                f"{self.shape} != "
                f"{other.shape}"
            )

    def _check_mul_shape(
        self,
        other
    ):

        if self.shape[1] != other.shape[0]:

            raise Exception(
                f"No se puede multiplicar "
                f"{self.shape} x "
                f"{other.shape}"
            )

    # =====================================
    # SUMA
    # =====================================
    def __add__(self, other):

        self._check_same_shape(other)

        resultado = Tensor(

            MATRXVAG.mat_add(
                self.data,
                other.data
            )

        )

        resultado._prev = [
            self,
            other
        ]

        resultado._op = "add"

        return resultado

    # =====================================
    # RESTA
    # =====================================
    def __sub__(self, other):

        self._check_same_shape(other)

        resultado = Tensor(

            MATRXVAG.mat_sub(
                self.data,
                other.data
            )

        )

        resultado._prev = [
            self,
            other
        ]

        resultado._op = "sub"

        return resultado

    # =====================================
    # MULTIPLICACION
    # =====================================
    def __mul__(self, other):

        # Escalar
        if isinstance(
            other,
            (int, float)
        ):

            resultado = []

            for fila in self.data:

                nueva_fila = []

                for valor in fila:

                    nueva_fila.append(
                        valor * other
                    )

                resultado.append(
                    nueva_fila
                )

            return Tensor(resultado)

        # Tensor x Tensor
        self._check_same_shape(other)

        resultado = []

        for i in range(
            self.shape[0]
        ):

            fila = []

            for j in range(
                self.shape[1]
            ):

                fila.append(

                    self.data[i][j] *
                    other.data[i][j]

                )

            resultado.append(fila)

        tensor = Tensor(resultado)

        tensor._prev = [
            self,
            other
        ]

        tensor._op = "mul"

        return tensor

    # =====================================
    # MULTIPLICACION INVERSA
    # =====================================
    def __rmul__(self, other):

        return self.__mul__(other)

    # =====================================
    # DIVISION ESCALAR
    # =====================================
    def __truediv__(self, other):

        if isinstance(
            other,
            (int, float)
        ):

            resultado = []

            for fila in self.data:

                nueva_fila = []

                for valor in fila:

                    nueva_fila.append(
                        valor / other
                    )

                resultado.append(
                    nueva_fila
                )

            return Tensor(resultado)

        raise Exception(
            "División inválida"
        )

    # =====================================
    # MATMUL
    # =====================================
    def __matmul__(self, other):

        self._check_mul_shape(other)

        resultado = Tensor(

            MATRXVAG.mat_mul(
                self.data,
                other.data
            )

        )

        resultado._prev = [
            self,
            other
        ]

        resultado._op = "matmul"

        return resultado

    # =====================================
    # TRANSPOSE
    # =====================================
    def T(self):

        filas, columnas = self.shape

        resultado = []

        for j in range(columnas):

            fila = []

            for i in range(filas):

                fila.append(
                    self.data[i][j]
                )

            resultado.append(fila)

        return Tensor(resultado)

    def transpose(self):

        return self.T()

    # =====================================
    # RELU
    # =====================================
    def relu(self):

        resultado = []

        for fila in self.data:

            nueva_fila = []

            for valor in fila:

                nueva_fila.append(

                    max(0, valor)

                )

            resultado.append(
                nueva_fila
            )

        tensor = Tensor(resultado)

        tensor._prev = [self]

        tensor._op = "relu"

        return tensor

    # =====================================
    # SIGMOID
    # =====================================
    def sigmoid(self):

        resultado = []

        for fila in self.data:

            nueva_fila = []

            for valor in fila:

                s = (

                    1 /

                    (
                        1 +
                        MATHVAG.exp(-valor)
                    )

                )

                nueva_fila.append(s)

            resultado.append(
                nueva_fila
            )

        tensor = Tensor(resultado)

        tensor._prev = [self]

        tensor._op = "sigmoid"

        return tensor

    # =====================================
    # TANH
    # =====================================
    def tanh(self):

        resultado = []

        for fila in self.data:

            nueva_fila = []

            for valor in fila:

                nueva_fila.append(

                    MATHVAG.tanh(valor)

                )

            resultado.append(
                nueva_fila
            )

        tensor = Tensor(resultado)

        tensor._prev = [self]

        tensor._op = "tanh"

        return tensor

    # =====================================
    # SUM
    # =====================================
    def sum(self):

        total = 0

        for fila in self.data:

            for valor in fila:

                total += valor

        return Tensor(total)

    # =====================================
    # MEAN
    # =====================================
    def mean(self):

        filas, columnas = self.shape

        total = self.sum().item()

        return Tensor(

            total / (
                filas * columnas
            )

        )

    # =====================================
    # BIAS BROADCASTING
    # =====================================
    def add_bias(self, bias):

        filas, columnas = self.shape

        if bias.shape != (1, columnas):

            raise Exception(
                "Bias incompatible"
            )

        resultado = []

        for fila in self.data:

            nueva_fila = []

            for j in range(columnas):

                nueva_fila.append(

                    fila[j] +
                    bias.data[0][j]

                )

            resultado.append(
                nueva_fila
            )

        return Tensor(resultado)

    # =====================================
    # CLONE
    # =====================================
    def clone(self):

        copia = []

        for fila in self.data:

            copia.append(
                fila[:]
            )

        return Tensor(copia)

    # =====================================
    # UTILIDADES
    # =====================================
    def to_list(self):

        return self.data

    def item(self):

        if self.shape == (1, 1):

            return self.data[0][0]

        raise Exception(
            "Tensor no es escalar"
        )

    # =====================================
    # FACTORY METHODS
    # =====================================
    @staticmethod
    def zeros(
        filas,
        columnas
    ):

        return Tensor(

            MATRXVAG.mat_zeros(
                filas,
                columnas
            )

        )

    @staticmethod
    def ones(
        filas,
        columnas
    ):

        return Tensor(

            MATRXVAG.mat_ones(
                filas,
                columnas
            )

        )

    @staticmethod
    def identity(n):

        return Tensor(

            MATRXVAG.mat_identity(n)

        )

    @staticmethod
    def random(
        filas,
        columnas,
        minimo=-1,
        maximo=1
    ):

        resultado = []

        for _ in range(filas):

            fila = []

            for _ in range(columnas):

                fila.append(

                    Tensor._uniform(
                        minimo,
                        maximo
                    )

                )

            resultado.append(fila)

        return Tensor(resultado)

    # =====================================
    # BACKWARD PLACEHOLDER
    # =====================================
    def backward(self):

        print(
            "Autograd pendiente"
        )