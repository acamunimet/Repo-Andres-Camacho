def Match_Search():
    print('''
*****Bienvenido al sistema de búsqueda de partidos de la plataforma de tickets del Mundial de Fútbol Quatar 2022*****
''')
while True:
    search_step1 = int(input('''¿Cómo desea realizar su búsqueda?
1.- Buscar los partidos en los que participa un equipo específico - Inserte "1".
2.- Buscar los partidos que se jugarán en un estadio específico   - Inserte "2".
3.- Buscar los partidos que se jugarán en una fecha determinada   - Inserte "3".

Cancelar búsqueda   - Inserte "0"
    '''))
    if search_step1 == 1:
        team_to_play = str(input('''¿Qué equipo desea buscar?'''))
    elif search_step1 == 2:
        stadium_to_play = str(input('''¿De qué estadio desea ver los partidos disponibles?'''))
    elif search_step1 == 3:
        date_to_play = str(input('''¿Qué fecha le interesa ver?'''))
    elif search_step1 == 0:
        break         
    else:
        print("Favor, inserte un argumento válido.")
        pass