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
    randomWord = []
    with open("data.txt", "r", encoding="utf-8") as f:
        for line in f:
            randomWord.append(line)
    correctWord = randomWord[random.randint(0, len(randomWord)-1)]
    correctWord = correctWord[:-1]
    displayWord = codeWord(correctWord)
    # print(displayWord)
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
    # aws = [i for i in aws]
    start = 0
    end = len(aws)
    while(word != aws):
        tempWord = [i for i in word]
        print('Palabra: ', ' '.join(tempWord))
        print(word, aws)
        print('Ingresa una letra')
        temCharacter = input()
        # while(temCharacter in aws):
        if temCharacter in aws:
            print(temCharacter in aws)
            print(aws.find(temCharacter, start, end))
            changePosition = aws.find(temCharacter, start, end)
            start = changePosition + 1
            tempListWord = list(word)
            tempListWord[changePosition] = temCharacter
            word = ''.join(tempListWord)
            # word[aws.index(temCharacter)] = temCharacter
            print('Palabra: ', ' '.join(word))

            # word = [temCharacter for i in aws if aws[i] == temCharacter]

def codeWord(word):
    temp = ['_' for i in word]
    return ''.join(temp)

if __name__ == "__main__":
    main()