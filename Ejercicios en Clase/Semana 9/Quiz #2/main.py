from alcohol import Alcohol
from refresco import Refresco


def get_bebidas_alcohólicas():
    return [
        Alcohol("Linaje", "Santa Teresa", 40, "Ron", True),
        Alcohol("Black Label", "Johnnie Walker", 43, "Whisky", True),
        Alcohol("Solera Verde", "Polar", 6, "Cerveza", True)
    ]

def get_bebidas_azucaradas():
    return [
        Refresco("Maltín Polar", "Polar", 7, "Malta", True),
        Refresco("Pepsi", "Pepsico", 7, "Cola", True),
        Refresco("Chinoto", "The Coca-Cola Company", 4, "Limón", True)
    ]

def main():

        #Bienvenida
    print("******¡Bienvenido/a a La Bodeguita!******")

        #Respuesta Inválida
    wrong_answer = ('''Favor, indique un valor válido.
    
    ''')

    #Primer Paso
    while True:
        first_step = str(input('''
        ¿Qué desea?

        Ver la lista de bebidas - Inserte "1"
        Eliminar una bebida del inventario   - Inserte "2"

        Salir                  - Inserte "0"

        '''))

        if first_step == "1":
            tipo_bebida = str(input('''¿Qué tipo de bebida desea?
            
            Alcohólica      - Inserte "1"
            Refresco        - Inserte "2"
            
            Cancelar        - Inserte "0"'''))

            if tipo_bebida == "1":
                print(get_bebidas_alcohólicas)
            elif tipo_bebida == "2":
                print(get_bebidas_azucaradas)
            elif tipo_bebida == "0":
                pass
            else:
                print(wrong_answer)

        elif first_step == "2":
            print(eliminar_bebida)


        elif first_step == "0":
            break

        else:
            print(wrong_answer)

    #Despedida
    print("¡Muchas gracias por venir!")

main()