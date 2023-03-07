"""Créez des calendriers mensuels, 
enregistrés dans un fichier texte et adaptés à l'impression."""

import datetime

# Définir les constances

DAYS = ('Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi',
        'Vendredi', 'Samedi')
MONTHS = ('Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 
          'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 
          'Décembre')

print('Créer Calendrier')

while True:
    print('Entrer l\'année pour le calendrier:')
    response = input ('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Veuillez entrer une année numérique, comme 2023')
    continue

while True:
    print('Entrer le mois pour le calendrier, 1-12')
    response = input('> ')

    if not response.isdecimal():
        print('Veuillez entrer un mois numérique, comme 3 pour Mars')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print('Veuillez entrer un nombre de 1 à 12')


def getCalendarFor(year, month):
    calText = '' # CalText contiendra la chaine de notre calendrier

    # Mettre lle mois et l'année en haut du calendrier
    calText += (' ' * 33) + MONTHS[month - 1] + ' ' + str(year) + '\n'

    # Ajouter les libellés des jours de la seaine au calendrier
    calText += '...Dimanche....Lundi....Mardi....Mercredi....Jeudi....Vendredi....Samedi...\n'

    # La chaîne de lignes horizontales qui séparent les semaines
    weekSeparator = ('+----------' * 7) + '\n'

    # Les lignes vides ont dix espaces entre le séparateur de jours
    blankRow = ('|          ' * 7) + '|\n'

    # Obtenir la première date du mois (Le module datetime gère tous)
    currentDate = datetime.date(year, month, 1)
    # Aller en arrière jusqu'à ce que ça soit le dimanche (weekday retourne 6)
    # pour un dimanche.
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)
    
    while True: # Bloucle  sur chaque semaine du mois
        calText += weekSeparator

        # dayNumberRow est la ligne avec les numéros du jour de la semaine
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1) # Aller au jour suivant
        dayNumberRow += '|\n' # Ajouter une ligne verticale après Samedi

        # Ajouter la ligne du numéro du jour et 3 lignes vide au texte du calendrier
        calText += dayNumberRow 
        for i in range(4):
            calText += blankRow
        
        # Vérifier si nous avon fini avec le mois
        if currentDate.month != month:
            break

    # Alouter des lignes horizontales tout en bas du calendrier
    calText += weekSeparator
    return calText

calText = getCalendarFor(year, month)
print (calText)


# Enregistrer le calendrier dans un fichier texte
calendarFilename = 'calendar_{}_{}.txt'.format(year, month)
with open(calendarFilename, 'w') as fileObj:
    fileObj.write(calText)

print('Enrigister dans ' + calendarFilename)
