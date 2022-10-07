number = int(input("Please enter a number: "))
aux = number - 1
count = 0

while aux >= 1:
    if number % aux == 0:
        count += 1
        break
    aux -= 1

if count == 0:
    print(f"The number {number} is prime")
else: 
    print (f"The number {number} is not prime")
