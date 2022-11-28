class Bebida:
    def __init__(self, nombre, marca, disponible):
        self.nombre = nombre
        self.marca = marca
        self.disponible = bool(disponible)

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Marca: {self.marca}")
        print(f"Disponible: {self.disponible}")
        print("")