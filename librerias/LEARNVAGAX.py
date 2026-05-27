# librerias/LEARNVAGAX.py
# API de alto nivel para ML en VAGAX — CERO imports nativos
from librerias.MATHVAG import MATHVAG
from librerias.REGREVAG import REGREVAG
from librerias.CLASIFVAG import CLASIFVAG
from librerias.DATASETVAG import DATASETVAG
from librerias.VAGML.Tensor import Tensor
from librerias.VAGML.Layer import Dense
from librerias.VAGML.Activation import ReLU, Sigmoid, Softmax
from librerias.VAGML.MLP import MLP
from librerias.VAGML.Data import DataLoader
from librerias.VAGML.Losses import MSE, BCE, CrossEntropyLoss
from librerias.VAGML.Optimizers import SGD, Adam
from librerias.VAGML.Trainer import Trainer


class LEARNVAGAX:
    """API de alto nivel para machine learning en VAGAX"""

    @staticmethod
    def quick_train(X, y, hidden_sizes, epochs=500, lr=0.01,
                    activation="relu", loss_type="mse", optimizer_type="adam"):
        """
        Entrenamiento rápido de red neuronal.
        X, y: Tensores
        hidden_sizes: lista de enteros [16, 8]
        """
        if not isinstance(X, Tensor): X = Tensor(X)
        if not isinstance(y, Tensor): y = Tensor(y)

        input_dim = X.shape[1]
        output_dim = y.shape[1]

        model = MLP()
        prev_dim = input_dim
        for h in hidden_sizes:
            model.add(Dense(prev_dim, h))
            if activation == "relu":
                model.add(ReLU())
            elif activation == "sigmoid":
                model.add(Sigmoid())
            prev_dim = h

        # Capa de salida
        if loss_type == "cross_entropy":
            model.add(Dense(prev_dim, output_dim))
            model.add(Softmax())
            loss_fn = CrossEntropyLoss()
        elif loss_type == "bce":
            model.add(Dense(prev_dim, output_dim))
            model.add(Sigmoid())
            loss_fn = BCE()
        else:
            model.add(Dense(prev_dim, output_dim))
            loss_fn = MSE()

        if optimizer_type == "adam":
            opt = Adam(model.parameters(), lr=lr)
        else:
            opt = SGD(model.parameters(), lr=lr)

        loader = DataLoader(X, y, batch_size=X.shape[0], shuffle=True)
        trainer = Trainer()
        history = trainer.fit(model, loader, loss_fn, opt, epochs, log_every=epochs//10)

        return model, history

    @staticmethod
    def quick_classify_knn(X_train, y_train, X_test, k=3):
        """Clasificación rápida con KNN"""
        if isinstance(X_train, Tensor): X_train = X_train.to_list()
        if isinstance(y_train, Tensor): y_train = [row[0] for row in y_train.to_list()]
        if isinstance(X_test, Tensor): X_test = X_test.to_list()
        return CLASIFVAG.knn_predict(X_train, y_train, X_test, k)

    @staticmethod
    def quick_classify_tree(X_train, y_train, X_test, max_depth=5):
        """Clasificación rápida con árbol de decisión"""
        if isinstance(X_train, Tensor): X_train = X_train.to_list()
        if isinstance(y_train, Tensor): y_train = [row[0] for row in y_train.to_list()]
        if isinstance(X_test, Tensor): X_test = X_test.to_list()
        tree = CLASIFVAG.decision_tree_fit(X_train, y_train, max_depth)
        return CLASIFVAG.decision_tree_predict_batch(tree, X_test)

    @staticmethod
    def quick_regress(x, y, degree=1):
        """Regresión rápida (lineal o polinomial)"""
        if isinstance(x, Tensor): x = x.to_flat_list()
        if isinstance(y, Tensor): y = y.to_flat_list()
        if degree == 1:
            return REGREVAG.lin_reg_fit(x, y)
        return REGREVAG.poly_reg_fit(x, y, degree)

    @staticmethod
    def load_csv(path, target_col=-1):
        """Carga CSV y separa en X, y como Tensores"""
        tensor = DATASETVAG.csv_to_tensor(path)
        X, y = DATASETVAG.split_xy(tensor, target_col)
        return X, y

    @staticmethod
    def prepare_data(X, y, normalize=True, split_ratio=0.8):
        """Pipeline completo: normalizar + dividir"""
        if normalize:
            X = DATASETVAG.normalize(X)
        X_train, y_train, X_test, y_test = DATASETVAG.train_test_split(X, y, split_ratio)
        return X_train, y_train, X_test, y_test

    @staticmethod
    def run_xor(epochs, lr):
        """XOR completo. Retorna [loss_final, pred00, pred01, pred10, pred11]"""
        Tensor.set_seed(42)
        X = Tensor([[0,0],[0,1],[1,0],[1,1]])
        y = Tensor([[0],[1],[1],[0]])
        model = MLP()
        model.add(Dense(2, 16))
        model.add(ReLU())
        model.add(Dense(16, 1))
        model.add(Sigmoid())
        opt = SGD(model.parameters(), lr=lr)
        crit = MSE()
        loader = DataLoader(X, y, batch_size=4, shuffle=False)
        fl = 0
        for ep in range(epochs):
            tl = 0
            for bx, by in loader:
                p = model.forward(bx)
                l = crit.forward(p, by)
                tl += l.item()
                g = crit.backward(p, by)
                model.backward(g)
                opt.step()
                opt.zero_grad()
            fl = tl
            if ep % (epochs // 5) == 0:
                print("  Epoch " + str(ep) + ": Loss = " + str(round(tl, 6)))
        fp = model.forward(X)
        return [fl, fp.data[0][0], fp.data[1][0], fp.data[2][0], fp.data[3][0]]

    @staticmethod
    def run_classify_nn(X_data, y_data, epochs, lr):
        """
        Entrena clasificador binario MLP. Retorna lista de predicciones.
        Acepta Tensores o listas de listas como entrada.
        La arquitectura se adapta al número de features de entrada.
        """
        Tensor.set_seed(42)

        # ── Normalizar entradas (Tensor o lista de listas) ──────────────
        if isinstance(X_data, Tensor):
            X = X_data
        else:
            X = Tensor(X_data)

        if isinstance(y_data, Tensor):
            y = y_data
        else:
            y = Tensor(y_data)

        # ── Arquitectura adaptativa ──────────────────────────────────────
        n_features = X.shape[1]

        # Para muchos features usamos capas más grandes
        if n_features <= 10:
            h1, h2 = 16, 0
        elif n_features <= 50:
            h1, h2 = 32, 0
        elif n_features <= 200:
            h1, h2 = 64, 32
        else:
            # 400+ features (imágenes aplanadas)
            h1, h2 = 64, 32

        model = MLP()
        model.add(Dense(n_features, h1))
        model.add(ReLU())

        if h2 > 0:
            model.add(Dense(h1, h2))
            model.add(ReLU())
            model.add(Dense(h2, 1))
        else:
            model.add(Dense(h1, 1))

        model.add(Sigmoid())

        # ── Optimizer y loss ──────────────────────────────────────────────
        if lr > 0:
            opt = Adam(model.parameters(), lr=lr)
        else:
            opt = SGD(model.parameters(), lr=0.01)

        crit = BCE()

        # ── Tamaño de batch adaptativo ────────────────────────────────────
        n_samples = X.shape[0]
        batch_size = min(64, n_samples)

        loader = DataLoader(X, y, batch_size=batch_size, shuffle=True)

        # ── Entrenamiento ─────────────────────────────────────────────────
        if epochs <= 0:
            # Solo predicción sin entrenamiento
            fp = model.forward(X)
            res = []
            for i in range(fp.shape[0]):
                res.append(fp.data[i][0])
            return res

        log_every = max(1, epochs // 5)

        for ep in range(epochs):
            total_loss = 0.0
            for bx, by in loader:
                p = model.forward(bx)
                l = crit.forward(p, by)
                total_loss += l.item()
                g = crit.backward(p, by)
                model.backward(g)
                opt.step()
                opt.zero_grad()

            if ep % log_every == 0:
                pf = model.forward(X)
                # Calcular accuracy rápida
                correctos = 0
                for i in range(pf.shape[0]):
                    pred_bin = 1 if pf.data[i][0] >= 0.5 else 0
                    real_bin = 1 if y.data[i][0] >= 0.5 else 0
                    if pred_bin == real_bin:
                        correctos += 1
                acc = correctos / n_samples
                print("  Epoch " + str(ep) + "/" + str(epochs) +
                      " | Loss: " + str(round(total_loss, 6)) +
                      " | Acc: " + str(round(acc * 100, 2)) + "%")

        fp = model.forward(X)
        res = []
        for i in range(fp.shape[0]):
            res.append(fp.data[i][0])
        return res

    @staticmethod
    def run_loss_trace(epochs, lr):
        """XOR training retornando lista de losses por época."""
        Tensor.set_seed(42)
        X = Tensor([[0,0],[0,1],[1,0],[1,1]])
        y = Tensor([[0],[1],[1],[0]])
        model = MLP()
        model.add(Dense(2, 16))
        model.add(ReLU())
        model.add(Dense(16, 1))
        model.add(Sigmoid())
        opt = SGD(model.parameters(), lr=lr)
        crit = MSE()
        loader = DataLoader(X, y, batch_size=4, shuffle=False)
        losses = []
        for ep in range(epochs):
            tl = 0
            for bx, by in loader:
                p = model.forward(bx)
                l = crit.forward(p, by)
                tl += l.item()
                g = crit.backward(p, by)
                model.backward(g)
                opt.step()
                opt.zero_grad()
            losses.append(tl)
        return losses

    @staticmethod
    def run_classify_and_predict(X_train_data, y_train_data, X_test_data, y_test_data, epochs, lr):
        """
        Entrena con (X_train, y_train) y predice sobre X_test.
        Retorna [preds_test, acc_train, acc_test].
        Acepta Tensores o listas de listas.
        """
        Tensor.set_seed(42)

        # ── Convertir entradas ─────────────────────────────────────────
        X_train = X_train_data if isinstance(X_train_data, Tensor) else Tensor(X_train_data)
        y_train = y_train_data if isinstance(y_train_data, Tensor) else Tensor(y_train_data)
        X_test  = X_test_data  if isinstance(X_test_data,  Tensor) else Tensor(X_test_data)
        y_test  = y_test_data  if isinstance(y_test_data,  Tensor) else Tensor(y_test_data)

        # ── Arquitectura adaptativa ────────────────────────────────────
        n_features = X_train.shape[1]
        if n_features <= 10:
            h1, h2 = 16, 0
        elif n_features <= 50:
            h1, h2 = 32, 0
        else:
            h1, h2 = 64, 32

        model = MLP()
        model.add(Dense(n_features, h1))
        model.add(ReLU())
        if h2 > 0:
            model.add(Dense(h1, h2))
            model.add(ReLU())
            model.add(Dense(h2, 1))
        else:
            model.add(Dense(h1, 1))
        model.add(Sigmoid())

        # ── Optimizer y loss ───────────────────────────────────────────
        opt  = Adam(model.parameters(), lr=lr if lr > 0 else 0.001)
        crit = BCE()

        n_samples  = X_train.shape[0]
        batch_size = min(64, n_samples)
        loader = DataLoader(X_train, y_train, batch_size=batch_size, shuffle=True)

        log_every = max(1, epochs // 5)

        # ── Entrenamiento ──────────────────────────────────────────────
        for ep in range(epochs):
            total_loss = 0.0
            for bx, by in loader:
                p = model.forward(bx)
                l = crit.forward(p, by)
                total_loss += l.item()
                g = crit.backward(p, by)
                model.backward(g)
                opt.step()
                opt.zero_grad()

            if ep % log_every == 0:
                pf = model.forward(X_train)
                correctos = 0
                for i in range(pf.shape[0]):
                    pred_bin = 1 if pf.data[i][0] >= 0.5 else 0
                    real_bin = 1 if y_train.data[i][0] >= 0.5 else 0
                    if pred_bin == real_bin:
                        correctos += 1
                acc = correctos / n_samples
                print("  Epoch " + str(ep) + "/" + str(epochs) +
                      " | Loss: " + str(round(total_loss, 6)) +
                      " | Acc Train: " + str(round(acc * 100, 2)) + "%")

        # ── Predicción sobre train ─────────────────────────────────────
        fp_train = model.forward(X_train)
        correctos_train = 0
        for i in range(fp_train.shape[0]):
            pred_bin = 1 if fp_train.data[i][0] >= 0.5 else 0
            real_bin = 1 if y_train.data[i][0] >= 0.5 else 0
            if pred_bin == real_bin:
                correctos_train += 1
        acc_train = correctos_train / X_train.shape[0]

        # ── Predicción sobre test ──────────────────────────────────────
        model.eval_mode()
        fp_test = model.forward(X_test)
        preds_test = []
        correctos_test = 0
        n_test = X_test.shape[0]
        for i in range(n_test):
            prob = fp_test.data[i][0]
            preds_test.append(prob)
            pred_bin = 1 if prob >= 0.5 else 0
            real_bin = 1 if y_test.data[i][0] >= 0.5 else 0
            if pred_bin == real_bin:
                correctos_test += 1
        acc_test = correctos_test / n_test if n_test > 0 else 0

        print("\n  === RESULTADOS FINALES ===")
        print("  Accuracy Train: " + str(round(acc_train * 100, 2)) + "%")
        print("  Accuracy Test:  " + str(round(acc_test  * 100, 2)) + "%")

        # Retorna [preds_test_lista, acc_train, acc_test]
        return [preds_test, acc_train, acc_test]

