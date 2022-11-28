import requests
import json

#1.- Registrar Equipos
class Team():
    def __init__(self, name, FIFA_code, group, id):
        self.name = name
        self.FIFA_code = FIFA_code
        self.group = group
        self.id = id

#Datos del API
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json"
    r = requests.get(url)
    for teams_dict in r.json():
        name = teams_dict['name']
        FIFA_code = teams_dict['fifa_code']
        group = teams_dict['group']
        id = teams_dict['id']

        print(teams_dict)

#2.- Registrar Estadios
class Stadiums():
    def __init__(self, id, name, capacity, restaurants):
        self.id = id
        self.name = name
        self.capacity = capacity
        self.restaurants = restaurants

class Restaurant():
    def __init__(self, stadium_id, stadium_name, capacity, restaurants):
        self.stadium_id = stadium_id
        self.stadium_name = stadium_name
        self.capacity = capacity
        self.restaurants = restaurants

class Product():
    def __init__(self, product_name, product_quantity, product_price, product_type, product_additional):
        self.product_name = product_name
        self.product_quantity = product_quantity
        self.product_price = product_price
        self.product_type = product_type
        self.product_additional = product_additional

#Datos del API
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json"
    r = requests.get(url)
    for stadium_list in r.json():
        stadium_id = stadium_list['id']
        stadium_name = stadium_list['name']
        capacity = stadium_list['capacity']
        restaurants = stadium_list['restaurants']
        for restaurant in restaurants:
            rest_name = restaurant['name']
            rest_products = restaurant['products']
            for product in rest_products:
                product_name = product['name']
                product_quantity = product['quantity']
                product_price = product['price']
                product_type = product['type']
                product_additional = product['adicional']
                print(product_quantity)