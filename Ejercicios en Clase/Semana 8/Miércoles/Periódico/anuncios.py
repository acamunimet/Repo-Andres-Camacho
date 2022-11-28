from xmlrpc.client import boolean


class AnuncioComercial:
    def __init__(self,imagen,sección):
        self.imagen = imagen
        self.seccion = sección

class AnuncioClasificado:
    def __init__(self,precio,fecha_publicación,días,tipo):
        self.precio = precio
        self.fecha_de_publicación = fecha_publicación
        self.cantidad_de_días = días
        self.tipo = tipo

class AnuncioVehículo(AnuncioClasificado):
    def __init__(self, precio, fecha_publicación, días,marca,modelo,año):
        super().__init__(precio, fecha_publicación, días, "Vehículo")
        self.marca = marca
        self.modelo = modelo
        self.año = año

class AnuncioVivienda(AnuncioClasificado):
    def __init__(self, precio, fecha_publicación, días,m2,cuartos,baños,puestos,politicas):
        super().__init__(precio, fecha_publicación, días, "Vivienda")
        self.m2 = m2
        self.cuartos = cuartos
        self.baños = baños
        self.puestos = puestos
        self.acepta_politica = politicas