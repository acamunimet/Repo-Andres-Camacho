

def main():
    
    lista = [3,5,7,1,4,8,9,2,6]
    number = int(input("Por favor, introduzca un número"))
    if binary_search(number, lista):
        print("The number", number, "is present")
    else: 
        print ("The number", number, "isn't present")