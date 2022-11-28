from bebida import Bebida


class Alcohol(Bebida):
    def __init__(self, nombre, marca, grado, tipo, disponible):
        Bebida.__init__(self, nombre, marca, disponible)
        self.grado = float(grado)
        self.tipo = tipo