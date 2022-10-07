number = input("Por favor, introduzca un número: ")

if number.isnumeric():
    number = int(number)
    number = number+1
    for index in range(1,number):
        print("*"*index)


else:
    print("Input error")