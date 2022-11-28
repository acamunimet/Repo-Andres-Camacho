import requests
import json

#1) Registrar equipos
def Teams():
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json"
    r = requests.get(url)
    teams_dict = r.json()
    country_name = teams_dict["name"]
    FIFA_code = teams_dict["fifa_code"]
    country_group = teams_dict["group"]
    return teams_dict

#2) Registrar estadios
def Stadiums():
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json"
    r = requests.get(url)
    stadiums_dict = r.json()
    return stadiums_dict

#3) Registrar partidos
def Matches():
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json"
    r = requests.get(url)
    matches_dict = r.json()
    return matches_dict

#4) Búsqueda partidos
def MatchSearch(Matches):
    search_step1 = int(input('''
¿Desea comenzar una búsqueda?

Sí - Inserte "1"
No - Inserte otro caracter.
'''))
    #if search_step1 == 1:


print(Stadiums())