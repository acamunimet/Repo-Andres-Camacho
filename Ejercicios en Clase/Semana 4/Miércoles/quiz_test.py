def main():
    products = {
        "mobiles" : {


        }

        ]
    }
    print("***** Welcome *****")
    while True:
        option = int(input("\nPlease enter a valid option: \n1-Show Inventory\n2-Make a purchase\n3-Exit\n->"))
        available_types = {1: "mobiles", 2: "laptops"}
        if option == 1:
            for types,brands in products.items():
                for brand_name, product_list in brands.items():
                    print (brand_name)
                    for product in product_list:
                        id = product.get("id")
                        brand_name = product.get("name")
                        price = product.get("price")
                        print(f"{id} - brand name:{brand_name} - price:{price}")
        elif option ==2:
            name = input("Please enter your name: ")
            id_card = input("Please enter your id card: ")
            product_id = input("Please enter product id: ")
            client = {}
            client["name"] = name
            client["id_card"] = id_card
            client["product_id"] = product_id

            for types,brands in products.items():
                for brand_name, product_list in brands.items():
                    for product in product_list:
                        if product.get("id") == product_id:
                            product_selected = product
                            break

            if product_selected
            else: 
                print("product not found.")
        elif option ==3:
            break
        else:
            continue
main()