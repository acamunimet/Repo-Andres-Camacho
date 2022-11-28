def print_welcome():
    print("*****Welcome*****")

def get_user_option(dict):
    for key, value in dict.items():
        for key_interno, value_interno in value.items():
                print(f"{key} - {value_interno}", end = "")
                print("")
    return input("Please, enter an option: ")

def get_client_data(study):
    client = {
        "id":input("Please enter the client's id: "),
        "age":input("Please enter the client's age: "),
        "gender":input("Please indicate if the client is M or F: ").upper()
    }
    return client

def print_invoice(client):
    print("****RECEIPT****")
    print("ID:",client.get{"id"})
    print("Age:",client.get{"age"})
    print("Gender:",client.get{"gender"})
    print("NetAmmount:",client.get{"id"})

def main():
    studies_dict_values = {
        "U":{
            "name":"Ultrasonido",
            "price":8900
        },
        "T": {
            "name":"Tomografía"
            "price":12640
        }
        "R":{
            "name":"Radiología"
            "price":15600
        }
        }

def print_invoice(study_):

    clients = []
    print_welcome()
    while True
        option = get_user_option(studies_dict_values)
        client = get_client_data(option)
        get_netammount
        print_invoice(option, client)
        clients.append(client)

main()