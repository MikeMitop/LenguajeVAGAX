from librerias.VAGML.Tensor import Tensor


class Optimizer:

    def __init__(
        self,
        parameters,
        lr=0.01
    ):

        self.parameters = parameters

        self.lr = lr

        self.name = "Optimizer"

    # =====================================
    # ACTUALIZAR PARAMETROS
    # =====================================
    def step(self):

        raise NotImplementedError

    # =====================================
    # LIMPIAR GRADIENTES
    # =====================================
    def zero_grad(self):

        for p in self.parameters:

            p.grad = None

    def __repr__(self):

        return (
            f"{self.name}"
            f"(lr={self.lr})"
        )


# =====================================
# SGD
# =====================================
class SGD(Optimizer):

    """
    Stochastic Gradient Descent
    """

    def __init__(
        self,
        parameters,
        lr=0.01
    ):

        super().__init__(
            parameters,
            lr
        )

        self.name = "SGD"

    def step(self):

        for p in self.parameters:

            # Saltar si no hay gradiente
            if p.grad is None:
                continue

            # Verificar dimensiones
            if p.grad.shape != p.shape:

                raise Exception(
                    "Gradiente incompatible "
                    f"{p.grad.shape} != "
                    f"{p.shape}"
                )

            # =================================
            # W = W - lr * grad
            # =================================
            update = p.grad * self.lr

            nuevo = p - update

            p.data = nuevo.data