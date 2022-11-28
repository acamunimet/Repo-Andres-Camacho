def exponential(base, exp):
    if exp == 0:
        return 1
    return base * exponential(base, exp-1)

def search_list(lista, letter, index):
    if lista[index] == letter:
        return letter
    else:
        if len(lista) -1 == index:
                if lista[index] == letter:
                    return letter
                else:
                    return None
        return search_list(lista, letter, index+1)

def invert_word(word, index):
    if index == 0:
        return word[index]
    return word[index] + invert_word(word,index-1)

def main():
    print("***** WELCOME TO RECURSION PROGRAM *****")
    option = int(input("Options: \n 1 - Exponential \n 2 - Search in list \n 3- Invert word \n "))
    if option == 1:
        print(exponential(int(input("Please, enter the base: ")), (int(input("Please, enter the base: ")))))
    elif option == 2:
        lista = ["A","B","C","D","E","F","G","H","I","J"]
        letter = input("Please enter a letter to search: ")
        print(search_list(lista,letter))
    elif option == 3:
        word = input("Please enter a word to invert: ")
        print(invert_word(word, len(word)-1))
main()