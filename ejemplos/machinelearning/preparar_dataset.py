"""
preparar_dataset.py
===================
Wrapper Python mínimo que bootstrapea el path y delega todo el trabajo
a las librerías VAGAX nativas (IMAGENVAG, OSVAG, SYSVAG).

Sin 'import sys' ni 'import os' en el cuerpo principal.
Todas las operaciones de ruta y sistema usan SYSVAG y OSVAG.

Ejecutar desde la raíz del proyecto:
  python ejemplos/machinelearning/preparar_dataset.py

NOTA: Este archivo existe como alternativa al script VAGAX
      machinelearning/preparar_dataset.vagax
      Ambos producen el mismo resultado.
"""

# ── Bootstrap del path (necesario para importar librerias/) ──────────
# __file__ y __import__ son built-ins de Python, no requieren imports.
_ruta_script = __file__.replace('\\', '/')

# Subir 2 niveles: .../ejemplos/machinelearning/preparar_dataset.py
# → nivel 1: .../ejemplos/machinelearning/
# → nivel 2: .../ejemplos/
# → nivel 3 (raíz): .../LenguajeVAGAX-main/
_partes = _ruta_script.split('/')
_raiz = '/'.join(_partes[:-3])   # quitar los 3 últimos segmentos
if not _raiz:
    _raiz = '.'
__import__('sys').path.insert(0, _raiz)
# ─────────────────────────────────────────────────────────────────────

# A partir de aquí, todo usa las librerías del proyecto VAGAX
from librerias.SYSVAG import SYSVAG
from librerias.OSVAG import OSVAG
from librerias.IMAGENVAG import IMAGENVAG

# ============================================================
# CONFIGURACIÓN DE RUTAS (usando OSVAG, no os.path)
# ============================================================
BASE_DIR = SYSVAG.get_script_dir(__file__)
ARCHIVE  = OSVAG.path_join(BASE_DIR, 'archive(1)')

TRAIN_MUFFIN    = OSVAG.path_join(ARCHIVE, 'train', 'muffin')
TRAIN_CHIHUAHUA = OSVAG.path_join(ARCHIVE, 'train', 'chihuahua')
TEST_MUFFIN     = OSVAG.path_join(ARCHIVE, 'test',  'muffin')
TEST_CHIHUAHUA  = OSVAG.path_join(ARCHIVE, 'test',  'chihuahua')

CSV_TRAIN = OSVAG.path_join(BASE_DIR, 'train_muffin_chihuahua.csv')
CSV_TEST  = OSVAG.path_join(BASE_DIR, 'test_muffin_chihuahua.csv')

# Dimensiones de imagen redimensionada (20x20 = 400 features)
TARGET_W = 20
TARGET_H = 20

# Límite por clase
MAX_POR_CLASE_TRAIN = 500
MAX_POR_CLASE_TEST  = 200

# ============================================================
# MAIN
# ============================================================
if __name__ == '__main__':
    print("=" * 60)
    print("  PREPARACION DATASET MUFFIN vs CHIHUAHUA")
    print("  IMAGENVAG + OSVAG + SYSVAG (sin sys/os directos)")
    print("=" * 60)

    print("\n[1/2] Generando CSV de entrenamiento...")
    print("      Clase 0 = muffin    -> " + TRAIN_MUFFIN)
    print("      Clase 1 = chihuahua -> " + TRAIN_CHIHUAHUA)
    print("      Tamano: " + str(TARGET_W) + "x" + str(TARGET_H) +
          " = " + str(TARGET_W * TARGET_H) + " features")
    print("      Max por clase: " + str(MAX_POR_CLASE_TRAIN))

    n_train = IMAGENVAG.directorio_a_csv(
        dir_clase0=TRAIN_MUFFIN,
        dir_clase1=TRAIN_CHIHUAHUA,
        ruta_csv=CSV_TRAIN,
        target_w=TARGET_W,
        target_h=TARGET_H,
        max_por_clase=MAX_POR_CLASE_TRAIN
    )

    print("\n[2/2] Generando CSV de prueba...")
    print("      Clase 0 = muffin    -> " + TEST_MUFFIN)
    print("      Clase 1 = chihuahua -> " + TEST_CHIHUAHUA)
    print("      Max por clase: " + str(MAX_POR_CLASE_TEST))

    n_test = IMAGENVAG.directorio_test_a_csv(
        dir_clase0=TEST_MUFFIN,
        dir_clase1=TEST_CHIHUAHUA,
        ruta_csv=CSV_TEST,
        target_w=TARGET_W,
        target_h=TARGET_H,
        max_por_clase=MAX_POR_CLASE_TEST
    )

    print("\n" + "=" * 60)
    print("  LISTO!")
    print("  Train: " + str(n_train) + " muestras -> " + CSV_TRAIN)
    print("  Test:  " + str(n_test) + "  muestras -> " + CSV_TEST)
    print("=" * 60)
    print("\nEjecuta el clasificador VAGAX:")
    print("  python main.py")
    print("  -> machinelearning/muffin_vs_chihuahua.vagax")
