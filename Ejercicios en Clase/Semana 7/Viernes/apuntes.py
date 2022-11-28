#Abstracción:

class Persona:
    def __init__(self, nombre, apellido, edad, cédula): #Primer método a llamar
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.cédula = cédula

    def mostrar(self):
        print("Nombre: {}".format(self.nombre))
        print("Apellido: {}".format(self.apellido))
        print("Edad: {}".format(self.edad))
        print("Cédula: {}".format(self.cédula))
        print("")

Andrés = Persona("Andrés","Camacho",22,27849723) 
# print(persona) #Imprime su posición en la memoria
Andrés.mostrar()

midoriya = Persona("Izuku","Midoriya",20,"Idk man")
midoriya.mostrar()