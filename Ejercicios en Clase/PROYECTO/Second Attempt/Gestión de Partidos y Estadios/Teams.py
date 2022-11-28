import requests
import json

#Clase Equipos
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

#def show_matches():
    #for teams_dict in r.json():
        #name = teams_dict['name']
        #FIFA_code = teams_dict['fifa_code']
        #group = teams_dict['group']
        #id = teams_dict['id']
