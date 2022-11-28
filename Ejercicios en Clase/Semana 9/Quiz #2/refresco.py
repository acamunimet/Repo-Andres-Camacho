from bebida import Bebida


class Refresco(Bebida):
    def __init__(self, nombre, marca, azúcar, sabor, disponible):
        Bebida.__init__(self, nombre, marca, disponible)
        self.azúcar = float(azúcar)
        self.sabor = sabor