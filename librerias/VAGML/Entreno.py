from librerias.VAGML.Tensor import Tensor
from librerias.VAGML.Layer import Dense
from librerias.VAGML.Activation import ReLU, Sigmoid
from librerias.VAGML.MLP import MLP
from librerias.VAGML.Data import DataLoader
from librerias.VAGML.Losses import MSE
from librerias.VAGML.Optimizers import SGD


def accuracy_binaria(y_pred, y_true):

    correctos = 0

    total = y_true.shape[0]

    for i in range(total):

        pred = y_pred.data[i][0]

        real = y_true.data[i][0]

        # Umbral binario
        pred_bin = 1 if pred >= 0.5 else 0

        if pred_bin == real:
            correctos += 1

    return correctos / total


def entrenar():

    print("\n==============================")
    print("🧠 VAGAX XOR TRAINING ENGINE")
    print("==============================\n")

    # =====================================
    # DATASET XOR
    # =====================================
    X = Tensor([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])

    y = Tensor([
        [0],
        [1],
        [1],
        [0]
    ])

    # =====================================
    # DATALOADER
    # =====================================
    loader = DataLoader(
        X,
        y,
        batch_size=4,
        shuffle=True
    )

    print(f"Dataset: {loader}\n")

    # =====================================
    # MODELO
    # =====================================
    model = MLP()

    model.add(Dense(2, 4))
    model.add(ReLU())

    model.add(Dense(4, 1))
    model.add(Sigmoid())

    print(model)

    # =====================================
    # LOSS
    # =====================================
    criterion = MSE()

    # =====================================
    # OPTIMIZER
    # =====================================
    optimizer = SGD(
        model.parameters(),
        lr=0.1
    )

    # =====================================
    # HIPERPARAMETROS
    # =====================================
    epochs = 1000

    # =====================================
    # TRAIN LOOP
    # =====================================
    for epoch in range(epochs):

        epoch_loss = 0

        for batch_x, batch_y in loader:

            # =============================
            # FORWARD
            # =============================
            pred = model.forward(batch_x)

            # =============================
            # LOSS
            # =============================
            loss = criterion.forward(
                pred,
                batch_y
            )

            epoch_loss += loss.item()

            # =============================
            # BACKWARD
            # =============================
            grad = criterion.backward(
                pred,
                batch_y
            )

            # =================================
            # BACKPROP MODELO
            # =================================
            model.backward(grad)

            # =================================
            # ACTUALIZAR PESOS
            # =================================
            optimizer.step()

            # =================================
            # LIMPIAR GRADIENTES
            # =================================
            optimizer.zero_grad()

        # =====================================
        # LOGGING
        # =====================================
        if epoch % 100 == 0:

            pred_total = model.forward(X)

            acc = accuracy_binaria(
                pred_total,
                y
            )

            print(
                f"[Epoch {epoch}] "
                f"Loss={epoch_loss:.6f} "
                f"Accuracy={acc:.2%}"
            )

    # =====================================
    # RESULTADOS FINALES
    # =====================================
    print("\n==============================")
    print("RESULTADOS FINALES")
    print("==============================")

    final_pred = model.forward(X)

    for i in range(X.shape[0]):

        entrada = X.data[i]

        pred = final_pred.data[i][0]

        pred_bin = (
            1 if pred >= 0.5 else 0
        )

        print(
            f"{entrada} -> "
            f"{pred:.6f} "
            f"(Clase: {pred_bin})"
        )


if __name__ == "__main__":

    entrenar()