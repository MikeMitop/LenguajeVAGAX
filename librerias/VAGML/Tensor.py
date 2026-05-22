# librerias/VAGML/Tensor.py
# Motor de Tensores VAGAX — CERO imports nativos
from librerias.MATRXVAG import MATRXVAG
from librerias.MATHVAG import MATHVAG


class Tensor:

    # =====================================
    # GENERADOR PSEUDOALEATORIO INTERNO
    # =====================================
    _seed = 123456789

    @staticmethod
    def _rand():
        Tensor._seed = (
            1103515245 * Tensor._seed + 12345
        ) % 2147483648
        return Tensor._seed / 2147483648

    @staticmethod
    def _uniform(minimo, maximo):
        r = Tensor._rand()
        return minimo + (maximo - minimo) * r

    @staticmethod
    def set_seed(seed):
        Tensor._seed = seed

    # =====================================
    # CONSTRUCTOR
    # =====================================
    def __init__(self, data, requires_grad=False):
        if isinstance(data, (int, float)):
            self.data = [[float(data)]]
        elif isinstance(data, list):
            if len(data) == 0:
                self.data = [[]]
            elif not isinstance(data[0], list):
                self.data = [data]
            else:
                self.data = data
        else:
            raise TypeError("Tipo inválido para Tensor")

        self.requires_grad = requires_grad
        self.grad = None
        self._prev = []
        self._op = None

    # =====================================
    # REPRESENTACIÓN
    # =====================================
    def __repr__(self):
        filas, columnas = self.shape
        return (
            "Tensor(\n"
            f"  data={self.data},\n"
            f"  shape=({filas}, {columnas}),\n"
            f"  requires_grad={self.requires_grad}\n"
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
            columnas = len(self.data[0])
        return (filas, columnas)

    # =====================================
    # VALIDACIONES
    # =====================================
    def _check_same_shape(self, other):
        if self.shape != other.shape:
            raise Exception(
                f"Shapes incompatibles: {self.shape} != {other.shape}"
            )

    def _check_mul_shape(self, other):
        if self.shape[1] != other.shape[0]:
            raise Exception(
                f"No se puede multiplicar {self.shape} x {other.shape}"
            )

    # =====================================
    # SUMA
    # =====================================
    def __add__(self, other):
        if isinstance(other, (int, float)):
            resultado = []
            for fila in self.data:
                nueva = []
                for v in fila:
                    nueva.append(v + other)
                resultado.append(nueva)
            t = Tensor(resultado)
            t._prev = [self]
            t._op = "add_scalar"
            return t

        self._check_same_shape(other)
        resultado = Tensor(MATRXVAG.mat_add(self.data, other.data))
        resultado._prev = [self, other]
        resultado._op = "add"
        return resultado

    def __radd__(self, other):
        return self.__add__(other)

    # =====================================
    # RESTA
    # =====================================
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            resultado = []
            for fila in self.data:
                nueva = []
                for v in fila:
                    nueva.append(v - other)
                resultado.append(nueva)
            t = Tensor(resultado)
            t._prev = [self]
            t._op = "sub_scalar"
            return t

        self._check_same_shape(other)
        resultado = Tensor(MATRXVAG.mat_sub(self.data, other.data))
        resultado._prev = [self, other]
        resultado._op = "sub"
        return resultado

    # =====================================
    # NEGACIÓN
    # =====================================
    def __neg__(self):
        resultado = []
        for fila in self.data:
            nueva = []
            for v in fila:
                nueva.append(-v)
            resultado.append(nueva)
        return Tensor(resultado)

    def neg(self):
        return self.__neg__()

    # =====================================
    # MULTIPLICACIÓN
    # =====================================
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            resultado = []
            for fila in self.data:
                nueva_fila = []
                for valor in fila:
                    nueva_fila.append(valor * other)
                resultado.append(nueva_fila)
            return Tensor(resultado)

        self._check_same_shape(other)
        resultado = []
        for i in range(self.shape[0]):
            fila = []
            for j in range(self.shape[1]):
                fila.append(self.data[i][j] * other.data[i][j])
            resultado.append(fila)
        tensor = Tensor(resultado)
        tensor._prev = [self, other]
        tensor._op = "mul"
        return tensor

    def __rmul__(self, other):
        return self.__mul__(other)

    # =====================================
    # DIVISIÓN ESCALAR
    # =====================================
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            resultado = []
            for fila in self.data:
                nueva_fila = []
                for valor in fila:
                    nueva_fila.append(valor / other)
                resultado.append(nueva_fila)
            return Tensor(resultado)
        raise Exception("División inválida")

    # =====================================
    # POTENCIA
    # =====================================
    def pow(self, n):
        resultado = []
        for fila in self.data:
            nueva = []
            for v in fila:
                nueva.append(MATHVAG.power(v, n))
            resultado.append(nueva)
        t = Tensor(resultado)
        t._prev = [self]
        t._op = "pow"
        return t

    # =====================================
    # MATMUL
    # =====================================
    def __matmul__(self, other):
        self._check_mul_shape(other)
        resultado = Tensor(MATRXVAG.mat_mul(self.data, other.data))
        resultado._prev = [self, other]
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
                fila.append(self.data[i][j])
            resultado.append(fila)
        return Tensor(resultado)

    def transpose(self):
        return self.T()

    # =====================================
    # ACTIVACIONES
    # =====================================
    def relu(self):
        resultado = []
        for fila in self.data:
            nueva_fila = []
            for valor in fila:
                nueva_fila.append(valor if valor > 0 else 0)
            resultado.append(nueva_fila)
        tensor = Tensor(resultado)
        tensor._prev = [self]
        tensor._op = "relu"
        return tensor

    def sigmoid(self):
        resultado = []
        for fila in self.data:
            nueva_fila = []
            for valor in fila:
                s = MATHVAG.sigmoid(valor)
                nueva_fila.append(s)
            resultado.append(nueva_fila)
        tensor = Tensor(resultado)
        tensor._prev = [self]
        tensor._op = "sigmoid"
        return tensor

    def tanh(self):
        resultado = []
        for fila in self.data:
            nueva_fila = []
            for valor in fila:
                nueva_fila.append(MATHVAG.tanh(valor))
            resultado.append(nueva_fila)
        tensor = Tensor(resultado)
        tensor._prev = [self]
        tensor._op = "tanh"
        return tensor

    def softmax(self):
        """Softmax por filas"""
        resultado = []
        for fila in self.data:
            resultado.append(MATHVAG.softmax(fila))
        tensor = Tensor(resultado)
        tensor._prev = [self]
        tensor._op = "softmax"
        return tensor

    def leaky_relu(self, alpha=0.01):
        resultado = []
        for fila in self.data:
            nueva_fila = []
            for valor in fila:
                nueva_fila.append(valor if valor > 0 else alpha * valor)
            resultado.append(nueva_fila)
        tensor = Tensor(resultado)
        tensor._prev = [self]
        tensor._op = "leaky_relu"
        return tensor

    # =====================================
    # OPERACIONES ELEMENTO A ELEMENTO
    # =====================================
    def log(self):
        resultado = []
        for fila in self.data:
            nueva = []
            for v in fila:
                nueva.append(MATHVAG.log(v) if v > 1e-15 else MATHVAG.log(1e-15))
            resultado.append(nueva)
        return Tensor(resultado)

    def exp(self):
        resultado = []
        for fila in self.data:
            nueva = []
            for v in fila:
                nueva.append(MATHVAG.exp(v))
            resultado.append(nueva)
        return Tensor(resultado)

    def abs(self):
        resultado = []
        for fila in self.data:
            nueva = []
            for v in fila:
                nueva.append(MATHVAG.abs_val(v))
            resultado.append(nueva)
        return Tensor(resultado)

    def sqrt(self):
        resultado = []
        for fila in self.data:
            nueva = []
            for v in fila:
                nueva.append(MATHVAG.sqrt(MATHVAG.abs_val(v)))
            resultado.append(nueva)
        return Tensor(resultado)

    def clip(self, min_val, max_val):
        resultado = []
        for fila in self.data:
            nueva = []
            for v in fila:
                nueva.append(MATHVAG.clamp(v, min_val, max_val))
            resultado.append(nueva)
        return Tensor(resultado)

    # =====================================
    # REDUCCIONES
    # =====================================
    def sum(self):
        total = 0
        for fila in self.data:
            for valor in fila:
                total += valor
        return Tensor(total)

    def mean(self):
        filas, columnas = self.shape
        total = self.sum().item()
        return Tensor(total / (filas * columnas))

    def max_val(self):
        m = self.data[0][0]
        for fila in self.data:
            for v in fila:
                if v > m: m = v
        return m

    def min_val(self):
        m = self.data[0][0]
        for fila in self.data:
            for v in fila:
                if v < m: m = v
        return m

    def argmax(self):
        """Retorna índice del máximo por cada fila"""
        result = []
        for fila in self.data:
            max_idx = 0
            max_v = fila[0]
            for j in range(1, len(fila)):
                if fila[j] > max_v:
                    max_v = fila[j]
                    max_idx = j
            result.append([max_idx])
        return Tensor(result)

    def argmin(self):
        """Retorna índice del mínimo por cada fila"""
        result = []
        for fila in self.data:
            min_idx = 0
            min_v = fila[0]
            for j in range(1, len(fila)):
                if fila[j] < min_v:
                    min_v = fila[j]
                    min_idx = j
            result.append([min_idx])
        return Tensor(result)

    def sum_axis(self, axis=0):
        """Suma a lo largo de un eje: 0=filas (resultado=1 fila), 1=columnas (resultado=1 col)"""
        filas, columnas = self.shape
        if axis == 0:
            result = [0.0] * columnas
            for fila in self.data:
                for j in range(columnas):
                    result[j] += fila[j]
            return Tensor([result])
        else:
            result = []
            for fila in self.data:
                s = 0
                for v in fila:
                    s += v
                result.append([s])
            return Tensor(result)

    # =====================================
    # BIAS BROADCASTING
    # =====================================
    def add_bias(self, bias):
        filas, columnas = self.shape
        if bias.shape != (1, columnas):
            raise Exception("Bias incompatible")
        resultado = []
        for fila in self.data:
            nueva_fila = []
            for j in range(columnas):
                nueva_fila.append(fila[j] + bias.data[0][j])
            resultado.append(nueva_fila)
        return Tensor(resultado)

    # =====================================
    # RESHAPE Y SLICING
    # =====================================
    def flatten(self):
        flat = []
        for fila in self.data:
            for v in fila:
                flat.append(v)
        return Tensor([flat])

    def reshape(self, filas, cols):
        flat = []
        for fila in self.data:
            for v in fila:
                flat.append(v)
        if len(flat) != filas * cols:
            raise Exception(
                f"No se puede reshape {self.shape} a ({filas}, {cols})"
            )
        result = []
        idx = 0
        for i in range(filas):
            row = []
            for j in range(cols):
                row.append(flat[idx])
                idx += 1
            result.append(row)
        return Tensor(result)

    def slice_rows(self, start, end):
        return Tensor([fila[:] for fila in self.data[start:end]])

    def slice_cols(self, start, end):
        return Tensor([fila[start:end] for fila in self.data])

    # =====================================
    # CONCATENACIÓN
    # =====================================
    def concat(self, other, axis=0):
        if axis == 0:
            if self.shape[1] != other.shape[1]:
                raise Exception("Columnas incompatibles para concat axis=0")
            data = [fila[:] for fila in self.data]
            for fila in other.data:
                data.append(fila[:])
            return Tensor(data)
        else:
            if self.shape[0] != other.shape[0]:
                raise Exception("Filas incompatibles para concat axis=1")
            data = []
            for i in range(self.shape[0]):
                data.append(self.data[i][:] + other.data[i][:])
            return Tensor(data)

    # =====================================
    # CLONE Y UTILIDADES
    # =====================================
    def clone(self):
        copia = []
        for fila in self.data:
            copia.append(fila[:])
        return Tensor(copia)

    def to_list(self):
        return self.data

    def to_flat_list(self):
        result = []
        for fila in self.data:
            for v in fila:
                result.append(v)
        return result

    def item(self):
        if self.shape == (1, 1):
            return self.data[0][0]
        raise Exception("Tensor no es escalar")

    def fill_(self, value):
        """Llena el tensor con un valor (in-place)"""
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                self.data[i][j] = float(value)
        return self

    # =====================================
    # COMPARACIONES
    # =====================================
    def equal(self, other):
        """Retorna tensor de 1s y 0s donde son iguales"""
        if isinstance(other, (int, float)):
            result = []
            for fila in self.data:
                nueva = []
                for v in fila:
                    nueva.append(1.0 if v == other else 0.0)
                result.append(nueva)
            return Tensor(result)
        self._check_same_shape(other)
        result = []
        for i in range(self.shape[0]):
            fila = []
            for j in range(self.shape[1]):
                fila.append(1.0 if self.data[i][j] == other.data[i][j] else 0.0)
            result.append(fila)
        return Tensor(result)

    # =====================================
    # FACTORY METHODS
    # =====================================
    @staticmethod
    def zeros(filas, columnas):
        return Tensor(MATRXVAG.mat_zeros(filas, columnas))

    @staticmethod
    def ones(filas, columnas):
        return Tensor(MATRXVAG.mat_ones(filas, columnas))

    @staticmethod
    def identity(n):
        return Tensor(MATRXVAG.mat_identity(n))

    @staticmethod
    def random(filas, columnas, minimo=-1, maximo=1):
        resultado = []
        for _ in range(filas):
            fila = []
            for _ in range(columnas):
                fila.append(Tensor._uniform(minimo, maximo))
            resultado.append(fila)
        return Tensor(resultado)

    @staticmethod
    def random_normal(filas, columnas, mu=0, sigma=1):
        """Distribución normal aproximada (Box-Muller)"""
        resultado = []
        for _ in range(filas):
            fila = []
            for _ in range(columnas):
                u1 = Tensor._rand()
                u2 = Tensor._rand()
                if u1 < 1e-10: u1 = 1e-10
                z = MATHVAG.sqrt(-2 * MATHVAG.log(u1)) * MATHVAG.cos(2 * MATHVAG.PI * u2)
                fila.append(mu + sigma * z)
            resultado.append(fila)
        return Tensor(resultado)

    @staticmethod
    def from_list(data):
        return Tensor(data)

    @staticmethod
    def arange(start, end, step=1):
        result = []
        v = start
        while v < end:
            result.append(float(v))
            v += step
        return Tensor([result])

    # =====================================
    # BACKWARD PLACEHOLDER
    # =====================================
    def backward(self):
        print("Autograd pendiente")