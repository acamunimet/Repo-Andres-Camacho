comprar = input("Bienvenidos a mi tienda de zapatos. ¿Desea comprar algo? (S/s => Si) (N/n = No) \n")

while(True):
    if comprar.upper() == "S":
        print("Seguir")
        break

    elif comprar.upper() == "N":
        print("Hasta luego")
        break

    elif comprar != "s" or comprar != "n":
        print("Error en el ingreso de datos, por favor, ingrese de nuevo")