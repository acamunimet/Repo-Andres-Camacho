def exponential(base, exp):
    if exp == 0:
        return 1
    return base * exponential(base, exp-1)

def main():
    print(exponential(int(input("Please, enter the base: ")), (int(input("Please, enter the base: ")))))


main()