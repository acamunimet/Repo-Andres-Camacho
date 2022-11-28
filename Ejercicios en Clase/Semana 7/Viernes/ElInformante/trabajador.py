from persona import Persona

class Trabajador(Persona):
    def __init__(self, nombre, cédula, sección):
        Persona.__init__(self, nombre, cédula)
        self.sección = sección