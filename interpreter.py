from grammar.generated.VagaxParserVisitor import VagaxParserVisitor
from grammar.generated.VagaxParser import VagaxParser
from memory_manager import MemoryManager
from librerias.MATHVAG import MATHVAG
from librerias.grafvag import GRAFVAG
from librerias.ARCHIVOSVAG  import ARCHIVOSVAG

class VAGAXInterpreter(VagaxParserVisitor):

    def __init__(self):

        self.variables = {}
        self.functions = {}

        # gestor de memoria
        self.memory = MemoryManager(4096)

    # -------- PROGRAMA --------

    def visitProgram(self, ctx):

        for stmt in ctx.statement():
            self.visit(stmt)

    # -------- STATEMENT --------

    def visitStatement(self, ctx):

        if ctx.expr():

            result = self.visit(ctx.expr())

            if result is not None:
                print(result)

            return result

        return self.visitChildren(ctx)

    # -------- BLOQUE --------

    def visitBlock(self, ctx):

        for stmt in ctx.statement():
            self.visit(stmt)

    # -------- DECLARACIÓN DE VARIABLES --------

    def visitVarDecl(self, ctx):

        name = ctx.ID().getText()

        if ctx.expr():
            value = self.visit(ctx.expr())
        else:
            value = None

        address = self.memory.allocate(name, value)

        self.variables[name] = address

    # -------- ASIGNACIÓN --------

    def visitAssignment(self, ctx):

        name = ctx.ID().getText()
        value = self.visit(ctx.expr())

        if name not in self.variables:

            address = self.memory.allocate(name, value)
            self.variables[name] = address

        else:

            address = self.variables[name]
            self.memory.set(address, value)

    # -------- ALLOC --------

    def visitAllocStmt(self, ctx):

        name = ctx.ID().getText()

        value = self.visit(ctx.expr())

        address = self.memory.allocate(name, value)

        self.variables[name] = address

    # -------- FREE --------

    def visitFreeStmt(self, ctx):

        name = ctx.ID().getText()

        if name not in self.variables:
            raise Exception(f"Variable no definida: {name}")

        address = self.variables[name]

        self.memory.free(address)

        del self.variables[name]

    # -------- MEMORY INFO --------

    def visitMemStmt(self, ctx):

        self.memory.info()

    # -------- IF --------

    def visitIfStatement(self, ctx):

        condition = self.visit(ctx.expr())

        if condition:
            self.visit(ctx.block(0))

        else:

            if ctx.ELSE():
                self.visit(ctx.block(1))

    # -------- WHILE --------

    def visitWhileStatement(self, ctx):

        while self.visit(ctx.expr()):
            self.visit(ctx.block())

    # -------- FOR --------

    def visitForStatement(self, ctx):

        self.visit(ctx.assignment(0))

        while self.visit(ctx.expr()):

            self.visit(ctx.block())

            self.visit(ctx.assignment(1))

    # -------- DECLARACIÓN DE FUNCIÓN --------

    def visitFunctionDecl(self, ctx):

        name = ctx.ID().getText()

        params = []

        if ctx.paramList():
            params = [p.getText() for p in ctx.paramList().ID()]

        self.functions[name] = {
            "params": params,
            "ctx": ctx
        }

    # -------- LLAMADA A FUNCIÓN --------

    def visitFunctionCall(self, ctx):
        name = ctx.ID().getText()

        # 1. EVALUAR ARGUMENTOS PRIMERO
        args = []
        if ctx.argList():
            args = [self.visit(e) for e in ctx.argList().expr()]

        # 2. BLOQUE DE FUNCIONES NATIVAS (Ordenado)
        
        # Matemáticas Básicas (Ya las tenías)
        if name == "sin": return MATHVAG.sin(args[0])
        if name == "cos": return MATHVAG.cos(args[0])
        if name == "sqrt": return MATHVAG.sqrt(args[0])
        if name == "pi_val": return MATHVAG.PI
        
        # Matemáticas Nuevas
        if name == "tan": return MATHVAG.tan(args[0])
        if name == "asin": return MATHVAG.asin(args[0])
        if name == "acos": return MATHVAG.acos(args[0])
        if name == "atan": return MATHVAG.atan(args[0])
        if name == "atan2": return MATHVAG.atan2(args[0], args[1])
        if name == "e_val": return MATHVAG.E
        if name == "factorial": return MATHVAG.factorial(args[0])
        if name == "is_prime": return MATHVAG.is_prime(args[0])
        if name == "round_val": return MATHVAG.round_val(args[0], args[1])

        # Archivos y CSV
        if name == "file_write": return ARCHIVOSVAG.file_write(args[0], args[1])
        if name == "file_read": return ARCHIVOSVAG.file_read(args[0])
        if name == "file_append": return ARCHIVOSVAG.file_append(args[0], args[1])
        if name == "file_exists": return ARCHIVOSVAG.file_exists(args[0])
        if name == "file_delete": return ARCHIVOSVAG.file_delete(args[0])
        if name == "file_lines": return ARCHIVOSVAG.file_lines(args[0])
        if name == "file_write_lines": return ARCHIVOSVAG.file_write_lines(args[0], args[1])
        if name == "csv_read": return ARCHIVOSVAG.csv_read(args[0])
        if name == "csv_write": return ARCHIVOSVAG.csv_write(args[0], args[1])

        # Listas y Texto
        if name == "len": return len(args[0])
        if name == "get": return args[0][args[1]]
        if name == "append": 
            args[0].append(args[1])
            return args[0]
        if name == "contains": return args[1] in args[0]
        if name == "str": return str(args[0])
        if name == "range": return list(range(int(args[0]), int(args[1])))

        # Gráficas (Deben estar aquí antes del error de "no definida")
        if name == "plot_pastel": return GRAFVAG.plot_pastel(args[0], args[1])
        if name == "plot_barras": return GRAFVAG.plot_barras(args[0], args[1])
        if name == "plot_lineal": return GRAFVAG.plot_lineal(args[0], args[1])

        # 3. LÓGICA PARA FUNCIONES DEL USUARIO (Solo si no es una nativa)
        if name not in self.functions:
            raise Exception(f"Función no definida: {name}")

        func = self.functions[name]
        params = func["params"]

        if len(args) != len(params):
            raise Exception(f"La función {name} esperaba {len(params)} argumentos y recibió {len(args)}")

        # Manejo de memoria local
        local_vars = {}
        for p, a in zip(params, args):
            address = self.memory.allocate(p, a)
            local_vars[p] = address

        old_vars = self.variables
        self.variables = {**old_vars, **local_vars}

        result = None
        for stmt in func["ctx"].block().statement():
            if stmt.returnStmt():
                result = self.visit(stmt.returnStmt().expr())
                break
            self.visit(stmt)

        for v in local_vars.values():
            self.memory.free(v)

        self.variables = old_vars
        return result

    # -------- EXPRESIONES --------

    def visitExpr(self, ctx):

        if ctx.literal():
            return self.visit(ctx.literal())

        if ctx.functionCall():
            return self.visit(ctx.functionCall())

        if ctx.ID():

            name = ctx.ID().getText()

            if name not in self.variables:
                raise Exception(f"Variable no definida: {name}")

            address = self.variables[name]

            return self.memory.get(address)

        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == "(":
            return self.visit(ctx.expr(0))

        if ctx.getChildCount() == 3:

            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.getChild(1).getText()

            if op == '+':
                return left + right

            if op == '-':
                return left - right

            if op == '*':
                return left * right

            if op == '/':
                return left / right

            if op == '%':
                return left % right

            if op == '^':
                return left ** right

            if op == '==':
                return left == right

            if op == '!=':
                return left != right

            if op == '<':
                return left < right

            if op == '>':
                return left > right

            if op == '<=':
                return left <= right

            if op == '>=':
                return left >= right

            if op == '&&':
                return left and right

            if op == '||':
                return left or right

        if ctx.getChildCount() == 2:

            val = self.visit(ctx.expr(0))
            return not val

    # -------- LITERALES --------

    def visitLiteral(self, ctx):

        if ctx.NUMBER():

            text = ctx.NUMBER().getText()

            if "." in text:
                return float(text)

            else:
                return int(text)

        if ctx.STRING():
            return ctx.STRING().getText().strip('"')

        if ctx.BOOL_LIT():

            val = ctx.BOOL_LIT().getText()

            if val == "sisas":
                return True
            else:
                return False
