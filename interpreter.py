# interpreter.py
from grammar.generated.VagaxParserVisitor import VagaxParserVisitor
from grammar.generated.VagaxParser import VagaxParser
from memory_manager import MemoryManager
from librerias.MATHVAG import MATHVAG
from librerias.grafvag import GRAFVAG
from librerias.ARCHIVOSVAG import ARCHIVOSVAG
from librerias.REGREVAG import REGREVAG
from librerias.CLASIFVAG import CLASIFVAG
from librerias.DATASETVAG import DATASETVAG
from librerias.MATRXVAG import MATRXVAG
from librerias.LEARNVAGAX import LEARNVAGAX
from librerias.VAGML.Tensor import Tensor
from librerias.VAGML.dataframe import leer_csv, div_entreno
from librerias.IMAGENVAG import IMAGENVAG
from runtime.mostrar import builtin_mostrar


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

        # 2. BLOQUE DE FUNCIONES NATIVAS

        # =============================================
        # MATEMÁTICAS BÁSICAS (MATHVAG)
        # =============================================
        if name == "sin": return MATHVAG.sin(args[0])
        if name == "cos": return MATHVAG.cos(args[0])
        if name == "tan": return MATHVAG.tan(args[0])
        if name == "sqrt": return MATHVAG.sqrt(args[0])
        if name == "cbrt": return MATHVAG.cbrt(args[0])
        if name == "abs_val": return MATHVAG.abs_val(args[0])
        if name == "pi_val": return MATHVAG.PI
        if name == "e_val": return MATHVAG.E
        if name == "asin": return MATHVAG.asin(args[0])
        if name == "acos": return MATHVAG.acos(args[0])
        if name == "atan": return MATHVAG.atan(args[0])
        if name == "atan2": return MATHVAG.atan2(args[0], args[1])
        if name == "sinh": return MATHVAG.sinh(args[0])
        if name == "cosh": return MATHVAG.cosh(args[0])
        if name == "tanh": return MATHVAG.tanh(args[0])
        if name == "exp": return MATHVAG.exp(args[0])
        if name == "log": return MATHVAG.log(args[0])
        if name == "log10": return MATHVAG.log10(args[0])
        if name == "log2": return MATHVAG.log2(args[0])
        if name == "logb": return MATHVAG.logb(args[0], args[1])
        if name == "power": return MATHVAG.power(args[0], args[1])
        if name == "factorial": return MATHVAG.factorial(args[0])
        if name == "is_prime": return MATHVAG.is_prime(args[0])
        if name == "gcd": return MATHVAG.gcd(args[0], args[1])
        if name == "lcm": return MATHVAG.lcm(args[0], args[1])
        if name == "round_val": return MATHVAG.round_val(args[0], args[1])
        if name == "floor_val": return MATHVAG.floor_val(args[0])
        if name == "ceil_val": return MATHVAG.ceil_val(args[0])
        if name == "clamp": return MATHVAG.clamp(args[0], args[1], args[2])
        if name == "degrees": return MATHVAG.degrees(args[0])
        if name == "radians": return MATHVAG.radians(args[0])
        if name == "combinations": return MATHVAG.combinations(args[0], args[1])
        if name == "permutations_val": return MATHVAG.permutations(args[0], args[1])
        if name == "nroot": return MATHVAG.nroot(args[0], args[1])

        # =============================================
        # ESTADÍSTICA (MATHVAG)
        # =============================================
        if name == "mean": return MATHVAG.mean(args[0])
        if name == "median": return MATHVAG.median(args[0])
        if name == "variance": return MATHVAG.variance(args[0])
        if name == "std_dev": return MATHVAG.std_dev(args[0])
        if name == "covariance": return MATHVAG.covariance(args[0], args[1])
        if name == "correlation": return MATHVAG.correlation(args[0], args[1])
        if name == "percentile": return MATHVAG.percentile(args[0], args[1])
        if name == "iqr": return MATHVAG.iqr(args[0])

        # =============================================
        # VECTORES (MATHVAG)
        # =============================================
        if name == "dot_product": return MATHVAG.dot_product(args[0], args[1])
        if name == "norm": return MATHVAG.norm(args[0])
        if name == "cross_product": return MATHVAG.cross_product(args[0], args[1])
        if name == "normalize_vector": return MATHVAG.normalize_vector(args[0])

        # =============================================
        # ML MATH (MATHVAG)
        # =============================================
        if name == "sigmoid": return MATHVAG.sigmoid(args[0])
        if name == "softmax_list": return MATHVAG.softmax(args[0])
        if name == "entropy": return MATHVAG.entropy(args[0])
        if name == "kl_divergence": return MATHVAG.kl_divergence(args[0], args[1])
        if name == "linspace": return MATHVAG.linspace(args[0], args[1], int(args[2]))

        # =============================================
        # MATRICES (MATRXVAG)
        # =============================================
        if name == "mat_zeros": return MATRXVAG.mat_zeros(int(args[0]), int(args[1]))
        if name == "mat_ones": return MATRXVAG.mat_ones(int(args[0]), int(args[1]))
        if name == "mat_identity": return MATRXVAG.mat_identity(int(args[0]))
        if name == "mat_add": return MATRXVAG.mat_add(args[0], args[1])
        if name == "mat_sub": return MATRXVAG.mat_sub(args[0], args[1])
        if name == "mat_mul": return MATRXVAG.mat_mul(args[0], args[1])
        if name == "mat_scalar": return MATRXVAG.mat_scalar(args[0], args[1])
        if name == "mat_transpose": return MATRXVAG.mat_transpose(args[0])
        if name == "mat_det": return MATRXVAG.mat_det(args[0])
        if name == "mat_inverse": return MATRXVAG.mat_inverse(args[0])
        if name == "mat_solve": return MATRXVAG.mat_solve(args[0], args[1])
        if name == "mat_lu": return MATRXVAG.mat_lu(args[0])
        if name == "mat_rank": return MATRXVAG.mat_rank(args[0])
        if name == "mat_trace": return MATRXVAG.mat_trace(args[0])
        if name == "mat_norm": return MATRXVAG.mat_norm(args[0])
        if name == "mat_shape": return MATRXVAG.mat_shape(args[0])
        if name == "mat_get": return MATRXVAG.mat_get(args[0], int(args[1]), int(args[2]))
        if name == "mat_set": return MATRXVAG.mat_set(args[0], int(args[1]), int(args[2]), args[3])
        if name == "mat_flatten": return MATRXVAG.mat_flatten(args[0])
        if name == "mat_reshape": return MATRXVAG.mat_reshape(args[0], int(args[1]), int(args[2]))
        if name == "mat_hadamard": return MATRXVAG.mat_hadamard(args[0], args[1])
        if name == "mat_eigenvalues_2x2": return MATRXVAG.mat_eigenvalues_2x2(args[0])
        if name == "mat_eigenvalue_dominant": return MATRXVAG.mat_eigenvalue_dominant(args[0])

        # =============================================
        # ARCHIVOS Y CSV
        # =============================================
        if name == "file_write": return ARCHIVOSVAG.file_write(args[0], args[1])
        if name == "file_read": return ARCHIVOSVAG.file_read(args[0])
        if name == "file_append": return ARCHIVOSVAG.file_append(args[0], args[1])
        if name == "file_exists": return ARCHIVOSVAG.file_exists(args[0])
        if name == "file_delete": return ARCHIVOSVAG.file_delete(args[0])
        if name == "file_lines": return ARCHIVOSVAG.file_lines(args[0])
        if name == "file_write_lines": return ARCHIVOSVAG.file_write_lines(args[0], args[1])
        if name == "csv_read": return ARCHIVOSVAG.csv_read(args[0])
        if name == "csv_write": return ARCHIVOSVAG.csv_write(args[0], args[1])

        # =============================================
        # LISTAS Y TEXTO
        # =============================================
        if name == "len": return len(args[0])
        if name == "get": return args[0][args[1]]
        if name == "set": 
            args[0][args[1]] = args[2]
            return args[0]
        if name == "append": 
            args[0].append(args[1])
            return args[0]
        if name == "contains": return args[1] in args[0]
        if name == "str": return str(args[0])
        if name == "to_num":
            text = str(args[0]).strip()
            if "." in text:
                return float(text)
            return int(text)
        if name == "range": return list(range(int(args[0]), int(args[1])))

        # =============================================
        # GRÁFICAS (GRAFVAG)
        # =============================================
        if name == "plot_pastel": return GRAFVAG.plot_pastel(args[0], args[1])
        if name == "plot_barras": return GRAFVAG.plot_barras(args[0], args[1])
        if name == "plot_lineal": return GRAFVAG.plot_lineal(args[0], args[1])
        if name == "plot_scatter": return GRAFVAG.plot_scatter(args[0], args[1])
        if name == "plot_heatmap": return GRAFVAG.plot_heatmap(args[0])
        if name == "plot_histogram": return GRAFVAG.plot_histogram(args[0], int(args[1]) if len(args) > 1 else 10)
        if name == "plot_loss": return GRAFVAG.plot_loss(args[0])
        if name == "set_title": return GRAFVAG.set_title(args[0])
        if name == "set_xlabel": return GRAFVAG.set_xlabel(args[0])
        if name == "set_ylabel": return GRAFVAG.set_ylabel(args[0])

        # =============================================
        # REGRESIÓN (REGREVAG)
        # =============================================
        if name == "lin_reg_fit": return REGREVAG.lin_reg_fit(args[0], args[1])
        if name == "lin_reg_predict": return REGREVAG.lin_reg_predict(args[0], args[1])
        if name == "lin_reg_r2": return REGREVAG.lin_reg_r2(args[0], args[1], args[2])
        if name == "log_reg_fit": return REGREVAG.log_reg_fit(args[0], args[1], args[2], args[3])
        if name == "log_reg_predict": return REGREVAG.log_reg_predict(args[0], args[1])
        if name == "poly_reg_fit": return REGREVAG.poly_reg_fit(args[0], args[1], int(args[2]))
        if name == "poly_reg_predict": return REGREVAG.poly_reg_predict(args[0], args[1])
        if name == "multi_lin_reg_fit": return REGREVAG.multi_lin_reg_fit(args[0], args[1])
        if name == "multi_lin_reg_predict": return REGREVAG.multi_lin_reg_predict(args[0], args[1])

        # =============================================
        # CLASIFICACIÓN (CLASIFVAG)
        # =============================================
        if name == "knn_classify": return CLASIFVAG.knn_classify(args[0], args[1], args[2], int(args[3]))
        if name == "knn_predict": return CLASIFVAG.knn_predict(args[0], args[1], args[2], int(args[3]))
        if name == "knn_accuracy": return CLASIFVAG.knn_accuracy(args[0], args[1], args[2], args[3], int(args[4]))
        if name == "decision_tree_fit": return CLASIFVAG.decision_tree_fit(args[0], args[1], int(args[2]) if len(args) > 2 else 5)
        if name == "decision_tree_predict": return CLASIFVAG.decision_tree_predict(args[0], args[1])
        if name == "confusion_matrix": return CLASIFVAG.confusion_matrix(args[0], args[1])
        if name == "accuracy_score": return CLASIFVAG.accuracy(args[0], args[1])
        if name == "precision_score": return CLASIFVAG.precision(args[0], args[1])
        if name == "recall_score": return CLASIFVAG.recall(args[0], args[1])
        if name == "f1": return CLASIFVAG.f1_score(args[0], args[1])
        if name == "classification_report": return CLASIFVAG.classification_report(args[0], args[1])

        # =============================================
        # DATASETS (DATASETVAG)
        # =============================================
        if name == "csv_to_tensor": return DATASETVAG.csv_to_tensor(args[0])
        if name == "normalize_data": return DATASETVAG.normalize(args[0])
        if name == "standardize_data": return DATASETVAG.standardize(args[0])
        if name == "train_test_split": return DATASETVAG.train_test_split(args[0], args[1], args[2] if len(args) > 2 else 0.8)
        if name == "one_hot_encode": return DATASETVAG.one_hot_encode(args[0], int(args[1]))
        if name == "shuffle_data": return DATASETVAG.shuffle_data(args[0], args[1])
        if name == "describe_data": return DATASETVAG.describe(args[0])
        if name == "head_data": return DATASETVAG.head(args[0], int(args[1]) if len(args) > 1 else 5)
        if name == "split_xy": return DATASETVAG.split_xy(args[0], int(args[1]) if len(args) > 1 else -1)
        if name == "csv_test_to_data": return DATASETVAG.csv_test_to_data(args[0])

        # =============================================
        # TENSORES (Tensor)
        # =============================================
        if name == "tensor": return Tensor(args[0])
        if name == "tensor_zeros": return Tensor.zeros(int(args[0]), int(args[1]))
        if name == "tensor_ones": return Tensor.ones(int(args[0]), int(args[1]))
        if name == "tensor_random": return Tensor.random(int(args[0]), int(args[1]))
        if name == "tensor_identity": return Tensor.identity(int(args[0]))

        # =============================================
        # LEARNVAGAX (API de alto nivel)
        # =============================================
        if name == "quick_regress": return LEARNVAGAX.quick_regress(args[0], args[1], int(args[2]) if len(args) > 2 else 1)
        if name == "load_csv": return LEARNVAGAX.load_csv(args[0], int(args[1]) if len(args) > 1 else -1)

        # =============================================
        # VAGML WRAPPERS (Entrenamiento completo)
        # =============================================
        if name == "run_xor": return LEARNVAGAX.run_xor(int(args[0]), args[1])
        if name == "run_classify_nn": return LEARNVAGAX.run_classify_nn(args[0], args[1], int(args[2]), args[3])
        if name == "run_loss_trace": return LEARNVAGAX.run_loss_trace(int(args[0]), args[1])
        if name == "run_classify_and_predict": return LEARNVAGAX.run_classify_and_predict(args[0], args[1], args[2], args[3], int(args[4]), args[5])
        if name == "kmeans": return CLASIFVAG.kmeans(args[0], int(args[1]), int(args[2]) if len(args) > 2 else 100)

        # =============================================
        # PRUEBAFRAME (Dataframes)
        # =============================================
        if name == "mostrar": return builtin_mostrar(*args)
        if name == "leer_csv": return leer_csv(args[0])
        if name == "df_columnas": return args[0].columnas()
        if name == "df_seleccionar": return args[0].seleccionar(args[1])
        if name == "df_filtrar": return args[0].filtrar(args[1])
        if name == "df_reemplazar": return args[0].reemplazar(args[1], args[2], args[3])
        if name == "df_llenar_na": return args[0].llenar_na(args[1], args[2])
        if name == "df_detectar_tipos": return args[0].detectar_tipos()
        if name == "df_to_matriz": return args[0].to_matriz(args[1])
        if name == "df_to_etiqueta": return args[0].to_etiqueta(args[1])
        if name == "df_guardar_csv": return args[0].guardar_csv(args[1])
        if name == "div_entreno": return div_entreno(args[0], args[1], args[2])

        # =============================================
        # IMAGENVAG (Procesamiento de imágenes)
        # =============================================
        if name == "imagen_leer_gris": return IMAGENVAG.leer_imagen_gris(args[0], int(args[1]) if len(args) > 1 else 16, int(args[2]) if len(args) > 2 else 16)
        if name == "imagen_dir_a_csv": return IMAGENVAG.directorio_a_csv(args[0], args[1], args[2], int(args[3]) if len(args) > 3 else 16, int(args[4]) if len(args) > 4 else 16, int(args[5]) if len(args) > 5 else None)
        if name == "imagen_test_a_csv": return IMAGENVAG.directorio_test_a_csv(args[0], args[1], args[2], int(args[3]) if len(args) > 3 else 16, int(args[4]) if len(args) > 4 else 16, int(args[5]) if len(args) > 5 else None)

        # =============================================
        # run_classify_nn_full (versión con logging detallado)
        # =============================================
        if name == "run_classify_nn_full": return LEARNVAGAX.run_classify_nn(args[0], args[1], int(args[2]), args[3])

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