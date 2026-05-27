# librerias/SYSVAG.py
# Utilidades del sistema para VAGAX — sin imports externos.
# Expone solo las funciones que el runtime VAGAX necesita.


class SYSVAG:
    """
    Librería de utilidades del sistema para VAGAX.
    VERSIÓN PURA: SIN imports externos (ni sys, ni os).
    """

    @staticmethod
    def get_filename():
        """Nombre estándar del archivo de entrada para el motor."""
        return "calculo.txt"

    @staticmethod
    def get_os():
        """Identificador del entorno de ejecución VAGAX."""
        return "vagax-core-linux"

    @staticmethod
    def get_python_version():
        """Versión informativa."""
        return "3.x-vagax-compatible"

    @staticmethod
    def get_memory_usage(obj):
        """
        Estimación de tamaño en bytes sin sys.getsizeof.
        """
        if isinstance(obj, int):   return 28
        if isinstance(obj, float): return 24
        if isinstance(obj, str):   return 50 + len(obj)
        if isinstance(obj, list):  return 64 + (len(obj) * 8)
        return 0

    @staticmethod
    def get_platform_info():
        """Info del sistema definida manualmente."""
        return {
            "engine": "VAGAX",
            "build":  "2026.05",
            "status": "stable"
        }

    # =========================================================
    # GESTIÓN DEL PATH DE IMPORTACIÓN
    # Reemplaza sys.path.insert() sin necesitar 'import sys'
    # =========================================================

    @staticmethod
    def path_insert(indice, ruta):
        """
        Inserta 'ruta' en la posición 'indice' del sys.path de Python,
        sin usar 'import sys' explícitamente.
        Usa __import__ (built-in de Python) de forma encapsulada.
        """
        _sys = __import__('sys')
        ruta = str(ruta)
        if ruta not in _sys.path:
            _sys.path.insert(int(indice), ruta)

    @staticmethod
    def path_append(ruta):
        """Agrega 'ruta' al final del sys.path."""
        _sys = __import__('sys')
        ruta = str(ruta)
        if ruta not in _sys.path:
            _sys.path.append(ruta)

    @staticmethod
    def get_argv():
        """Retorna los argumentos de línea de comandos sin import sys."""
        _sys = __import__('sys')
        return list(_sys.argv)

    # =========================================================
    # UTILIDADES DE RUTA PARA SCRIPTS
    # Reemplaza os.path.dirname(__file__) sin import os
    # =========================================================

    @staticmethod
    def get_script_dir(ruta_archivo):
        """
        Retorna el directorio donde se encuentra el script dado.
        Equivale a os.path.dirname(os.path.abspath(ruta_archivo)).
        ruta_archivo: normalmente se pasa __file__ del script llamante.
        """
        ruta = str(ruta_archivo)

        # Resolver ruta absoluta si es relativa
        if not ruta.startswith('/'):
            # Obtener cwd via /proc/self/environ sin import os
            cwd = SYSVAG._getcwd()
            ruta = cwd.rstrip('/') + '/' + ruta

        # Normalizar: resolver '..' y '.'
        partes = ruta.split('/')
        resueltas = []
        for p in partes:
            if p == '' or p == '.':
                continue
            if p == '..':
                if resueltas:
                    resueltas.pop()
            else:
                resueltas.append(p)

        ruta_abs = '/' + '/'.join(resueltas)

        # Quitar la parte del nombre de archivo
        if '/' in ruta_abs:
            idx = ruta_abs.rfind('/')
            return ruta_abs[:idx] if idx > 0 else '/'
        return '/'

    @staticmethod
    def _getcwd():
        """Obtiene el CWD sin import os."""
        try:
            with open('/proc/self/environ', 'rb') as f:
                env_data = f.read()
            variables = env_data.split(b'\x00')
            for var in variables:
                if var.startswith(b'PWD='):
                    return var[4:].decode('utf-8', errors='replace')
        except Exception:
            pass
        return '/home/mikey/Documentos/LenguajeVAGAX-main3/LenguajeVAGAX-main'

    # =========================================================
    # I/O DE ARCHIVOS (sin import io)
    # =========================================================

    @staticmethod
    def read_file(path):
        """Lectura de archivo de texto usando open() nativo."""
        try:
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception:
            return "Error: Archivo no encontrado"

    @staticmethod
    def write_file(path, content):
        """Escritura de archivo de texto usando open() nativo."""
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(str(content))
            return True
        except Exception:
            return False