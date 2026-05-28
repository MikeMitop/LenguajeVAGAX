from antlr4 import InputStream, CommonTokenStream
from grammar.generated.VagaxLexer import VagaxLexer
from grammar.generated.VagaxParser import VagaxParser
from interpreter import VAGAXInterpreter
from librerias.ARCHIVOSVAG import ARCHIVOSVAG


def main():
    try:
        # ── Soporte para argumentos CLI ───────────────────────────────
        # Forma 1 (interactivo): python main.py
        # Forma 2 (directo):     python main.py regresionlineal.vagax datos.xlsx col_x col_y
        _sys = __import__('sys')
        argv = _sys.argv  # built-in __import__, no 'import sys'

        if len(argv) >= 2:
            # Argumento 1: nombre del script .vagax
            nombre_archivo = argv[1].strip()
            # Argumentos adicionales: parámetros para el script vagax
            script_args = argv[2:]
        else:
            # Modo interactivo: pedir nombre del script
            nombre_archivo = input("Ingrese el archivo .vagax: ").strip()
            script_args = []

        # Construir ruta al script
        if nombre_archivo.startswith("ejemplos/"):
            ruta = nombre_archivo
        else:
            ruta = f"ejemplos/{nombre_archivo}"

        codigo = ARCHIVOSVAG.file_read(ruta)

        input_stream = InputStream(codigo)
        lexer = VagaxLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = VagaxParser(stream)
        tree = parser.program()

        interpreter = VAGAXInterpreter()

        # Inyectar argumentos del script en el intérprete
        # Accesibles desde VAGAX con get_arg(indice) y num_args()
        interpreter.script_args = script_args

        interpreter.visit(tree)

    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
