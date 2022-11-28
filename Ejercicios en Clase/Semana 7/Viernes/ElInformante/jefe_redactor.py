from trabajador import Trabajador

class Jefe(Trabajador):
    def __init__(self, nombre, cédula, sección):
        Trabajador.__init__(self, nombre, cédula, sección)