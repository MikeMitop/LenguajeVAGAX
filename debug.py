from antlr4 import InputStream, CommonTokenStream
from grammar.generated.VagaxLexer import VagaxLexer
from grammar.generated.VagaxParser import VagaxParser
from interpreter import VAGAXInterpreter
from librerias.archivos import leer_archivo

codigo = leer_archivo("ejemplos/memoria.vagax")
print("codigo:", codigo)
input_stream = InputStream(codigo)
lexer = VagaxLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = VagaxParser(stream)
tree = parser.program()
print("tree:", tree.toStringTree(recog=parser))

interpreter = VAGAXInterpreter()
print("visitando...")
interpreter.visit(tree)
print("fin visit")
