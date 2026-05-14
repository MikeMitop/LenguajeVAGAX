from librerias.SYSVAG import SYSVAG

class Visualizer:
    @staticmethod
    def print_epoch(epoch, total_epochs, loss, accuracy=None):
        """Imprime el progreso del entrenamiento con estilo VAGAX"""
        bar_length = 20
        progress = int((epoch / total_epochs) * bar_length)
        bar = "█" * progress + "-" * (bar_length - progress)
        
        stat = f"Epoch {epoch}/{total_epochs} [{bar}] Loss: {loss:.6f}"
        if accuracy is not None:
            stat += f" | Acc: {accuracy:.2%}"
            
        print(stat)

    @staticmethod
    def summary(model):
        """Muestra la arquitectura y el peso en memoria"""
        print("\n" + "="*40)
        print("📊 VAGML MODEL SUMMARY")
        print("="*40)
        print(model)
        # Aquí podrías usar SYSVAG para calcular el peso total de los parámetros
        print("="*40 + "\n")