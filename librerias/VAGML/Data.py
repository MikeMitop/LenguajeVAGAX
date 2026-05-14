from librerias.VAGML.Tensor import Tensor


class DataLoader:

    def __init__(
        self,
        X,
        y,
        batch_size=1,
        shuffle=True,
        drop_last=False
    ):

        # =========================
        # VALIDACIONES
        # =========================
        if X.shape[0] != y.shape[0]:

            raise Exception(
                "X e y deben tener "
                "el mismo número de filas"
            )

        self.X = X
        self.y = y

        self.batch_size = batch_size

        self.shuffle = shuffle

        self.drop_last = drop_last

        self.n_samples = X.shape[0]

        self.indices = list(
            range(self.n_samples)
        )

    # =========================
    # NUMERO DE BATCHES
    # =========================
    def __len__(self):

        if self.drop_last:

            return (
                self.n_samples //
                self.batch_size
            )

        return (
            self.n_samples +
            self.batch_size - 1
        ) // self.batch_size

    # =========================
    # SHUFFLE
    # =========================
    def _get_shuffled_indices(self):

        idx = self.indices[:]

        # Fisher-Yates
        for i in range(
            len(idx) - 1,
            0,
            -1
        ):

            j = int(
                Tensor._rand() *
                (i + 1)
            )

            idx[i], idx[j] = (
                idx[j],
                idx[i]
            )

        return idx

    # =========================
    # ITERADOR
    # =========================
    def __iter__(self):

        idx = (
            self._get_shuffled_indices()
            if self.shuffle
            else self.indices
        )

        limite = self.n_samples

        if self.drop_last:

            limite = (
                self.n_samples //
                self.batch_size
            ) * self.batch_size

        for i in range(
            0,
            limite,
            self.batch_size
        ):

            batch_idx = idx[
                i : i + self.batch_size
            ]

            batch_x = [
                self.X.data[j]
                for j in batch_idx
            ]

            batch_y = [
                self.y.data[j]
                for j in batch_idx
            ]

            yield (
                Tensor(batch_x),
                Tensor(batch_y)
            )

    # =========================
    # REPRESENTACION
    # =========================
    def __repr__(self):

        return (
            f"DataLoader("
            f"samples={self.n_samples}, "
            f"batch_size={self.batch_size}, "
            f"shuffle={self.shuffle}"
            f")"
        )