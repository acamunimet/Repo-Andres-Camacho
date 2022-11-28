class Persona:
    def __init__(self, nombre, cédula):
        self.nombre = nombre
        self.cédula = cédula

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Cédula: {self.cédula}")
        print("")