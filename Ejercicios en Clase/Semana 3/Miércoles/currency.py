currency_dict = {"Euro" : "€", "Dollar": "$", "Yen": "¥"}
currency_input = input("Please enter a currency name eg: Euro, Dollar: ")

print(currency_dict.get(currency_input,"Currency not found"))