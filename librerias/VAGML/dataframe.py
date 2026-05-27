from runtime.excepciones import VAGAXError
from librerias.ARCHIVOSVAG import ARCHIVOSVAG

class PruebaFrame:
    def __init__(self, columnas, datos):
        # columnas: lista de strings
        # datos: lista de diccionarios (registros)
        self._cols = columnas
        self._data = datos

    def columnas(self):
        # Retorna la lista de nombres de columnas
        return self._cols[:]

    def seleccionar(self, columnas):
        # Selecciona un subconjunto de columnas
        for c in columnas:
            if c not in self._cols:
                raise VAGAXError(f"La columna '{c}' no existe")
        
        datos_nuevos = []
        for fila in self._data:
            datos_nuevos.append({c: fila[c] for c in columnas})
        
        return PruebaFrame(columnas[:], datos_nuevos)

    def filtrar(self, funcion):
        # Filtra filas usando una función que retorna bool
        datos_nuevos = []
        for fila in self._data:
            try:
                if funcion(fila):
                    datos_nuevos.append(fila)
            except Exception:
                raise VAGAXError("Error al ejecutar la función en filtrar()")
        
        return PruebaFrame(self._cols[:], datos_nuevos)

    def reemplazar(self, col, viejo, nuevo):
        # Reemplaza valores en una columna
        if col not in self._cols:
            raise VAGAXError(f"La columna '{col}' no existe")
        
        for fila in self._data:
            if fila[col] == viejo:
                fila[col] = nuevo
        
        return self

    def llenar_na(self, col, valor):
        # Rellena valores None con un valor dado
        if col not in self._cols:
            raise VAGAXError(f"La columna '{col}' no existe")
        
        for fila in self._data:
            if fila[col] is None:
                fila[col] = valor
        
        return self

    def detectar_tipos(self):
        # Detecta si cada columna es numérica o categórica
        tipos = {}

        for col in self._cols:
            es_numerico = True

            for fila in self._data:
                v = fila[col]

                if v is None:
                    continue

                if not isinstance(v, (int, float)):
                    es_numerico = False
                    break

            tipos[col] = "numerico" if es_numerico else "categorico"

        return tipos

    def to_matriz(self, columnas):
        # Convierte columnas seleccionadas a matriz (lista de listas)
        for c in columnas:
            if c not in self._cols:
                raise VAGAXError(f"La columna '{c}' no existe")
        
        matriz = []
        for fila in self._data:
            matriz.append([fila[c] for c in columnas])
        
        return matriz

    def to_etiqueta(self, columna):
        # Extrae una columna como lista (para labels/etiquetas)
        if columna not in self._cols:
            raise VAGAXError(f"La columna '{columna}' no existe")
        
        return [fila[columna] for fila in self._data]

    def guardar_csv(self, ruta):
        # Guarda el DataFrame como CSV utilizando ARCHIVOSVAG
        try:
            # Preparamos la matriz incluyendo los encabezados en la posición 0
            matriz = [self._cols]
            
            # Escribir filas
            for fila in self._data:
                valores = []
                for c in self._cols:
                    v = fila[c]
                    if v is None:
                        valores.append("")
                    else:
                        valores.append(str(v))
                matriz.append(valores)

            # Usamos el wrapper nativo de la librería
            ARCHIVOSVAG.csv_write(ruta, matriz)
            return True
        except Exception as e:
            raise VAGAXError(f"No se pudo guardar CSV: {e}")

def leer_csv(ruta):
    # Lee un archivo CSV usando ARCHIVOSVAG y retorna un PruebaFrame
    try:
        matriz = ARCHIVOSVAG.csv_read(ruta)
    except Exception:
        raise VAGAXError(f"No se pudo leer el CSV en {ruta}")

    if not matriz or len(matriz) == 0:
        raise VAGAXError("CSV vacío")

    columnas = [c.strip() for c in matriz[0]]
    datos = []

    for fila_valores in matriz[1:]:
        # Omitir filas vacías
        if len(fila_valores) == 0 or all(v.strip() == "" for v in fila_valores):
            continue
        
        if len(fila_valores) != len(columnas):
            raise VAGAXError("Fila con número incorrecto de columnas")

        fila = {}
        for c, v in zip(columnas, fila_valores):
            v2 = v.strip()
            if v2 == "":
                fila[c] = None
            else:
                # intentar convertir a número
                try:
                    if "." in v2:
                        fila[c] = float(v2)
                    else:
                        fila[c] = int(v2)
                except:
                    fila[c] = v2
        
        datos.append(fila)

    return PruebaFrame(columnas, datos)

def div_entreno(X, y, porcentaje):
    # Divide datos en conjunto de entrenamiento y prueba
    if porcentaje <= 0 or porcentaje >= 1:
        raise VAGAXError("El porcentaje debe estar entre 0 y 1")

    n = len(X)
    corte = int(n * porcentaje)

    X_train = X[:corte]
    y_train = y[:corte]

    X_test = X[corte:]
    y_test = y[corte:]

    return X_train, y_train, X_test, y_test