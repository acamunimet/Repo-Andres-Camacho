class Vehicle:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

class Coche(Vehicle):
    def __init__(self, color, ruedas, velocidad, cc):
        Vehicle.__init__(color, ruedas)
        self.velocidad = velocidad
        self.cc = cc

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cc, carga):
        super().__init__(color, ruedas, velocidad, cc)
        self.carga = carga