def main():
    wrong_answer = ("""Por favor, ingrese un valor válido.
    
    """)

    juegos = {
        "Shooter": [
            {
                "id": 1,
                "name": "Overwatch2",
                "price": 60  
            },
            {
                "id": 2,
                "name": "Valorant",
                "price": 0
            },
            {
                "id": 3,
                "name": "Pixel Gun 3D",
                "price": 10
            }
        ],
        "RPG": [
            {
                "id": 4,
                "name": "Pokemon",
                "price": 50  
            },
            {
                "id": 5,
                "name": "Final Fantasy Exvius",
                "price": 0
            }
        ],
        "Open World": [
            {
                "id": 6,
                "name": "Minecraft",
                "price": 60  
            },
            {
                "id": 7,
                "name": "Cyberpunk 2077",
                "price": 60
            },
            {
                "id": 8,
                "name": "GTA V",
                "price": 40
            }
        ],  
    }

    #Bienvenida
    print("******¡Bienvenido/a a la tienda online de Epic Saman y Metro-Steam!******")

    #Primer Paso
    while True:
        first_step = str(input('''
        ¿Qué desea?

        Ver la lista de juegos - Inserte "1"
        Registrar una compra   - Inserte "2"

        Salir                  - Inserte "0"

        '''))

        #Ver Inventario

        if first_step == "1":
            filter_type = str(input('''¿Desea ver la lista de videojuegos de un género en específico?
            
            Sí       - Inserte "1"
            No       - Inserte "2"

            Cancelar - Inserte "0"
            
            '''))

            if filter_type == "1":
                gender = str(input('''¿Qué género desea explorar?
                
                Shooter       - Inserte "1"
                RPG           - Inserte "2"
                Mundo Abierto - Inserte "3"

                Cancelar      - Inserte "0"
                
                '''))
                
                if gender == "1":
                    for 
                    print(juegos["Shooter"])
                elif gender == "2":
                    print(juegos["RPG"])
                elif gender == "3":
                    print(juegos["Open World"])


            elif filter_type == "2":
                for juego in juegos:
                    print("- " + (juego))

            elif filter_type == "0":
                pass

            else:
                print(wrong_answer)

        elif first_step == "2":

            #¡COMPRA!

            name = str(input("Por favor, indique su nombre: "))
            last_name = str(input("Por favor, ahora ingrese su apellido: "))
            id_number = list(input("Por favor, indique su número de cédula: "))

            client_data = {"Nombre: ":name, "Apellido: ":last_name, "C.I.: ":id_number}
            
        elif first_step == "0":
            break

        else:
            print(wrong_answer)

    #Bonus
    if id_number[-1,-2,-3] == 

    #Despedida
    despedida = ("De nada, ¡vuelva pronto!")
    print(despedida)
        
main()