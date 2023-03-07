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
   Please enter a number from 1 to 12.

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


