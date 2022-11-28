import random
from article import Artículo

class Redactor:
    def __init__(self,nombre,ci):
        self.nombre = nombre
        self.ci = ci

    def escribir(self):
        print("Estoy escribiendo un artículo")
        articulo = Artículo(
            input("Título: "),
            input("Cuerpo: "),
            input("Fecha: "),
            input("Resumen: "),
            input("Imagenes: "),
            self.nombre
            )
        print("Terminé el artículo",articulo.titulo)
        return articulo

class JefeRedactor(Redactor):
    def __init__(self,nombre,ci,sección,grupo):
        super().__init__(nombre,ci,sección)
        self.grupo_de_redactor = grupo

    def supervisar(self):
        print("Todo está bien con los redactores")

    def decidir(self,artículo):
        if random.random() > 0.5:
            print("El artículo ",artículo," fue aprobado")

        else:
            print("El artículo",artículo,"no fue aprobado")
