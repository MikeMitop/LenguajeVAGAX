from librerias.VAGML.Tensor import Tensor
from librerias.VAGML.Layer import Dense
from librerias.VAGML.Activation import ReLU, Sigmoid
from librerias.VAGML.MLP import MLP
from librerias.VAGML.Losses import MSE
from librerias.VAGML.Optimizers import SGD


# =====================================
# ACCURACY
# =====================================
def accuracy(predicciones, reales):

    correctos = 0

    total = len(predicciones.data)

    for i in range(total):

        pred = predicciones.data[i][0]

        clase = 1 if pred >= 0.5 else 0

        if clase == reales.data[i][0]:

            correctos += 1

    return (
        correctos / total
    ) * 100


# =====================================
# TEST COMPLETO
# =====================================
def test_guardado_vagml():

    print("\n==============================")
    print("🧠 TEST GUARDADO VAGML")
    print("==============================\n")

    # =================================
    # DATASET XOR
    # =================================
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

    print("Dataset XOR cargado\n")

    # =================================
    # MODELO
    # =================================
    model = MLP()

    model.add(Dense(2, 4))

    model.add(ReLU())

    model.add(Dense(4, 1))

    model.add(Sigmoid())

    print(model)

    # =================================
    # LOSS Y OPTIMIZER
    # =================================
    criterion = MSE()

    optimizer = SGD(
        model.parameters(),
        lr=0.1
    )

    # =================================
    # ENTRENAMIENTO
    # =================================
    print("\n--- ENTRENANDO ---\n")

    epochs = 1000

    for epoch in range(epochs):

        # FORWARD
        pred = model.forward(X)

        # LOSS
        loss = criterion.forward(
            pred,
            y
        )

        # BACKWARD LOSS
        grad = criterion.backward(
            pred,
            y
        )

        # LIMPIAR GRADIENTES
        optimizer.zero_grad()

        # BACKPROP
        model.backward(grad)

        # ACTUALIZAR
        optimizer.step()

        # MOSTRAR
        if epoch % 100 == 0:

            acc = accuracy(
                pred,
                y
            )

            print(
                f"Epoch {epoch} | "
                f"Loss: {loss.item():.6f} | "
                f"Accuracy: {acc:.2f}%"
            )

    # =================================
    # PREDICCIONES ORIGINALES
    # =================================
    print("\n==============================")
    print("MODELO ENTRENADO")
    print("==============================\n")

    pred_original = model.forward(X)

    for i in range(len(X.data)):

        entrada = X.data[i]

        prediccion = (
            pred_original.data[i][0]
        )

        clase = (
            1 if prediccion >= 0.5
            else 0
        )

        print(
            f"{entrada} -> "
            f"{prediccion:.6f} "
            f"(Clase {clase})"
        )

    # =================================
    # GUARDAR MODELO
    # =================================
    print("\n==============================")
    print("GUARDANDO MODELO")
    print("==============================\n")

    model.guardar_vagml(
        "xor_model.vagml"
    )

    # =================================
    # NUEVO MODELO VACIO
    # =================================
    print("\n==============================")
    print("CREANDO NUEVO MODELO")
    print("==============================\n")

    nuevo_modelo = MLP()

    nuevo_modelo.add(Dense(2, 4))

    nuevo_modelo.add(ReLU())

    nuevo_modelo.add(Dense(4, 1))

    nuevo_modelo.add(Sigmoid())

    print(
        "Nuevo modelo creado "
        "sin entrenamiento"
    )

    # =================================
    # PREDICCIONES ANTES DE CARGAR
    # =================================
    print("\n--- ANTES DE CARGAR ---\n")

    pred_sin_cargar = (
        nuevo_modelo.forward(X)
    )

    for i in range(len(X.data)):

        entrada = X.data[i]

        prediccion = (
            pred_sin_cargar.data[i][0]
        )

        print(
            f"{entrada} -> "
            f"{prediccion:.6f}"
        )

    # =================================
    # CARGAR MODELO
    # =================================
    print("\n==============================")
    print("CARGANDO MODELO")
    print("==============================\n")

    nuevo_modelo.cargar_vagml(
        "xor_model.vagml"
    )

    # =================================
    # PREDICCIONES DESPUES
    # =================================
    print("\n--- DESPUES DE CARGAR ---\n")

    pred_cargado = (
        nuevo_modelo.forward(X)
    )

    for i in range(len(X.data)):

        entrada = X.data[i]

        prediccion = (
            pred_cargado.data[i][0]
        )

        clase = (
            1 if prediccion >= 0.5
            else 0
        )

        print(
            f"{entrada} -> "
            f"{prediccion:.6f} "
            f"(Clase {clase})"
        )

    # =================================
    # VERIFICACION
    # =================================
    print("\n==============================")
    print("VERIFICACION")
    print("==============================\n")

    iguales = True

    for i in range(len(X.data)):

        a = pred_original.data[i][0]

        b = pred_cargado.data[i][0]

        diferencia = abs(a - b)

        if diferencia > 0.0001:

            iguales = False

    if iguales:

        print(
            "✅ EL MODELO FUE "
            "RESTAURADO PERFECTAMENTE"
        )

    else:

        print(
            "❌ ERROR EN LA RESTAURACION"
        )


# =====================================
# MAIN
# =====================================
if __name__ == "__main__":

    test_guardado_vagml()