from grammar.generated.VagaxParserVisitor import VagaxParserVisitor
from grammar.generated.VagaxParser import VagaxParser
from memory_manager import MemoryManager
from librerias.MATHVAG import MATHVAG
from librerias.grafvag import GRAFVAG
from librerias.ARCHIVOSVAG  import ARCHIVOSVAG
from librerias.MATRXVAG import MATRXVAG
from librerias.SYSVAG import SYSVAG


class ReturnSignal(Exception):
    """Señal de control de flujo para propagar returnvag a través de bloques anidados."""
    def __init__(self, value):
        self.value = value


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
            self.visit(stmt)  # ReturnSignal se propaga naturalmente

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
        
        # Matemáticas Básicas 
        if name == "sin": return MATHVAG.sin(args[0])
        if name == "cos": return MATHVAG.cos(args[0])
        if name == "sqrt": return MATHVAG.sqrt(args[0])
        if name == "pi_val": return MATHVAG.PI
        
        # Matemáticas Nuevas
        if name == "abs_val": return MATHVAG.abs_val(args[0])
        if name == "factorial": return MATHVAG.factorial(args[0])
        if name == "power": return MATHVAG.power(args[0], args[1])
        if name == "sqrt": return MATHVAG.sqrt(args[0])
        if name == "cbrt": return MATHVAG.cbrt(args[0])
        if name == "root": return MATHVAG.root(args[0], args[1])

        # Exponenciales y Logaritmos
        if name == "exp": return MATHVAG.exp(args[0])
        if name == "log": return MATHVAG.log(args[0])
        if name == "log10": return MATHVAG.log10(args[0])
        if name == "log2": return MATHVAG.log2(args[0])
        if name == "log_base": return MATHVAG.log_base(args[0], args[1])

        # Trigonometría Completa
        if name == "sin": return MATHVAG.sin(args[0])
        if name == "cos": return MATHVAG.cos(args[0])
        if name == "tan": return MATHVAG.tan(args[0])
        if name == "asin": return MATHVAG.asin(args[0])
        if name == "acos": return MATHVAG.acos(args[0])
        if name == "atan": return MATHVAG.atan(args[0])
        if name == "atan2": return MATHVAG.atan2(args[0], args[1])
        if name == "sinh": return MATHVAG.sinh(args[0])
        if name == "cosh": return MATHVAG.cosh(args[0])
        if name == "tanh": return MATHVAG.tanh(args[0])

        # Teoría de Números
        if name == "gcd": return MATHVAG.gcd(args[0], args[1])
        if name == "lcm": return MATHVAG.lcm(args[0], args[1])
        if name == "is_prime": return MATHVAG.is_prime(args[0])

        # Estadística y Vectores
        if name == "mean": return MATHVAG.mean(args[0])
        if name == "median": return MATHVAG.median(args[0])
        if name == "variance": return MATHVAG.variance(args[0])
        if name == "std_dev": return MATHVAG.standard_deviation(args[0])
        if name == "dot_product": return MATHVAG.dot_product(args[0], args[1])
        if name == "norm": return MATHVAG.norm(args[0])

        # Combinatoria
        if name == "combinations": return MATHVAG.combinations(args[0], args[1])
        if name == "permutations": return MATHVAG.permutations(args[0], args[1])

        # Redondeo, Conversión y Constantes
        if name == "floor": return MATHVAG.floor_val(args[0])
        if name == "ceil": return MATHVAG.ceil_val(args[0])
        if name == "round_val": return MATHVAG.round_val(args[0], args[1])
        if name == "degrees": return MATHVAG.degrees(args[0])
        if name == "radians": return MATHVAG.radians(args[0])
        if name == "pi_val": return MATHVAG.PI
        if name == "e_val": return MATHVAG.E

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


        if name == "mat_zeros": return MATRXVAG.mat_zeros(args[0], args[1])
        if name == "mat_ones": return MATRXVAG.mat_ones(args[0], args[1])
        if name == "mat_identity": return MATRXVAG.mat_identity(args[0])
        if name == "mat_set": return MATRXVAG.mat_set(args[0], args[1], args[2], args[3])
        if name == "mat_get": return MATRXVAG.mat_get(args[0], args[1], args[2])
        if name == "mat_row": return MATRXVAG.mat_row(args[0], args[1])
        if name == "mat_col": return MATRXVAG.mat_col(args[0], args[1])
        if name == "mat_shape": return MATRXVAG.mat_shape(args[0])
        if name == "mat_add": return MATRXVAG.mat_add(args[0], args[1])
        if name == "mat_sub": return MATRXVAG.mat_sub(args[0], args[1])
        if name == "mat_mul": return MATRXVAG.mat_mul(args[0], args[1])
        if name == "mat_scalar": return MATRXVAG.mat_scalar(args[0], args[1])
        if name == "mat_transpose": return MATRXVAG.mat_transpose(args[0])
        if name == "mat_det": return MATRXVAG.mat_det(args[0])
        if name == "mat_inverse": return MATRXVAG.mat_inverse(args[0])
        if name == "mat_trace": return MATRXVAG.mat_trace(args[0])
        if name == "mat_norm": return MATRXVAG.mat_norm(args[0])
        if name == "mat_dot": return MATRXVAG.mat_dot(args[0], args[1])

        # --- SECCIÓN SYSVAG (Utilidades del Sistema) ---
        if name == "get_filename": 
            return SYSVAG.get_filename()
            
        if name == "get_args": 
            return SYSVAG.get_args()
            
        if name == "get_os": 
            return SYSVAG.get_os()
            
        if name == "get_python_version": 
            return SYSVAG.get_python_version()
            
        if name == "get_memory_usage": 
            # Requiere un argumento (el objeto a medir)
            return SYSVAG.get_memory_usage(args[0])
            
        if name == "get_platform_info": 
            return SYSVAG.get_platform_info()
            
        if name == "get_current_directory": 
            return SYSVAG.get_current_directory()

        if name == "exit_program":
            return SYSVAG.exit_program()

        # 3. LÓGICA PARA FUNCIONES DEL USUARIO (Solo si no es una nativa)
        if name not in self.functions:
            raise Exception(f"Función no definida: {name}")

        func = self.functions[name]
        params = func["params"]

        if len(args) != len(params):
            raise Exception(f"La función {name} esperaba {len(params)} argumentos y recibió {len(args)}")

        # Crear frame local con parámetros (aislamiento de pila)
        local_vars = {}
        for p, a in zip(params, args):
            address = self.memory.allocate(p, a)
            local_vars[p] = address

        # Guardar scope del llamador y crear nuevo scope
        old_vars = self.variables
        self.variables = {**old_vars, **local_vars}

        result = None
        try:
            # Ejecutar el cuerpo de la función
            for stmt in func["ctx"].block().statement():
                self.visit(stmt)
        except ReturnSignal as r:
            # Capturar el valor de returnvag (propagado desde cualquier nivel)
            result = r.value
        finally:
            # SIEMPRE restaurar scope y liberar memoria local
            for v in local_vars.values():
                self.memory.free(v)
            self.variables = old_vars

        return result

    # -------- RETURN --------

    def visitReturnStmt(self, ctx):
        """Lanza ReturnSignal para propagar el valor de retorno."""
        value = self.visit(ctx.expr())
        raise ReturnSignal(value)

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
