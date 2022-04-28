import os
import random


global displayWord
global correctWord

def main():
    menu_options = {
        1: 'Usar diccionario',
        2: 'Ingresar palabra',
        3: 'Exit',
    }
    printTitle()
    print('Selecciona una opcion: ')
    print_menu(menu_options)
    optionChosen = int(input())
    if optionChosen == 1:
        optionOne()
        os.system('clear')
    elif optionChosen == 2:
        optionTwo()
    elif optionChosen == 3:
        quit()
    else:
        print('Opcion no valida')

def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
    else:
        print("Thanks For Playing! We expect you back again!")

def print_menu(menu_options):
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )


def optionOne():
    printTitle()
    print('Ingresa una letra')
    randomWord = []
    with open("data.txt", "r", encoding="utf-8") as f:
        for line in f:
            randomWord.append(line)
    correctWord = randomWord[random.randint(0, len(randomWord)-1)]
    correctWord = correctWord[:-1]
    displayWord = codeWord(correctWord)
    guessTheWord(displayWord, correctWord)
    play_loop()

def optionTwo():
    print('Option2')

def printTitle():
    print('╔╦╗╔╦═══════════════════════╗')
    print('║║╚╝╠═╦═╦═╦══╦═╦═╗╔═╦═╦══╦═╗║')
    print('║║╔╗╠╝║║║║║║║╠╝║║║║║╠╝║║║║╩╣║')
    print('║╚╝╚╩═╩╩╬═╠╩╩╩═╩╩╝╠═╠═╩╩╩╩═╝║')
    print('╚═══════╩═╩═══════╩═╩═══════╝')

def guessTheWord(word, aws):
    print(' '.join(word))
    # print(word, aws)

def codeWord(word):
    temp = ['_' for i in word]
    return temp

if __name__ == "__main__":
    main()