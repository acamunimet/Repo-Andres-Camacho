import requests
import json

#Clase Partidos
class Match():
    def __init__(self, home_team, away_team, date, stadium_id, id):
        self.home_team = home_team
        self.away_team = away_team
        self.date = date
        self.stadium_id = stadium_id
        self.id = id

#Datos del API
url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json"
r = requests.get(url)
for matches_dict in r.json():
    home_team = matches_dict['home_team']
    away_team = matches_dict['away_team']
    date = matches_dict['date']
    stadium_id = matches_dict['stadium_id']
    id = matches_dict['id']
    print(home_team, away_team, date, stadium_id, id)

def show_matches():
    print(f'''
{home_team} VS. {away_team}.

Fecha de Encuentro: {date}
En:                 {stadium_id}''')