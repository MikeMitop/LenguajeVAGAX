# Informe Técnico: Implementación de Recursión en VAGAX

## 1. Descripción del Problema

El intérprete de VAGAX no soportaba llamadas recursivas a funciones definidas por el usuario. Al ejecutar una función como `factorial(5)`, que se llama a sí misma con `factorial(n - 1)`, se producían dos fallos críticos:

### 1.1 El `returnvag` no se propagaba desde bloques anidados

El código original detectaba el `returnvag` **solo** en el nivel superior del cuerpo de la función:

```python
for stmt in func["ctx"].block().statement():
    if stmt.returnStmt():
        result = self.visit(stmt.returnStmt().expr())
        break
    self.visit(stmt)
```

Esto significaba que un `returnvag` dentro de un `ifvag` (que es lo normal en un caso base recursivo) **nunca era detectado**, porque el `returnStmt` está dentro del bloque del `if`, no directamente en el cuerpo de la función.

### 1.2 No había aislamiento seguro de la pila de llamadas

Aunque el código guardaba las variables antiguas (`old_vars = self.variables`), **no usaba un bloque `finally`** para garantizar la restauración. Si ocurría una excepción durante la ejecución recursiva, las variables del llamador se perdían y la memoria local no se liberaba.

---

## 2. Solución Implementada

### 2.1 Excepción `ReturnSignal`

Se creó una excepción de control de flujo que transporta el valor de retorno a través de cualquier nivel de anidamiento:

```python
class ReturnSignal(Exception):
    """Señal de control de flujo para propagar returnvag."""
    def __init__(self, value):
        self.value = value
```

### 2.2 Método `visitReturnStmt`

Se agregó un método dedicado que evalúa la expresión de retorno y lanza `ReturnSignal`:

```python
def visitReturnStmt(self, ctx):
    value = self.visit(ctx.expr())
    raise ReturnSignal(value)
```

Cuando el intérprete visita un `returnvag x;`, la excepción sube automáticamente a través de:
- `visitBlock` → `visitIfStatement` → `visitFunctionCall`

Sin importar cuántos niveles de `ifvag`/`whilevag`/`forvag` haya.

### 2.3 Ejecución con `try/except/finally`

El `visitFunctionCall` fue modificado para capturar la señal y garantizar limpieza:

```python
result = None
try:
    for stmt in func["ctx"].block().statement():
        self.visit(stmt)
except ReturnSignal as r:
    result = r.value
finally:
    for v in local_vars.values():
        self.memory.free(v)
    self.variables = old_vars

return result
```

**El bloque `finally`** es el componente crítico: garantiza que, incluso en llamadas recursivas profundas, cada frame restaure correctamente el scope de su llamador y libere su memoria local.

---

## 3. Diagrama de Flujo de una Llamada Recursiva

```
factorial(3)
├── Guardar scope → old_vars_1
├── Crear frame local: n=3
├── Ejecutar cuerpo:
│   ├── ifvag(3 <= 1) → falso
│   ├── returnvag 3 * factorial(2)
│   │   ├── factorial(2)
│   │   │   ├── Guardar scope → old_vars_2
│   │   │   ├── Crear frame local: n=2
│   │   │   ├── Ejecutar cuerpo:
│   │   │   │   ├── ifvag(2 <= 1) → falso
│   │   │   │   ├── returnvag 2 * factorial(1)
│   │   │   │   │   ├── factorial(1)
│   │   │   │   │   │   ├── Guardar scope → old_vars_3
│   │   │   │   │   │   ├── Crear frame local: n=1
│   │   │   │   │   │   ├── ifvag(1 <= 1) → verdadero
│   │   │   │   │   │   ├── returnvag 1 → ReturnSignal(1)
│   │   │   │   │   │   └── finally: liberar n=1, restaurar old_vars_3
│   │   │   │   │   └── resultado = 1
│   │   │   │   ├── 2 * 1 = 2 → ReturnSignal(2)
│   │   │   └── finally: liberar n=2, restaurar old_vars_2
│   │   └── resultado = 2
│   ├── 3 * 2 = 6 → ReturnSignal(6)
└── finally: liberar n=3, restaurar old_vars_1
    resultado final = 6
```

---

## 4. Pruebas Realizadas

### 4.1 Archivo de test: `ejemplos/recursion.vagax`

| Función | Llamada | Resultado Esperado | Resultado Obtenido | Estado |
|---------|---------|--------------------|--------------------|--------|
| Factorial recursivo | `factorial(5)` | 120 | 120 | ✅ |
| Fibonacci recursivo | `fib(7)` | 13 | 13 | ✅ |
| Suma recursiva | `sumaRec(10)` | 55 | 55 | ✅ |
| Potencia recursiva | `potencia(2, 8)` | 256 | 256 | ✅ |

### 4.2 Regresión en ejemplos existentes

| Archivo | Resultado Esperado | Resultado Obtenido | Estado |
|---------|--------------------|--------------------|--------|
| `validacion.vagax` | "ok", 10 | "ok", 10 | ✅ |
| `fib.vagax` | 13 | 13 | ✅ |
| `suma.vagax` | 25 | 25 | ✅ |
| `nPrfimo.vagax` | True | True | ✅ |

---

## 5. Código VAGAX de Ejemplo

### Factorial Recursivo

```
functionvag factorial(n) {
    ifvag (n <= 1) {
        returnvag 1;
    } endvag
    returnvag n * factorial(n - 1);
} endvag

factorial(5);  // Imprime: 120
```

### Fibonacci Recursivo

```
functionvag fib(n) {
    ifvag (n <= 0) {
        returnvag 0;
    } endvag
    ifvag (n == 1) {
        returnvag 1;
    } endvag
    returnvag fib(n - 1) + fib(n - 2);
} endvag

fib(7);  // Imprime: 13
```

---

## 6. Conclusiones

La recursión en VAGAX fue habilitada mediante dos cambios fundamentales:

1. **`ReturnSignal`**: Una excepción de control de flujo que permite a `returnvag` propagarse desde cualquier profundidad de bloques anidados hasta el `visitFunctionCall` que la captura.

2. **`try/except/finally`**: Un patrón que garantiza aislamiento correcto de la pila de llamadas — cada invocación recursiva tiene su propio frame de variables y limpia su memoria al terminar, sin importar si la función retornó normalmente o con error.

Estos cambios son retrocompatibles: no afectan la ejecución de funciones no-recursivas ni de ningún otro constructo del lenguaje.
