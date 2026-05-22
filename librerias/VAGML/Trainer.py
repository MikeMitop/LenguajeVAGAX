# librerias/VAGML/Trainer.py
# Loop de entrenamiento encapsulado para VAGML — CERO imports nativos
from librerias.VAGML.Tensor import Tensor


class Trainer:
    """
    Encapsula el loop de entrenamiento completo.
    Soporta: logging, early stopping, historial de métricas.
    """

    def __init__(self):
        self.history = {
            "loss": [],
            "accuracy": []
        }
        self.best_loss = float('inf')
        self.patience_counter = 0

    # ==========================================
    # ACCURACY BINARIA
    # ==========================================
    @staticmethod
    def binary_accuracy(y_pred, y_true):
        correctos = 0
        total = y_true.shape[0]
        for i in range(total):
            pred = y_pred.data[i][0]
            real = y_true.data[i][0]
            pred_bin = 1 if pred >= 0.5 else 0
            if pred_bin == int(real):
                correctos += 1
        return correctos / total if total > 0 else 0

    # ==========================================
    # ACCURACY MULTICLASE
    # ==========================================
    @staticmethod
    def multiclass_accuracy(y_pred, y_true):
        correctos = 0
        total = y_pred.shape[0]
        for i in range(total):
            # Argmax de predicción
            pred_max = 0
            pred_val = y_pred.data[i][0]
            for j in range(1, y_pred.shape[1]):
                if y_pred.data[i][j] > pred_val:
                    pred_val = y_pred.data[i][j]
                    pred_max = j
            # Argmax de verdadero
            true_max = 0
            true_val = y_true.data[i][0]
            for j in range(1, y_true.shape[1]):
                if y_true.data[i][j] > true_val:
                    true_val = y_true.data[i][j]
                    true_max = j
            if pred_max == true_max:
                correctos += 1
        return correctos / total if total > 0 else 0

    # ==========================================
    # FIT (ENTRENAMIENTO)
    # ==========================================
    def fit(self, model, loader, loss_fn, optimizer, epochs,
            log_every=100, early_stopping=0, accuracy_fn=None):
        """
        model: MLP
        loader: DataLoader
        loss_fn: Loss (MSE, BCE, CrossEntropy)
        optimizer: Optimizer (SGD, Adam)
        epochs: int
        log_every: int - cada cuántas épocas imprimir
        early_stopping: int - épocas sin mejora antes de parar (0=desactivado)
        accuracy_fn: función(y_pred, y_true) -> float (opcional)
        """
        if accuracy_fn is None:
            accuracy_fn = Trainer.binary_accuracy

        self.history = {"loss": [], "accuracy": []}
        self.best_loss = float('inf')
        self.patience_counter = 0

        print("\n" + "=" * 40)
        print("  VAGML TRAINING ENGINE")
        print("=" * 40)
        print(f"  Epochs: {epochs}")
        print(f"  Optimizer: {optimizer}")
        print(f"  Loss: {loss_fn}")
        print("=" * 40 + "\n")

        for epoch in range(epochs):
            epoch_loss = 0
            batch_count = 0

            for batch_x, batch_y in loader:
                # Forward
                pred = model.forward(batch_x)

                # Loss
                loss = loss_fn.forward(pred, batch_y)
                epoch_loss += loss.item()
                batch_count += 1

                # Backward loss
                grad = loss_fn.backward(pred, batch_y)

                # Backward model
                model.backward(grad)

                # Update pesos
                optimizer.step()

                # Reset gradientes
                optimizer.zero_grad()

            avg_loss = epoch_loss / batch_count if batch_count > 0 else 0
            self.history["loss"].append(avg_loss)

            # Accuracy (sobre todo el dataset)
            # Usamos el loader X e y directamente
            full_pred = model.forward(loader.X)
            acc = accuracy_fn(full_pred, loader.y)
            self.history["accuracy"].append(acc)

            # Logging
            if epoch % log_every == 0 or epoch == epochs - 1:
                bar_length = 20
                progress = int((epoch / epochs) * bar_length)
                bar = "█" * progress + "-" * (bar_length - progress)
                print(
                    f"  Epoch {epoch}/{epochs} [{bar}] "
                    f"Loss: {avg_loss:.6f} | Acc: {acc:.2%}"
                )

            # Early stopping
            if early_stopping > 0:
                if avg_loss < self.best_loss:
                    self.best_loss = avg_loss
                    self.patience_counter = 0
                else:
                    self.patience_counter += 1
                    if self.patience_counter >= early_stopping:
                        print(f"\n  ⚠ Early stopping en epoch {epoch}")
                        break

        print("\n" + "=" * 40)
        print("  ENTRENAMIENTO COMPLETO")
        final_loss = self.history["loss"][-1] if self.history["loss"] else 0
        final_acc = self.history["accuracy"][-1] if self.history["accuracy"] else 0
        print(f"  Loss Final: {final_loss:.6f}")
        print(f"  Accuracy Final: {final_acc:.2%}")
        print("=" * 40 + "\n")

        return self.history

    # ==========================================
    # EVALUATE
    # ==========================================
    def evaluate(self, model, loader, loss_fn, accuracy_fn=None):
        """Evaluación sin entrenamiento"""
        if accuracy_fn is None:
            accuracy_fn = Trainer.binary_accuracy

        total_loss = 0
        batch_count = 0

        for batch_x, batch_y in loader:
            pred = model.forward(batch_x)
            loss = loss_fn.forward(pred, batch_y)
            total_loss += loss.item()
            batch_count += 1

        avg_loss = total_loss / batch_count if batch_count > 0 else 0
        full_pred = model.forward(loader.X)
        acc = accuracy_fn(full_pred, loader.y)

        print(f"  Eval Loss: {avg_loss:.6f} | Eval Acc: {acc:.2%}")
        return {"loss": avg_loss, "accuracy": acc}

    # ==========================================
    # PREDICT
    # ==========================================
    @staticmethod
    def predict(model, X, threshold=0.5):
        """Predicción con umbral para clasificación binaria"""
        pred = model.forward(X)
        result = []
        for i in range(pred.shape[0]):
            fila = []
            for j in range(pred.shape[1]):
                if pred.shape[1] == 1:
                    fila.append(1 if pred.data[i][j] >= threshold else 0)
                else:
                    fila.append(pred.data[i][j])
            result.append(fila)
        return Tensor(result)
