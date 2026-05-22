# librerias/VAGML/Optimizers.py
# Optimizadores para VAGML — CERO imports nativos
from librerias.VAGML.Tensor import Tensor
from librerias.MATHVAG import MATHVAG


class Optimizer:

    def __init__(self, parameters, lr=0.01):
        self.parameters = parameters
        self.lr = lr
        self.name = "Optimizer"

    def step(self):
        raise NotImplementedError

    def zero_grad(self):
        for p in self.parameters:
            p.grad = None

    def __repr__(self):
        return f"{self.name}(lr={self.lr})"


# =====================================
# SGD (Stochastic Gradient Descent)
# =====================================
class SGD(Optimizer):
    """SGD con momentum opcional"""

    def __init__(self, parameters, lr=0.01, momentum=0.0):
        super().__init__(parameters, lr)
        self.name = "SGD"
        self.momentum = momentum
        self.velocities = None

    def step(self):
        if self.velocities is None and self.momentum > 0:
            self.velocities = []
            for p in self.parameters:
                self.velocities.append(Tensor.zeros(p.shape[0], p.shape[1]))

        for idx, p in enumerate(self.parameters):
            if p.grad is None:
                continue
            if p.grad.shape != p.shape:
                raise Exception(
                    f"Gradiente incompatible {p.grad.shape} != {p.shape}"
                )

            if self.momentum > 0 and self.velocities is not None:
                # v = momentum * v - lr * grad
                self.velocities[idx] = (
                    self.velocities[idx] * self.momentum
                ) - (p.grad * self.lr)
                # No restar, sumar v (que ya tiene signo negativo del grad)
                nuevo = p + self.velocities[idx]
            else:
                update = p.grad * self.lr
                nuevo = p - update

            p.data = nuevo.data


# =====================================
# ADAM
# =====================================
class Adam(Optimizer):
    """
    Adam optimizer: combina momentum y RMSProp.
    """

    def __init__(self, parameters, lr=0.001, beta1=0.9, beta2=0.999, eps=1e-8):
        super().__init__(parameters, lr)
        self.name = "Adam"
        self.beta1 = beta1
        self.beta2 = beta2
        self.eps = eps
        self.t = 0

        # Momentos: m (primer momento), v (segundo momento)
        self.m = []
        self.v = []
        for p in self.parameters:
            self.m.append(Tensor.zeros(p.shape[0], p.shape[1]))
            self.v.append(Tensor.zeros(p.shape[0], p.shape[1]))

    def step(self):
        self.t += 1

        for idx, p in enumerate(self.parameters):
            if p.grad is None:
                continue
            if p.grad.shape != p.shape:
                raise Exception(
                    f"Gradiente incompatible {p.grad.shape} != {p.shape}"
                )

            filas, columnas = p.shape

            for i in range(filas):
                for j in range(columnas):
                    g = p.grad.data[i][j]

                    # m = beta1 * m + (1 - beta1) * g
                    self.m[idx].data[i][j] = (
                        self.beta1 * self.m[idx].data[i][j]
                        + (1 - self.beta1) * g
                    )

                    # v = beta2 * v + (1 - beta2) * g^2
                    self.v[idx].data[i][j] = (
                        self.beta2 * self.v[idx].data[i][j]
                        + (1 - self.beta2) * g * g
                    )

                    # Corrección de sesgo
                    m_hat = self.m[idx].data[i][j] / (1 - MATHVAG.power(self.beta1, self.t))
                    v_hat = self.v[idx].data[i][j] / (1 - MATHVAG.power(self.beta2, self.t))

                    # Actualizar parámetro
                    p.data[i][j] -= self.lr * m_hat / (MATHVAG.sqrt(v_hat) + self.eps)


# =====================================
# LEARNING RATE SCHEDULER
# =====================================
class LRScheduler:
    """Step decay: reduce lr cada `step_size` epochs por factor `gamma`"""

    def __init__(self, optimizer, step_size=100, gamma=0.1):
        self.optimizer = optimizer
        self.step_size = step_size
        self.gamma = gamma
        self.epoch = 0
        self.initial_lr = optimizer.lr

    def step(self):
        self.epoch += 1
        if self.epoch % self.step_size == 0:
            self.optimizer.lr *= self.gamma

    def get_lr(self):
        return self.optimizer.lr

    def reset(self):
        self.epoch = 0
        self.optimizer.lr = self.initial_lr

    def __repr__(self):
        return (
            f"LRScheduler(step_size={self.step_size}, "
            f"gamma={self.gamma}, current_lr={self.optimizer.lr:.6f})"
        )