"""
Pa' subir el beta a GitHub, parado en el explorador de archivos dentro de la carpeta "Repo-Andrés-Camacho"
1.- git add. 
2.- git commit -m "Mensajito"
3.- git push
"""

#Para transformar a número entero: int(input("180")) = 180
#Para transoformar número a string: str(input(180)) = "180"



#Strings

string = ("273")
print(string.upper()) = todo mayúsculas
print(string.lower()) = todo minúsculas
print(string.capitalize()) = primeras letras mayúsculas
    #Ver si es numérico
string.isnumeric() = True



#Listas

personas = ["Victor", "Paco", "Pepe"]
números = [4,6,3,8,2]
print(personas[0]) = "Víctor"
    #Para agregar
personas.append("Josefa") = ["Victor", "Paco", "Pepe", "Josefa"] #También funciona para agregar otras listas.
personas.append(2,"Josefa") = ["Victor", "Paco", "Josefa", "Pepe"] #Agrega el atributo en el índice indicado primero
personas.extend(["José","Manuel","Tomás"]) = ["Victor", "Paco", "Pepe","José","Manuel","Tomás"]
    #Para borrar
personas.pop(2) = ["Victor", "Paco"]
personas.remove("Victor") = ["Paco", "Pepe"]
personas.clear() = []
    #Cantidad de repeticiones
x = personas.count("Victor") = 1
index = personas.index("Victor") = 1
    #¿Está en la lista?
print("Paco" in personas) = True
    #Invertir
personas.reverse() = ["Pepe","Paco","Victor"]
    #Ordenar
números.sort() = [2,3,4,6,8]
números.sort(reverse=True) = [8,6,4,3,2]




#Bucle for

for persona in personas:
    print("-" + (persona)) =
    """
    - Víctor
    - Paco
    - Pepe
    """



#Bucle while

while condición != 79:
    respuesta = int(input("Respuesta equivocada, responda otra vez: "))
print("Respuesta correcta.")



#Tuplas

No se pueden alterar. Son inmutables
tupla = (1,2)



#Diccionarios

diccionario = {"key":"value", "Key2":"value2"}
print(diccionario["key"]) = value
    #Extraer un valor con get
diccionario.get("key") = "value"
    #Para agregar 
diccionario["key3"] = "value3"
    #Para modificar
diccionario["key2"] = "valueX"
    #Para borrar
del(diccionario["key2"])
    #Diccionario con listas
value = ["v1","v2","v3"]



#Condicionales

if tienes_llave == "si":
    forma = input("¿Qué forma tiene la llave?: ")
    color = input("¿De qué color es la llave?: ")
    if forma == "cuadrada" and color == "naranja"
        print("Puedes pasar por la puerta 1")
    elif forma == "redonda" and color == "amarilla"
        print("Puedes pasar por la puerta 2")
    else:
        print("Tienes la llave equivocada")
else:
    print("No puedes pasar")
