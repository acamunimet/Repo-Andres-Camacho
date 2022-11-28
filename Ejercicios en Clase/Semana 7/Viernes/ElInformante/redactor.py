from trabajador import Trabajador
from artículo import Articulo

class Redactor(Trabajador):
    def __init__(self, nombre, cédula, sección):
        Trabajador.__init__(self, nombre, cédula, sección)

    def escribirArtículo(self, titulo, resumen, cuerpo, imagenes, aprobación, fechaPub, fechaCreación):
        return Articulo(titulo, resumen, cuerpo, imagenes, aprobación, fechaPub, fechaCreación, self)