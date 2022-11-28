from redactor import Redactor

def main():
    sergio = Redactor("Sergio",1234567, "Tecnología")
    sergio.mostrar()

    articuloSergio = sergio.escribirArtículo("Semana 8, me quiero matar", "Esto no es un meme", "Ayuda, por favor", [], True, "28/10/2022", "21/10/2022")
    articuloSergio.mostrar()
main()