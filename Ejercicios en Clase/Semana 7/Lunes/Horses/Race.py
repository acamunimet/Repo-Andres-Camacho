import random
class Race:
    def __init__(self, number, horse_list):
        self.number = number
        self.horse_list = horse_list

    def start_race(self):
        print("¡PARTIDA!")

    def choose_winner(self, horses):
        print("The winner is: " random.choice(horses).name)