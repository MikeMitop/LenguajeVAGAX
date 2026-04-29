class SYSVAG:
    """
    Librería de utilidades del sistema para VAGAX
    VERSIÓN PURA: SIN LIBRERÍAS EXTERNAS
    """

    @staticmethod
    def get_filename():
        # Como no podemos usar sys.argv, definimos el nombre estándar 
        # que el motor buscará siempre.
        return "calculo.txt"

    @staticmethod
    def get_os():
        # Devolvemos una cadena fija. En un lenguaje propio, 
        # tú defines el nombre del entorno.
        return "vagax-core-linux"

    @staticmethod
    def get_python_version():
        # Valor informativo manual
        return "3.x-vagax-compatible"

    @staticmethod
    def get_memory_usage(obj):
        """
        Lógica manual para estimar peso sin sys.getsizeof.
        Útil para tus reportes de Sistemas Operativos.
        """
        if isinstance(obj, int): return 28  # Peso promedio de un int en Python
        if isinstance(obj, float): return 24
        if isinstance(obj, str): return 50 + len(obj)
        if isinstance(obj, list): return 64 + (len(obj) * 8)
        return 0

    @staticmethod
    def get_platform_info():
        """Retorna info del sistema definida manualmente"""
        return {
            "engine": "VAGAX",
            "build": "2026.04",
            "status": "stable"
        }

    @staticmethod
    def read_file(path):
        """
        Usa la función built-in open() que no requiere import
        """
        try:
            with open(path, "r", encoding="utf-8") as file:
                return file.read()
        except:
            return "Error: Archivo no encontrado"

    @staticmethod
    def write_file(path, content):
        """
        Escritura nativa
        """
        try:
            with open(path, "w", encoding="utf-8") as file:
                file.write(str(content))
            return True
        except:
            return False