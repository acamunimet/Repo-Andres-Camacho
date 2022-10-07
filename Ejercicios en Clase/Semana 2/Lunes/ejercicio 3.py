a = (input("Por favor ingrese un valor 'a': "))
b = (input("Por favor ingrese un valor 'b': "))
is_valid = True

if a.isnumeric():
    a= float(a)
else:
    is_valid = False

if b.isnumeric():
    b= float(b)
else:
    is_valid = False

if is_valid:
    if b == 0:
     print("Error")
    else:
      print(a / b)