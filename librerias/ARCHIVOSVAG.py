# librerias/archivos.py

class ARCHIVOSVAG:
    
    @staticmethod
    def file_write(ruta, contenido):
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(str(contenido))
        return True

    @staticmethod
    def file_read(ruta):
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                return f.read()
        except:
            return ""

    @staticmethod
    def file_append(ruta, contenido):
        with open(ruta, 'a', encoding='utf-8') as f:
            f.write(str(contenido))
        return True

    @staticmethod
    def file_exists(ruta):
        try:
            with open(ruta, 'r') as f:
                return True
        except:
            return False

    @staticmethod
    def file_delete(ruta):
        import os
        if ARCHIVOSVAG.file_exists(ruta):
            os.remove(ruta)
            return True
        return False

    @staticmethod
    def file_lines(ruta):
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                return [line.strip() for line in f.readlines()]
        except:
            return []

    @staticmethod
    def file_write_lines(ruta, lista):
        with open(ruta, 'w', encoding='utf-8') as f:
            for linea in lista:
                f.write(str(linea) + "\n")
        return True

    @staticmethod
    def csv_read(ruta):
        lineas = ARCHIVOSVAG.file_lines(ruta)
        # Retorna una lista de listas separando por comas
        return [l.split(',') for l in lineas if l.strip()]

    @staticmethod
    def csv_write(ruta, matriz):
        lineas = [",".join(map(str, fila)) for fila in matriz]
        return ARCHIVOSVAG.file_write_lines(ruta, lineas)