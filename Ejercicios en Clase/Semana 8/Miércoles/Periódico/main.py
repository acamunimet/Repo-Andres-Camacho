from redactor import Redactor,JefeRedactor
from section import Sección

def get_redactores_entretenimiento():
    return [
        Redactor("Pedro",1234),
        Redactor("Juan",1234),
        Redactor("Christian",1234),
        Redactor("Ana",1234),
        Redactor("Andrea",1234),
    ]

def get_redactores_deportes():
    return [
        Redactor("Pedro",1234),
        Redactor("Juan",1234),
        Redactor("Christian",1234),
        Redactor("Ana",1234),
        Redactor("Andrea",1234),
    ]

def get_redactores_farandula():
    return [
        Redactor("Pedro",1234),
        Redactor("Juan",1234),
        Redactor("Christian",1234),
        Redactor("Ana",1234),
        Redactor("Andrea",1234),
    ]

def procesar_articulos(seccion):
    articles_to_review = []
    for escritor in seccion.jefe_redactor.grupo_de_redactor:
        articulo = escritor.escribir_articulo()
        seccion.jefe_redactor.decidir

def main():

    jefe_entretenimiento = JefeRedactor("José Quevedo",12345, get_redactores_entretenimiento{})
    jefe_deportes = JefeRedactor("José Quevedo",12345, get_redactores_deportes{})
    jefe_farandula = JefeRedactor("José Quevedo",12345, get_redactores_farandula{})

    seccion_entretenimiento = Sección("Entretenimineto",jefe_entretenimiento)
    seccion_deportes = Sección("Entretenimineto",jefe_deportes)
    seccion_farandula = Sección("Entretenimineto",jefe_farandula)

    procesar_articulos(seccion_entretenimiento)
    procesar_articulos(seccion_deportes)
    procesar_articulos(seccion_farandula)

main()