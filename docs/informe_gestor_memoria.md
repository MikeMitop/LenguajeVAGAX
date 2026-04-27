# Gestor de Memoria de VAGAX: Implementación y Funcionamiento

Recientemente se integró al intérprete del lenguaje VAGAX un sistema simulado de gestión de memoria virtual y recolección de basura. Este documento detalla qué fue lo que se hizo, cómo interactúan sus componentes y cómo funciona por debajo.

---

## 1. El Componente Central: `memory_manager.py`

Se creó un módulo con la clase `MemoryManager` para simular una RAM de tamaño fijo (por defecto, 4096 bloques). 

En lugar de delegar el manejo de variables únicamente al entorno nativo de Python, ahora el lenguaje cuenta con un "Heap" controlado (`self.memory`), donde cada variable se guarda usando una *dirección de memoria* ficticia (un entero autoincremental).

### Métodos Principales de `MemoryManager`
*   **`allocate(name, value)`**: Simula la reserva de memoria para una nueva variable. Si se excede el límite máximo (`self.size`), arroja un error "Out of memory". Retorna la dirección (address) donde se almacenó.
*   **`free(address)`**: Libera el espacio eliminando la variable del heap.
*   **`get(address)` / `set(address, value)`**: Métodos para acceder y modificar el valor almacenado en un bloque de memoria específico.
*   **`info()`**: Imprime el estado actual de la memoria (Total, Usada y Libre).
*   **`gc(variables)`**: Implementa un recolector de basura (*Garbage Collector*) básico. Revisa las direcciones activas (Mark) y elimina de la memoria cualquier dirección que haya quedado huérfana en el heap (Sweep).

---

## 2. Modificación de la Gramática (Frontend)

Para exponer el control de la memoria al programador, se modificaron los archivos de **ANTLR4** que dictan las reglas léxicas y sintácticas del lenguaje.

### Modificaciones en `VagaxLexer.g4` (Tokens)
Se añadieron nuevas palabras reservadas:
*   `allocvag`: Para reserva de memoria explícita.
*   `freevag`: Para liberación de memoria explícita.
*   `memvag`: Para solicitar el reporte de estado de memoria.

### Modificaciones en `VagaxParser.g4` (Reglas de Sintaxis)
Se definieron las estructuras gramaticales (nodos del AST) y se añadieron al bloque de sentencias (`statement`):
```antlr
allocStmt : ALLOCVAG ID ASSIGN expr ;         // allocvag x = 10;
freeStmt  : FREEVAG LPAREN ID RPAREN ;        // freevag(x);
memStmt   : MEMVAG LPAREN RPAREN ;            // memvag();
```

---

## 3. Integración en el Intérprete (Backend)

La mayor transformación ocurrió en `interpreter.py`, pasando de guardar valores en diccionarios de Python a utilizar los punteros generados por el `MemoryManager`.

### Instanciación del Heap
Al iniciar el intérprete, arranca una nueva memoria:
```python
self.memory = MemoryManager(4096)
```

### El nuevo paradigma de Variables (Punteros virtuales)
Antes, una asignación como `intvag x = 10;` guardaba directamente `self.variables["x"] = 10`. 
Ahora, opera como una tabla de símbolos y punteros:
1. El intérprete solicita memoria: `address = self.memory.allocate("x", 10)`
2. Guarda el puntero en su tabla: `self.variables["x"] = address`

Para leer una variable en expresiones matemáticas (`visitExpr`), primero recupera el puntero desde `self.variables` y luego extrae el valor real pidiéndolo a la memoria: `self.memory.get(address)`.

### Liberación Automática (Funciones)
Se mejoró la administración de memoria en los llamados a funciones (`visitFunctionCall`). Cuando una función recibe parámetros, el intérprete hace un `allocate` de variables locales temporales. Al terminar de ejecutarse el bloque de la función, el intérprete se encarga de recorrer todas esas variables locales temporales y llamar a `self.memory.free(v)` para limpiar el espacio que consumió la función de forma automática.

### Instrucciones Nativas en Tiempo de Ejecución
Se agregaron tres métodos que procesan las llamadas de los usuarios desde el archivo fuente `.vagax`:

*   **`visitAllocStmt(self, ctx)`**: Permite asignar una variable con la palabra `allocvag`, funcionando bajo el capó idéntico a una variable normal pero destacando semánticamente la asignación de memoria.
*   **`visitFreeStmt(self, ctx)`**: Al llamar a `freevag(x)`, el intérprete pide a la memoria borrar el bloque asociado a `x` y luego borra la referencia a `x` de la tabla de símbolos para evitar punteros huérfanos.
*   **`visitMemStmt(self, ctx)`**: Ejecuta el comando `self.memory.info()` interrumpiendo el flujo temporalmente para imprimir el uso en consola.

---

## 4. Resumen

Gracias a esta arquitectura, VAGAX ya no depende 100% de que Python limpie la RAM automáticamente por él, sino que provee una capa intermedia donde el propio intérprete rastrea y controla los bytes reservados, dando lugar a reportes dinámicos, a recolección de basura personalizada, y proporcionándole al usuario sentencias estilo `C` (`freevag`) para manipular el ciclo de vida de los datos de forma directa.
