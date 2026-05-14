from librerias.VAGML.Tensor import Tensor
from librerias.VAGML.Layer import Dense
from librerias.VAGML.Activation import ReLU, Sigmoid
from librerias.VAGML.MLP import MLP
from librerias.VAGML.Data import DataLoader
from librerias.VAGML.Losses import MSE
from librerias.VAGML.Optimizers import SGD


# ==========================================
# ACCURACY BINARIA
# ==========================================
def accuracy(y_pred, y_true):

    correctos = 0

    total = y_true.shape[0]

    for i in range(total):

        pred = y_pred.data[i][0]

        real = y_true.data[i][0]

        pred_bin = 1 if pred >= 0.5 else 0

        if pred_bin == real:
            correctos += 1

    return correctos / total


# ==========================================
# TEST ENTRENAMIENTO XOR
# ==========================================
def test_xor():

    print("\n==============================")
    print("🧠 TEST XOR - VAGML ENGINE")
    print("==============================\n")

    # ======================================
    # DATASET XOR
    # ======================================
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

    # ======================================
    # DATALOADER
    # ======================================
    loader = DataLoader(
        X,
        y,
        batch_size=4,
        shuffle=True
    )

    print("Dataset cargado correctamente")
    print(loader)

    # ======================================
    # MODELO
    # ======================================
    model = MLP()

    model.add(Dense(2, 4))
    model.add(ReLU())

    model.add(Dense(4, 1))
    model.add(Sigmoid())

    print("\nModelo:")
    print(model)

    # ======================================
    # LOSS
    # ======================================
    criterion = MSE()

    # ======================================
    # OPTIMIZER
    # ======================================
    optimizer = SGD(
        model.parameters(),
        lr=0.1
    )

    # ======================================
    # PREDICCION INICIAL
    # ======================================
    print("\n--- Predicciones Iniciales ---")

    inicial = model.forward(X)

    for i in range(X.shape[0]):

        entrada = X.data[i]

        pred = inicial.data[i][0]

        print(
            f"{entrada} -> {pred:.6f}"
        )

    # ======================================
    # ENTRENAMIENTO
    # ======================================
    epochs = 1000

    print("\n--- Entrenando ---\n")

    for epoch in range(epochs):

        total_loss = 0

        for batch_x, batch_y in loader:

            # ===============================
            # FORWARD
            # ===============================
            pred = model.forward(batch_x)

            # ===============================
            # LOSS
            # ===============================
            loss = criterion.forward(
                pred,
                batch_y
            )

            total_loss += loss.item()

            # ===============================
            # BACKWARD LOSS
            # ===============================
            grad = criterion.backward(
                pred,
                batch_y
            )

            # ===============================
            # BACKWARD MODELO
            # ===============================
            model.backward(grad)

            # ===============================
            # UPDATE PESOS
            # ===============================
            optimizer.step()

            # ===============================
            # RESET GRADIENTES
            # ===============================
            optimizer.zero_grad()

        # ==================================
        # LOGGING
        # ==================================
        if epoch % 100 == 0:

            pred_total = model.forward(X)

            acc = accuracy(
                pred_total,
                y
            )

            print(
                f"Epoch {epoch} | "
                f"Loss: {total_loss:.6f} | "
                f"Accuracy: {acc:.2%}"
            )

    # ======================================
    # RESULTADOS FINALES
    # ======================================
    print("\n==============================")
    print("RESULTADOS FINALES")
    print("==============================\n")

    final_pred = model.forward(X)

    for i in range(X.shape[0]):

        entrada = X.data[i]

        pred = final_pred.data[i][0]

        pred_bin = (
            1 if pred >= 0.5 else 0
        )

        real = y.data[i][0]

        print(
            f"Entrada: {entrada}"
        )

        print(
            f"Predicción: {pred:.6f}"
        )

        print(
            f"Clase Final: {pred_bin}"
        )

        print(
            f"Valor Esperado: {real}"
        )

        print("------------------")

    # ======================================
    # ACCURACY FINAL
    # ======================================
    final_acc = accuracy(
        final_pred,
        y
    )

    print(
        f"\nAccuracy Final: "
        f"{final_acc:.2%}"
    )

    # ======================================
    # VALIDACION
    # ======================================
    if final_acc >= 0.75:

        print(
            "\n✅ EL MODELO ESTÁ "
            "APRENDIENDO"
        )

    else:

        print(
            "\n❌ EL MODELO NO "
            "ESTÁ APRENDIENDO"
        )

        print(
            "Revisa backward()"
        )


# ==========================================
# MAIN
# ==========================================
if __name__ == "__main__":

    test_xor()