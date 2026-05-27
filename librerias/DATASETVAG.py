# librerias/DATASETVAG.py
# Manejo de datasets para VAGAX — CERO imports nativos
from librerias.MATHVAG import MATHVAG
from librerias.ARCHIVOSVAG import ARCHIVOSVAG
from librerias.VAGML.Tensor import Tensor


class DATASETVAG:

    @staticmethod
    def csv_to_tensor(path, skip_header=True):
        """Carga CSV numérico como Tensor"""
        lines = ARCHIVOSVAG.file_lines(path)
        if skip_header and len(lines) > 0:
            lines = lines[1:]
        data = []
        for line in lines:
            if not line.strip(): continue
            parts = line.split(",")
            row = []
            for p in parts:
                p = p.strip()
                if "." in p:
                    row.append(float(p))
                else:
                    try:
                        row.append(float(p))
                    except:
                        row.append(0.0)
            data.append(row)
        return Tensor(data)

    @staticmethod
    def csv_to_lists(path, skip_header=True):
        """Carga CSV como lista de listas de strings"""
        lines = ARCHIVOSVAG.file_lines(path)
        if skip_header and len(lines) > 0:
            header = lines[0].split(",")
            lines = lines[1:]
        else:
            header = None
        data = []
        for line in lines:
            if not line.strip(): continue
            data.append(line.split(","))
        return data, header

    @staticmethod
    def csv_test_to_data(path):
        """
        Lee CSV de test con formato: filename, p0, p1, ..., pN, label
        Retorna [Tensor_X, Tensor_y, lista_filenames]
        Primera columna = filename (string), última = label (int).
        """
        lines = ARCHIVOSVAG.file_lines(path)
        if len(lines) == 0:
            return [Tensor([[]]), Tensor([[]]), []]

        # Saltar header
        lines = lines[1:]

        X_data = []
        y_data = []
        filenames = []

        for line in lines:
            if not line.strip():
                continue
            parts = line.split(",")
            if len(parts) < 3:
                continue

            # Columna 0 = filename
            fname = parts[0].strip()
            filenames.append(fname)

            # Columna 1 a N-1 = features
            row = []
            for p in parts[1:-1]:
                p = p.strip()
                try:
                    row.append(float(p))
                except:
                    row.append(0.0)
            X_data.append(row)

            # Última columna = label
            try:
                label = float(parts[-1].strip())
            except:
                label = 0.0
            y_data.append([label])

        return [Tensor(X_data), Tensor(y_data), filenames]

    @staticmethod
    def normalize(tensor):
        """Normalización min-max: (x - min) / (max - min) por columna"""
        filas, cols = tensor.shape
        result = []
        for _ in range(filas):
            result.append([0.0] * cols)
        for j in range(cols):
            min_v = tensor.data[0][j]
            max_v = tensor.data[0][j]
            for i in range(1, filas):
                if tensor.data[i][j] < min_v: min_v = tensor.data[i][j]
                if tensor.data[i][j] > max_v: max_v = tensor.data[i][j]
            rango = max_v - min_v
            if rango == 0: rango = 1
            for i in range(filas):
                result[i][j] = (tensor.data[i][j] - min_v) / rango
        return Tensor(result)

    @staticmethod
    def standardize(tensor):
        """Estandarización Z-score: (x - mean) / std por columna"""
        filas, cols = tensor.shape
        result = []
        for _ in range(filas):
            result.append([0.0] * cols)
        for j in range(cols):
            col_vals = []
            for i in range(filas):
                col_vals.append(tensor.data[i][j])
            m = MATHVAG.mean(col_vals)
            s = MATHVAG.std_dev(col_vals)
            if s == 0: s = 1
            for i in range(filas):
                result[i][j] = (tensor.data[i][j] - m) / s
        return Tensor(result)

    @staticmethod
    def train_test_split(X, y, ratio=0.8):
        """Divide X e y en train/test con la proporción dada"""
        n = X.shape[0]
        split = int(n * ratio)
        # Shuffle con Fisher-Yates
        indices = list(range(n))
        for i in range(n - 1, 0, -1):
            j = int(Tensor._rand() * (i + 1))
            indices[i], indices[j] = indices[j], indices[i]
        train_x = [X.data[indices[i]][:] for i in range(split)]
        train_y = [y.data[indices[i]][:] for i in range(split)]
        test_x = [X.data[indices[i]][:] for i in range(split, n)]
        test_y = [y.data[indices[i]][:] for i in range(split, n)]
        return Tensor(train_x), Tensor(train_y), Tensor(test_x), Tensor(test_y)

    @staticmethod
    def one_hot_encode(labels, num_classes):
        """Convierte lista de etiquetas enteras a one-hot Tensor"""
        result = []
        for l in labels:
            row = [0.0] * num_classes
            row[int(l)] = 1.0
            result.append(row)
        return Tensor(result)

    @staticmethod
    def shuffle_data(X, y):
        """Shuffle sincronizado de X e y"""
        n = X.shape[0]
        indices = list(range(n))
        for i in range(n - 1, 0, -1):
            j = int(Tensor._rand() * (i + 1))
            indices[i], indices[j] = indices[j], indices[i]
        new_x = [X.data[indices[i]][:] for i in range(n)]
        new_y = [y.data[indices[i]][:] for i in range(n)]
        return Tensor(new_x), Tensor(new_y)

    @staticmethod
    def describe(tensor):
        """Estadísticas descriptivas por columna"""
        filas, cols = tensor.shape
        print("\n" + "=" * 60)
        print("  DATASET DESCRIBE")
        print("=" * 60)
        print(f"  Shape: ({filas}, {cols})")
        print(f"  {'Col':<6} {'Mean':<12} {'Std':<12} {'Min':<12} {'Max':<12}")
        print("-" * 60)
        for j in range(cols):
            col_vals = []
            for i in range(filas):
                col_vals.append(tensor.data[i][j])
            m = MATHVAG.mean(col_vals)
            s = MATHVAG.std_dev(col_vals)
            mn = col_vals[0]
            mx = col_vals[0]
            for v in col_vals:
                if v < mn: mn = v
                if v > mx: mx = v
            print(f"  {j:<6} {m:<12.4f} {s:<12.4f} {mn:<12.4f} {mx:<12.4f}")
        print("=" * 60 + "\n")

    @staticmethod
    def head(tensor, n=5):
        """Muestra las primeras n filas"""
        filas = tensor.shape[0]
        limit = n if n < filas else filas
        print(f"\nHead ({limit} filas):")
        for i in range(limit):
            print(f"  {tensor.data[i]}")
        print()

    @staticmethod
    def split_xy(tensor, target_col=-1):
        """Separa tensor en X (features) e y (target)"""
        filas, cols = tensor.shape
        if target_col < 0:
            target_col = cols + target_col
        X_data = []
        y_data = []
        for i in range(filas):
            row = []
            for j in range(cols):
                if j == target_col:
                    y_data.append([tensor.data[i][j]])
                else:
                    row.append(tensor.data[i][j])
            X_data.append(row)
        return Tensor(X_data), Tensor(y_data)
