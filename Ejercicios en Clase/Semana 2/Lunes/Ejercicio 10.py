print("*** Welcome to Bella Napoli pizzeria!***")
option = input("Please enter an option: \n1-Vegetarian\n2-Non-Vegetarian")
if option.isnumeric():
    option=int(option)
    if option == 1:
        ingredient = input("Please enter an ingredient: \n1")
    elif option == 2:
    else:
        print("Invalid option")
else:
    print("Error")