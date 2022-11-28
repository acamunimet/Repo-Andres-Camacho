from Vehiculo import Vehicle

class Bicicleta(Vehicle):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidades):
        super().__init__(color, ruedas, tipo)
        self.velocidades  = velocidades