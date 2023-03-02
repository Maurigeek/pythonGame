import random

NUM_DIGITS = 4
MAX_GUESSES = 12


def main():
    print('''Bagels, un jeu de logique déductive.

     Je pense à un nombre à {} chiffres sans chiffres répétés.
     Essayez de deviner ce que c'est. Voici quelques indices :
     Quand je dis : ça veut dire :
       Doré Un chiffre est correct mais dans la mauvaise position.
       Sido Un chiffre est correct et dans la bonne position.
       Bagels Aucun chiffre n'est correct.

Par exemple, si le numéro secret était 248 et que votre supposition était 843, l'indices seraient Fermi Pico.'''.format(NUM_DIGITS))

    while True: # Main game loop.
        # This stores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print("J'ai imaginé un chiffre.")
        print("Vous avez {} suppositions pour l'obtenir.".format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter avalid guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')
            
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break #They're correct, so break out of this loop.
            if numGuesses > MAX_GUESSES:
                print('Vous avez manqué de suppositions.')
                print('La réponse était {}.'.format(secretNum))
        
        # Ask player if they want to play again;
        print('Voulez-vous rejouer? (Oui ou non)')
        if not input('> ').lower().startswith('y'):
            break
    print("Merci d'avoir joué!")


def getSecretNum():
    """Renvoie une chaîne composée de NUM_DIGITS chiffres aléatoires uniques."""

    numbers = list('0123456789')  # Create a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle them into random order.

    #Get the first NUM_DIGITS digits in the list for the secret number;
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Renvoie une chaîne avec les indices doré, sido, bagels pour deviner
     et la paire de numéros secrets."""

    if guess == secretNum:
        return "Vous l'avez trouvé"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place.
            clues.append('Sido')
        elif guess[i] in secretNum:
            # A correct digit is in the incorrect place.
            clues.append('Doré')
    if len(clues) == 0:
        return 'Bagels' # There are no correct digits all.
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return ' '.join(clues)

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()


        
        