class Articulo:
    def __init__(self, titulo, resumen, cuerpo, imagenes, aprobación, fechaPub, fechaCreación, redactor):
        self.titulo = titulo
        self.resumen = resumen
        self.cuerpo = cuerpo
        self.imagenes = imagenes
        self.aprobación = aprobación
        self.fechaPub = fechaPub
        self.fechaCreación = fechaCreación
        self.redactor = redactor

    def mostrar(self):
        print(f"Titulo: {self.titulo}")
        print(f"Cuerpo: {self.cuerpo}")
        print(f"Imágenes: ")
        for imagen in self.imagenes:
            print(f"    {imagen}")

        print(f"fechaPub: {self.fechaPub}")
        print(f"fechaCreación: {self.fechaCreación}")
        