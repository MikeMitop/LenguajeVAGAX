# VAGAX — Lenguaje de programación

VAGAX es un lenguaje de programación pensado como un DSL (Lenguaje para un dominio específico) enfocado para correr desde operaciones aritméticas básicas, funciones, condicionales, bucles, expresiones, importación de librerías, carga de archivos, etc; hasta su objetivo principal: Deep Learning. Diseñado con ANTLR4 + Python y pensado en su visualización como PSeInt sin quitar la sencillez de Python.

---

## Tabla de Contenidos

1. [Descripción General](#descripcion-general)
2. [Arquitectura del Proyecto](#arquitectura-del-proyecto)
3. [Gramática y Sintaxis](#gramatica-y-sintaxis)
4. [Librerías Nativas](#librerias-nativas)
5. [Requisitos Cumplidos](#requisitos-cumplidos)
6. [Instalación y Ejecución](#instalacion-y-ejecucion)
7. [Ejemplos por Categoría](#ejemplos-por-categoria)
8. [Motor de Deep Learning (VAGML)](#motor-de-deep-learning-vagml)
9. [Filosofía Zero-Dependency](#filosofia-zero-dependency)

---

## Descripción General

**VAGAX** es un lenguaje de programación funcional de dominio específico construido sobre ANTLRv4 e interpretado en Python. Su propósito es proporcionar un entorno limpio y autosuficiente para:

- Aritmética y álgebra matricial
- Estadística descriptiva
- Regresión lineal y logística
- Clasificación (KNN, árboles de decisión, MLP)
- Agrupamiento (K-Means)
- Redes neuronales con backpropagation
- Clasificación de imágenes (muffin vs. chihuahua)
- Lectura de archivos `.xlsx`, `.csv` y `.txt`
- Gráficas de datos

El lenguaje expone una sintaxis propia con palabras clave `vag`-sufijadas (`ifvag`, `whilevag`, `functionvag`, `intvag`, etc.) que lo distinguen visualmente de cualquier otro lenguaje.

---

## Arquitectura del Proyecto

A continuación se detalla la estructura completa de carpetas y archivos del proyecto, explicando la función de cada componente dentro del ecosistema VAGAX:

```
LenguajeVAGAX-main/
│
├── main.py                     ← Punto de entrada principal. Maneja la ejecución en modo consola y procesa los argumentos CLI para cargar y ejecutar los scripts `.vagax`.
├── repl.py                     ← Implementa el Read-Eval-Print Loop (REPL), permitiendo ejecutar instrucciones VAGAX de forma interactiva línea por línea.
├── interpreter.py              ← El núcleo del lenguaje. Implementa el patrón Visitor recorriendo el AST generado por ANTLR y delegando la ejecución a las librerías nativas.
├── memory_manager.py           ← Gestor de memoria propio que simula la reserva y liberación de bloques (4096 bloques en total), permitiendo operaciones estilo C (`allocvag`, `freevag`).
│
├── grammar/                    ← Contiene las reglas sintácticas y léxicas del lenguaje.
│   ├── VagaxLexer.g4           ← Define los tokens del lenguaje (palabras clave, operadores, literales).
│   ├── VagaxParser.g4          ← Define las reglas gramaticalales (cómo se estructuran las sentencias, bloques, funciones, etc.).
│   └── generated/              ← Clases en Python generadas automáticamente por ANTLR4 a partir de los archivos `.g4`.
│       ├── VagaxLexer.py
│       ├── VagaxParser.py
│       └── VagaxParserVisitor.py
│
├── librerias/                  ← Colección de librerías nativas del lenguaje, creadas bajo la filosofía "Zero-Dependency" (sin usar librerías externas de Python).
│   ├── MATHVAG.py              ← Implementa operaciones matemáticas avanzadas, trigonometría y un generador de números pseudoaleatorios.
│   ├── MATRXVAG.py             ← Funciones para la creación y manipulación de matrices (suma, multiplicación, inversa, transpuesta).
│   ├── REGREVAG.py             ← Modelos de regresión (lineal, logística, polinomial, multivariable).
│   ├── CLASIFVAG.py            ← Algoritmos de clasificación y agrupamiento (KNN, K-Means, Árboles de decisión).
│   ├── DATASETVAG.py           ← Utilidades para cargar, limpiar, normalizar y transformar datasets (principalmente CSV).
│   ├── LEARNVAGAX.py           ← API de alto nivel para facilitar el entrenamiento y evaluación de modelos de Machine Learning.
│   ├── ARCHIVOSVAG.py          ← Operaciones de entrada/salida para leer y escribir archivos de texto y CSV.
│   ├── XLSXVAG.py              ← Parser personalizado capaz de leer archivos de Excel (.xlsx) desempaquetando el ZIP y leyendo el XML interno.
│   ├── IMAGENVAG.py            ← Lector y procesador de imágenes (JPEG/BMP) a nivel de píxel sin utilizar librerías como Pillow.
│   ├── STRUCTVAG.py            ← Implementación nativa para la lectura de datos binarios, emulando la funcionalidad de `struct` en Python.
│   ├── OSVAG.py                ← Provee funciones para interactuar con el sistema de archivos (crear directorios, listar archivos).
│   ├── SYSVAG.py               ← Controla configuraciones del sistema, rutas de ejecución y acceso a argumentos pasados por consola.
│   ├── grafvag.py              ← Herramienta para generar visualizaciones gráficas de los datos procesados en el lenguaje.
│   └── VAGML/                  ← El motor de Deep Learning del proyecto, creado desde cero.
│       ├── Tensor.py           ← Estructura fundamental para almacenar datos n-dimensionales, con soporte para operaciones vectorizadas y diferenciación automática (Autograd).
│       ├── Layer.py            ← Representa las capas de la red neuronal (por ejemplo, capas densas con pesos y sesgos).
│       ├── Activation.py       ← Funciones de activación para introducir no-linealidad (ReLU, Sigmoid, Tanh, Softmax).
│       ├── Losses.py           ← Funciones de pérdida para calcular el error del modelo (MSE, Cross-Entropy).
│       ├── Optimizers.py       ← Algoritmos de optimización para actualizar los pesos durante el entrenamiento (SGD, Adam).
│       ├── MLP.py              ← Definición de la estructura del Perceptrón Multicapa, orquestando el forward y backward pass.
│       ├── Data.py             ← Herramientas para agrupar y mezclar los datos en lotes (batches) durante el entrenamiento.
│       ├── ENTRENAMIENTO.py    ← Lógica principal que coordina los ciclos (epochs) de entrenamiento supervisado.
│       └── Trainer.py          ← Interfaz simplificada para configurar y lanzar procesos de entrenamiento y validación.
│
└── ejemplos/                   ← Directorio con múltiples scripts `.vagax` que demuestran las capacidades del lenguaje.
    ├── suma.vagax
    ├── regresion.vagax
    ├── regresionlineal.vagax   ← Regresión lineal genérica sobre cualquier archivo .xlsx interactivo.
    ├── test_xor_ML.vagax       ← Prueba clásica de propagación hacia atrás resolviendo la compuerta XOR.
    ├── test_clasificacion_ML.vagax
    ├── test_kmeans_ML.vagax
    ├── analisisestadistico.vagax
    ├── fib.vagax               ← Ejemplo clásico de recursión (Fibonacci).
    ├── bubblesort.vagax
    └── machinelearning/
        ├── muffin_vs_chihuahua.vagax  ← Proyecto completo de clasificación de imágenes usando el motor VAGML.
        └── preparar_dataset.vagax     ← Script que procesa un directorio de imágenes y las convierte a un formato tabular.
```

---

## Gramática y Sintaxis

La gramática está definida en dos archivos ANTLRv4:

### Tipos de datos

| Keyword VAGAX | Tipo         | Ejemplo                        |
|---------------|--------------|-------------------------------|
| `intvag`      | Entero       | `intvag x = 5;`               |
| `floatvag`    | Flotante     | `floatvag pi = 3.14159;`      |
| `stringvag`   | Cadena       | `stringvag s = "hola";`       |
| `boolvag`     | Booleano     | `boolvag b = sisas;`          |
| `listvag`     | Lista        | `listvag datos = range(0,0);` |
| `matrixvag`   | Matriz       | `matrixvag M;`                |
| `dataframevag`| DataFrame    | `dataframevag df;`            |

> Los literales booleanos son `sisas` (true) y `nokas` (false).

### Estructuras de control

```vagax
// Condicional
ifvag (x > 10) {
    "mayor";
} elsevag {
    "menor o igual";
} endvag

// Ciclo while
whilevag (i < 100) {
    i = i + 1;
} endvag

// Ciclo for
forvag (intvag i = 0; i < 10; i = i + 1) {
    i;
} endvag
```

### Funciones

```vagax
functionvag factorial(n) {
    ifvag (n <= 1) {
        returnvag 1;
    } endvag
    returnvag n * factorial(n - 1);
} endvag

factorial(10);
```

### Operadores

| Categoría      | Operadores                     |
|----------------|-------------------------------|
| Aritméticos    | `+`, `-`, `*`, `/`, `%`, `^`  |
| Comparación    | `==`, `!=`, `<`, `>`, `<=`, `>=` |
| Lógicos        | `&&`, `\|\|`, `!`             |
| Potencia       | `^` (ej: `2^8` = 256)         |

### Conversión entre tipos

VAGAX incluye funciones nativas para convertir valores entre los diferentes tipos de datos, lo que es esencial al procesar datos importados de archivos externos o cuando se necesita mostrar información:

- `to_num(valor)`: Convierte un string o cualquier valor a## Librerías Nativas

Todas implementadas desde cero en Python, sin dependencias externas.

### MATHVAG — Matemáticas completas

Esta librería centraliza todas las operaciones matemáticas que van más allá del álgebra básica soportada en la gramática. Su función en el proyecto es proveer el soporte trigonométrico, logarítmico, y de generación de números aleatorios necesarios para inicializar pesos en redes neuronales, calcular funciones de pérdida y realizar análisis estadístico sin depender de los módulos `math` o `random` nativos de Python.

```vagax
floatvag r = sqrt(144);       // Raíz cuadrada → 12.0
floatvag s = sin(pi_val());   // Seno de π
floatvag c = cos(0);          // Coseno → 1.0
floatvag l = log(2.718);      // Logaritmo natural
floatvag p = power(2, 10);    // Potencia → 1024
floatvag a = abs_val(-5);     // Valor absoluto → 5
floatvag m = mean(lista);     // Promedio
floatvag d = std_dev(lista);  // Desviación estándar
floatvag med = median(lista); // Mediana
```

Incluye además: `tan`, `asin`, `acos`, `atan`, `atan2`, `floor`, `ceil`, `round_val`, `min_val`, `max_val`, `factorial`, `gcd`, y el generador aleatorio `VAGRandom` (LCG, sin `random` de Python).

### MATRXVAG — Álgebra matricial

Esta librería está diseñada específicamente para manejar listas bidimensionales como matrices. Su función principal es facilitar la programación de modelos de aprendizaje automático y cálculos estadísticos multivariables, ofreciendo operaciones esenciales como el producto punto, el cálculo de la inversa y la obtención de determinantes, evitando por completo la dependencia de librerías externas especializadas en computación científica como `numpy`.

```vagax
listvag A = mat_create(3, 3, 0);
listvag B = mat_identity(3);
listvag C = mat_add(A, B);
listvag D = mat_mul(A, B);
listvag T = mat_transpose(A);
listvag I = mat_inverse(A);
floatvag d = mat_det(A);
mat_print(C);
```

### REGREVAG — Regresión

Se encarga de abstraer los algoritmos predictivos clásicos orientados a problemas de regresión. Su papel es fundamental para aquellos casos donde no se requiere la complejidad de una red neuronal completa, permitiendo ajustar y predecir valores continuos utilizando mínimos cuadrados para modelos lineales, o implementando un entrenamiento iterativo básico para regresiones logísticas, convirtiéndose en el puente entre el análisis exploratorio y el machine learning dentro de VAGAX.

```vagax
// Regresión lineal simple (OLS)
listvag modelo = lin_reg_fit(X, Y);
floatvag pred  = lin_reg_predict(modelo, 15.0);
floatvag r2    = lin_reg_r2(X, Y, modelo);

// Regresión logística
listvag modelo_log = log_reg_fit(X, Y, 0.1, 1000);
floatvag prob      = log_reg_predict(modelo_log, 5.0);

// Regresión polinomial
listvag coefs = poly_reg_fit(X, Y, 3);
floatvag yp   = poly_reg_predict(coefs, 2.5);

// Regresión multivariable
listvag beta = multi_lin_reg_fit(X_matrix, Y);
```

### CLASIFVAG — Clasificación y Agrupamiento

Actúa como el núcleo de Machine Learning tradicional, complementando a las redes neuronales. Implementa algoritmos clásicos como K-Nearest Neighbors (KNN), Árboles de Decisión y agrupamiento con K-Means. Su objetivo es brindar a los usuarios herramientas variadas de clasificación y segmentación de datos sin tener que programar los algoritmos desde cero, funcionando como el equivalente a los componentes básicos de `scikit-learn` en el entorno cerrado de VAGAX.

```vagax
// K-Nearest Neighbors
intvag clase = knn_classify(X_train, y_train, punto, 5);

// Árbol de decisión
listvag arbol = dt_fit(X_train, y_train, 5);
intvag pred   = dt_predict(arbol, nuevo_punto);

// K-Means (clustering)
listvag resultado = kmeans(X_datos, 3, 100);
```

### LEARNVAGAX — Red Neuronal MLP (API de alto nivel)

Esta librería funciona como una capa envolvente y simplificada que interactúa directamente con el motor interno de VAGML. Su propósito principal es ocultar la complejidad matemática de los Tensores, las capas y el backpropagation, permitiendo a los usuarios entrenar y evaluar Perceptrones Multicapa (MLP) mediante unas pocas líneas de código. Es la herramienta definitiva del lenguaje para que cualquier programa VAGAX alcance fácilmente su meta principal de Aprendizaje Profundo.

```vagax
// Clasificador binario (acepta Tensores o listas)
// Arquitectura adaptativa: Input→Dense(64)→ReLU→Dense(32)→ReLU→Dense(1)→Sigmoid
// Optimizador: Adam | Loss: BCE
listvag preds = run_classify_nn(X_train, y_train, 50, 0.001);

// Entrenamiento + predicción sobre test en un solo paso
listvag resultado = run_classify_and_predict(X_tr, y_tr, X_te, y_te, 30, 0.001);

// XOR con backpropagation
listvag res = run_xor(1000, 0.1);

// Curva de pérdida
listvag losses = run_loss_trace(200, 0.05);
```

### DATASETVAG — Datasets

Sirve como el eslabón entre los datos crudos y los algoritmos analíticos. Se encarga de transformar listas provenientes de archivos en estructuras de datos listas para su procesamiento matemático (como Tensores), brindando también funciones de normalización y separación de variables dependientes e independientes, fundamentales en cualquier pipeline de ciencia de datos serio.

```vagax
listvag tensor  = csv_to_tensor("datos.csv");
listvag split   = split_xy(tensor, -1);
listvag X       = get(split, 0);
listvag y       = get(split, 1);
listvag datos   = csv_test_to_data("test.csv");
normalize_data(tensor);
describe_data(tensor);
head_data(tensor, 5);
```

### XLSXVAG — Lector Excel

Implementa un mecanismo ingenioso para extraer información directamente desde archivos de Microsoft Excel (.xlsx), abriéndolos como archivos ZIP y buscando patrones de texto en sus documentos XML internos. Su rol es crítico para la adopción práctica del DSL, ya que elimina la necesidad de contar con librerías externas de terceros (como `pandas` o `openpyxl`) para ingestar conjuntos de datos comerciales estándar.

```vagax
// Carga automática (resuelve la ruta)
listvag tabla = xlsx_leer_auto("data.xlsx");

// Información del archivo
xlsx_resumen(tabla);
listvag cols = xlsx_headers(tabla);

// Extracción de columnas numéricas alineadas
listvag nombres = range(0,0);
append(nombres, "edad");
append(nombres, "ingreso_mensual");
listvag columnas = xlsx_columnas(tabla, nombres);
```

### IMAGENVAG — Procesamiento de Imágenes

Ofrece la funcionalidad necesaria para abordar problemas de visión por computadora dentro de VAGAX. Desempaqueta y decodifica imágenes en formatos crudos (como BMP) o complejos (JPEG) convirtiéndolas a vectores normalizados listos para ser consumidos por una red neuronal, logrando así que el entorno del lenguaje se mantenga estricto en su política "zero-dependency" al no hacer uso de `Pillow` ni `OpenCV`.

```vagax
// Leer imagen como vector de grises normalizado [0,1]
// (formato JPEG o BMP, sin Pillow, sin OpenCV)
listvag vector = imagen_leer_gris("foto.jpg", 20, 20);

// Convertir directorio de imágenes a CSV
imagen_dir_a_csv(dir_clase0, dir_clase1, "train.csv", 20, 20, 500);
imagen_test_a_csv(dir_clase0, dir_clase1, "test.csv",  20, 20, 200);
```

### ARCHIVOSVAG — Archivos

Maneja de manera unificada las operaciones de entrada y salida elementales del sistema para los scripts. Su función primordial es proporcionar acceso genérico a archivos de texto y CSV, facilitando la exportación de resultados numéricos calculados por modelos predictivos, asegurando que los programas escritos en VAGAX tengan persistencia más allá de la consola de ejecución.

```vagax
stringvag contenido = file_read("archivo.txt");
file_write("salida.txt", "Hola VAGAX");
listvag lineas = file_lines("datos.txt");
csv_write("resultado.csv", tabla);
listvag mat = csv_read("datos.csv");
```

### grafvag — Visualización

Constituye la capa de salida visual del análisis de datos. Toma las coordenadas y resultados de operaciones para renderizar gráficos de manera programática, brindándole al lenguaje la capacidad interactiva y visual indispensable para observar tendencias estadísticas y comprender las curvas de aprendizaje de los algoritmos descritos previamente.

```vagax
plotvag(x_datos, y_datos);
titlevag("Mi Gráfica");
xlabelvag("Eje X");
ylabelvag("Eje Y");
showvag();
```"foto.jpg", 20, 20);

// Convertir directorio de imágenes a CSV
imagen_dir_a_csv(dir_clase0, dir_clase1, "train.csv", 20, 20, 500);
imagen_test_a_csv(dir_clase0, dir_clase1, "test.csv",  20, 20, 200);
```

### ARCHIVOSVAG — Archivos

```vagax
stringvag contenido = file_read("archivo.txt");
file_write("salida.txt", "Hola VAGAX");
listvag lineas = file_lines("datos.txt");
csv_write("resultado.csv", tabla);
listvag mat = csv_read("datos.csv");
```

### grafvag — Visualización

```vagax
plotvag(x_datos, y_datos);
titlevag("Mi Gráfica");
xlabelvag("Eje X");
ylabelvag("Eje Y");
showvag();
```

---

## Requisitos Cumplidos

### ✅ Operaciones Aritméticas Completas

Implementadas en `MATHVAG.py` y directamente en la gramática.

```vagax
intvag r1 = 10 + 3 * 2 ^ 4;        // Precedencia correcta
floatvag r2 = sqrt(2) * cos(pi_val() / 4);
floatvag r3 = log(factorial(10));
```

Cubre: suma, resta, multiplicación, división, módulo, potencia, raíces, logaritmos, trigonometría completa (sin, cos, tan, asin, acos, atan), valor absoluto, redondeo, piso, techo, máximo, mínimo, factorial, MCD.

---

### ✅ Operaciones de Matrices

Implementadas en `MATRXVAG.py`:

```vagax
listvag A = mat_create(3, 3, 1);
listvag B = mat_identity(3);
listvag suma      = mat_add(A, B);
listvag resta     = mat_sub(A, B);
listvag producto  = mat_mul(A, B);
listvag transpuesta = mat_transpose(A);
listvag inversa   = mat_inverse(A);
floatvag det      = mat_det(A);
mat_print(suma);
```

---

### ✅ Condicionales y Ciclos

```vagax
// IF / ELSE
ifvag (x > 0 && x < 100) {
    "positivo menor a 100";
} elsevag {
    "fuera de rango";
} endvag

// WHILE
intvag i = 0;
whilevag (i < 10) {
    i;
    i = i + 1;
} endvag

// FOR
forvag (intvag j = 0; j < 5; j = j + 1) {
    j * j;
} endvag
```

---

### ✅ Gráficas de Datos

```vagax
listvag x = range(0, 0);
listvag y = range(0, 0);
append(x, 1);  append(y, 2);
append(x, 2);  append(y, 4);
append(x, 3);  append(y, 9);

plotvag(x, y);
titlevag("Cuadrados");
xlabelvag("n");
ylabelvag("n^2");
showvag();
```

---

### ✅ Manejo de Archivos

```vagax
// Lectura de texto
stringvag datos = file_read("ejemplos/casos.txt");

// Escritura
file_write("resultado.txt", "Análisis completado");

// CSV
listvag tabla = csv_read("datos.csv");
csv_write("salida.csv", tabla);

// Excel .xlsx (sin openpyxl)
listvag hoja = xlsx_leer_auto("mi_archivo.xlsx");
```

---

### ✅ Regresión Lineal y Logística

Ver `ejemplos/regresionlineal.vagax` — ejemplo interactivo genérico:

```vagax
// Carga cualquier .xlsx, muestra columnas, permite elegir X e Y
listvag tabla  = xlsx_leer_auto(ruta_xlsx);
listvag modelo = lin_reg_fit(X, Y);
floatvag r2    = lin_reg_r2(X, Y, modelo);
floatvag pred  = lin_reg_predict(modelo, x_nuevo);
```

```vagax
// Regresión logística para clasificación binaria
listvag modelo_log = log_reg_fit(X, Y, 0.1, 1000);
floatvag prob = log_reg_predict(modelo_log, 5.0);
```

---

### ✅ Clasificador — Perceptrón Multicapa (MLP)

El motor `VAGML` implementa backpropagation completo desde cero:

```vagax
// Clasificador binario con MLP
// Arquitectura adaptativa: Input → Dense(64) → ReLU → Dense(32) → ReLU → Sigmoid
listvag resultado = run_classify_and_predict(
    X_train, y_train,
    X_test,  y_test,
    30,       // epochs
    0.001     // learning rate (Adam)
);
```

Compuerta XOR (no linealmente separable — demuestra backpropagation):

```vagax
listvag res = run_xor(1000, 0.1);
floatvag loss = get(res, 0);
// Loss final < 0.05 → backpropagation funciona
```

---

### ✅ Agrupamiento, Clasificación y Predicción con Redes Neuronales

```vagax
// CLUSTERING — K-Means
listvag clusters = kmeans(X_datos, 3, 100);

// CLASIFICACIÓN — KNN
intvag clase = knn_classify(X_train, y_train, nuevo, 5);

// CLASIFICACIÓN — Árbol de decisión
listvag arbol = dt_fit(X_train, y_train, 5);
intvag pred   = dt_predict(arbol, nuevo);

// CLASIFICACIÓN DE IMÁGENES — Muffin vs Chihuahua (CNN aproximada con MLP)
// (ver ejemplos/machinelearning/muffin_vs_chihuahua.vagax)
listvag resultado = run_classify_and_predict(X_tr, y_tr, X_te, y_te, 30, 0.001);
```

---

## Instalación y Ejecución

### Requisitos

```bash
pip install antlr4-python3-runtime
```

> No se requieren otras dependencias. NumPy, pandas, TensorFlow, Keras, sklearn: **ninguno**.

### Ejecutar desde consola (modo interactivo)

```bash
cd LenguajeVAGAX-main
python main.py
# → Ingrese el archivo .vagax: regresionlineal.vagax
```

### Ejecutar con argumentos CLI

```bash
# Script con archivo y columnas
python main.py regresionlineal.vagax data.xlsx anios_esc ingreso_mensual

# Solo el script (pide lo demás interactivamente)
python main.py regresionlineal.vagax data.xlsx
```

### REPL interactivo

```bash
python repl.py
# Evalúa expresiones línea a línea
```

### Ejecutar el clasificador de imágenes

```bash
# Paso 1: Preparar dataset (solo la primera vez)
python main.py
# → machinelearning/preparar_dataset.vagax

# Paso 2: Entrenar y clasificar
python main.py
# → machinelearning/muffin_vs_chihuahua.vagax
# Genera: submission.csv con label=0 (muffin) / label=1 (chihuahua)
```

---

## Ejemplos por Categoría

| Archivo `.vagax`              | Categoría              | Descripción                                          |
|-------------------------------|------------------------|------------------------------------------------------|
| `suma.vagax`                  | Aritmética             | Suma básica                                          |
| `division.vagax`              | Aritmética             | División con manejo de casos                         |
| `modulo.vagax`                | Aritmética             | Operador módulo `%`                                  |
| `taylor_exp.vagax`            | Matemáticas            | Serie de Taylor para exponencial                     |
| `fib.vagax`                   | Recursión              | Fibonacci recursivo                                  |
| `euclides.vagax`              | Algoritmos             | GCD por algoritmo de Euclides                        |
| `bubblesort.vagax`            | Algoritmos             | Ordenamiento burbuja                                 |
| `nPrfimo.vagax`               | Algoritmos             | Números primos                                       |
| `prueba.vagax`                | Matrices               | Operaciones matriciales                              |
| `regresion.vagax`             | ML                     | Regresión lineal y logística con datos de ejemplo    |
| `regresionlineal.vagax`       | ML                     | Regresión lineal genérica sobre cualquier `.xlsx`    |
| `test_xor_ML.vagax`           | Deep Learning          | Backpropagation — compuerta XOR                      |
| `test_clasificacion_ML.vagax` | Deep Learning          | MLP clasificador binario                             |
| `test_kmeans_ML.vagax`        | ML                     | Clustering K-Means                                   |
| `test_loss_ML.vagax`          | Deep Learning          | Curva de pérdida por épocas                          |
| `test_regresion_ML.vagax`     | ML                     | Regresión completa con VAGML                         |
| `analisisestadistico.vagax`   | Estadística            | Análisis de todas las columnas numéricas de un xlsx  |
| `df.vagax`                    | DataFrames             | Operaciones con dataframe                            |
| `machinelearning/*.vagax`     | Computer Vision        | Clasificador Muffin vs Chihuahua (imágenes JPEG)     |

---

## Motor de Deep Learning (VAGML)

El módulo `librerias/VAGML/` es un motor de aprendizaje profundo **implementado completamente desde cero** en Python puro, sin NumPy ni TensorFlow.

### Componentes

| Módulo           | Descripción                                               |
|------------------|-----------------------------------------------------------|
| `Tensor.py`      | Tensor n-dimensional, operaciones matriciales, autograd   |
| `Layer.py`       | Capa `Dense` con pesos y bias aleatorios                  |
| `Activation.py`  | `ReLU`, `Sigmoid`, `Tanh`, `Softmax`, `LeakyReLU`         |
| `Losses.py`      | `MSE`, `BCE` (Binary Cross-Entropy), `CrossEntropy`       |
| `Optimizers.py`  | `SGD` (con momentum), `Adam`                              |
| `MLP.py`         | Perceptrón Multicapa — forward/backward pass              |
| `Data.py`        | `DataLoader` con mini-batches y shuffle                   |
| `ENTRENAMIENTO.py` | Loop de entrenamiento supervisado completo              |
| `Trainer.py`     | Trainer de alto nivel con validación                      |

### Arquitectura de ejemplo (Muffin vs Chihuahua)

```
Input(400 features)
    └─► Dense(64) → ReLU
            └─► Dense(32) → ReLU
                    └─► Dense(1) → Sigmoid
                            └─► Probabilidad [0,1]
```

- **Optimizador:** Adam (`lr=0.001`)
- **Loss:** Binary Cross-Entropy
- **Batch size:** 64
- **Dataset:** 1000 imágenes JPEG (20×20 px, escala de grises)

---

## Filosofía Zero-Dependency

VAGAX es completamente autocontenido. Todas las librerías estándar de Python han sido reimplementadas dentro del proyecto:

| Librería Python | Reemplazada por  | Implementación                                  |
|-----------------|------------------|-------------------------------------------------|
| `struct`        | `STRUCTVAG`      | Parser binario con aritmética de bits            |
| `os`            | `OSVAG`          | Rutas, listado de directorios, I/O de archivos  |
| `sys`           | `SYSVAG`         | Gestión de path, argumentos CLI, CWD            |
| `random`        | `VAGRandom`      | Generador LCG (Linear Congruential Generator)   |
| `openpyxl`      | `XLSXVAG`        | Parser ZIP+XML para archivos `.xlsx`            |
| `PIL/Pillow`    | `IMAGENVAG`      | Decodificador JPEG/BMP + nearest-neighbor resize|
| `numpy`         | `VAGML/Tensor`   | Tensor n-dimensional con operaciones matriciales|
| `tensorflow`    | `VAGML/MLP`      | Red neuronal con backpropagation                |
| `sklearn`       | `CLASIFVAG`      | KNN, Árbol de decisión, K-Means                 |
| `pandas`        | `DATASETVAG`     | Carga y preprocesamiento de CSV/tensores        |

> Los únicos `__import__` internos (encapsulados dentro de las librerías VAGAX) son `zipfile` para leer `.xlsx` y llamadas a nivel de motor para `listdir`. Ningún script `.vagax` del usuario puede importar librerías externas directamente.

---

## Patrón de Diseño Visitor

La implementación sigue estrictamente el patrón **Visitor** de ANTLRv4:

```
Código fuente (.vagax)
        │
    [ANTLRv4 Lexer]        VagaxLexer.g4
        │ tokens
    [ANTLRv4 Parser]       VagaxParser.g4
        │ AST (árbol de sintaxis abstracta)
    [VAGAXInterpreter]     interpreter.py
        │ extiende VagaxParserVisitor
        │ visitProgram → visitStatement → visitExpr → ...
        ▼
    Resultado en consola
```

Cada nodo del AST es visitado por un método `visit*` específico en `interpreter.py`, que delega la lógica a las librerías nativas cuando corresponde.

---

*VAGAX — Construido con ANTLRv4, Python y cero dependencias externas.*
