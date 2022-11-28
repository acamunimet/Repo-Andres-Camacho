from multiprocessing import current_process
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap


class Artículo:
    def __init__(self,titulo,cuerpo,fecha,resumen,imagenes,redactor):
        self.titulo = titulo
        self.cuerpo = cuerpo
        self.fecha_publicación = None
        self.fecha_creación = fecha
        self.resumen = resumen 
        self.imagenes = imagenes
        self.redactor = redactor