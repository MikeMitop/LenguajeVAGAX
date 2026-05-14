class MLP:

    def __init__(self):

        self.layers = []

        self.name = "MultilayerPerceptron"

    def add(self, layer):

        self.layers.append(layer)

    def forward(self, x):

        out = x

        for layer in self.layers:

            out = layer.forward(out)

        return out

    def backward(self, grad):

        for layer in reversed(self.layers):

            if hasattr(layer, "backward"):

                grad = layer.backward(grad)

        return grad

    def parameters(self):

        params = []

        for layer in self.layers:

            if hasattr(layer, "parameters"):

                params.extend(
                    layer.parameters()
                )

        return params

    # =====================================
    # GUARDAR MODELO .VAGML
    # =====================================
    def guardar_vagml(
        self,
        nombre_archivo
    ):

        with open(
            nombre_archivo,
            "wb"
        ) as f:

            for layer in self.layers:

                # Solo capas Dense
                if hasattr(layer, 'W'):

                    f.write(
                        b"DENSE_LAYER\n"
                    )

                    # ==================
                    # GUARDAR PESOS W
                    # ==================
                    for fila in layer.W.data:

                        linea = (

                            "|".join(
                                str(w)
                                for w in fila
                            ) + "\n"

                        )

                        f.write(
                            linea.encode()
                        )

                    # ==================
                    # INICIO BIAS
                    # ==================
                    f.write(
                        b"BIAS_START\n"
                    )

                    # ==================
                    # GUARDAR BIAS
                    # ==================
                    if layer.B is not None:

                        for fila in layer.B.data:

                            linea = (

                                "|".join(
                                    str(b)
                                    for b in fila
                                ) + "\n"

                            )

                            f.write(
                                linea.encode()
                            )

                    # ==================
                    # FIN CAPA
                    # ==================
                    f.write(
                        b"LAYER_END\n"
                    )

        print(
            f"✅ Modelo guardado:"
            f" {nombre_archivo}"
        )

    # =====================================
    # CARGAR MODELO .VAGML
    # =====================================
    def cargar_vagml(
        self,
        nombre_archivo
    ):

        from librerias.VAGML.Tensor import Tensor

        with open(
            nombre_archivo,
            "rb"
        ) as f:

            lineas = f.readlines()

        capa_actual = 0

        en_bias = False

        w_temp = []

        b_temp = []

        for linea in lineas:

            l = linea.decode().strip()

            # ==================
            # NUEVA CAPA
            # ==================
            if l == "DENSE_LAYER":

                w_temp = []

                b_temp = []

                en_bias = False

            # ==================
            # INICIO BIAS
            # ==================
            elif l == "BIAS_START":

                en_bias = True

            # ==================
            # FIN CAPA
            # ==================
            elif l == "LAYER_END":

                while not hasattr(
                    self.layers[capa_actual],
                    'W'
                ):

                    capa_actual += 1

                layer = self.layers[capa_actual]

                # ==================
                # RESTAURAR W
                # ==================
                layer.W = Tensor(
                    w_temp
                )

                layer.params["W"] = (
                    layer.W
                )

                # ==================
                # RESTAURAR B
                # ==================
                if len(b_temp) > 0:

                    layer.B = Tensor(
                        b_temp
                    )

                    layer.params["B"] = (
                        layer.B
                    )

                capa_actual += 1

            # ==================
            # LEER MATRICES
            # ==================
            elif (

                l != "DENSE_LAYER"
                and l != "BIAS_START"
                and l != "LAYER_END"
                and l != ""

            ):

                partes = l.split("|")

                valores = []

                for x in partes:

                    valores.append(
                        float(x)
                    )

                if en_bias:

                    b_temp.append(
                        valores
                    )

                else:

                    w_temp.append(
                        valores
                    )

        print(
            f"🔌 Modelo cargado:"
            f" {nombre_archivo}"
        )

    def __repr__(self):

        res = f"{self.name}\n"

        res += "-" * 40 + "\n"

        for i, layer in enumerate(self.layers):

            res += f"[{i}] {layer}\n"

        return res