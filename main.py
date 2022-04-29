import random
import time
from getpass import getpass
from weakref import finalize

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
    optionChosen = input()
    while len(optionChosen) == 0:
        print('Selecciona una opcion: ')
        optionChosen = input()
    optionChosen = int(optionChosen)
    if optionChosen == 1:
        optionOne()
    elif optionChosen == 2:
        optionTwo()
    elif optionChosen == 3:
        quit()
    else:
        print('Opcion no valida')

def play_loop():
    global play_game
    play_game = input("Quieres jugar otra vez? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Quieres jugar otra vez? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Gracias por jugar, te esperamos de regreso!")
        exit()
    else:
        print("Gracias por jugar, te esperamos de regreso!")
        exit()

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
    printTitle()
    print('Ingrese la palabra: ')
    correctWord = getpass('Palabra: ').replace(" ", "")
    displayWord = codeWord(correctWord)
    # print(displayWord)
    guessTheWord(displayWord, correctWord)
    play_loop()

def printTitle():
    print('╔╦╗╔╦═══════════════════════╗')
    print('║║╚╝╠═╦═╦═╦══╦═╦═╗╔═╦═╦══╦═╗║')
    print('║║╔╗╠╝║║║║║║║╠╝║║║║║╠╝║║║║╩╣║')
    print('║╚╝╚╩═╩╩╬═╠╩╩╩═╩╩╝╠═╠═╩╩╩╩═╝║')
    print('╚═══════╩═╩═══════╩═╩═══════╝')

def printWiningMeassage(correct):
    print('════════════════════════════════════════════')
    print('La palabra es => ', correct)
    print('╔╦══╦═╦═╦╦═╦═╦══╦═╦╦╗')
    print('║║╔═╣║║║║║║║╚╬╣╠╣═╣║║')
    print('║║╚╝║╩║║║║╩╠╗║║║║═╬╣║')
    print('║╚══╩╩╩╩═╩╩╩═╝╚╝╚═╩╝║')
    print('╚═══════════════════╝')
    print('════════════════════════════════════════════')

def guessTheWord(word, aws):
    start = 0
    count = 0
    usedWords = []
    end = len(aws)
    while(word != aws):
        tempWord = [i for i in word]
        print('════════════════════════════════════════════')
        print('Palabra: ', ' '.join(tempWord))
        # print('Testing vlues: ', word, aws)
        print('Ingresa una letra')
        temCharacter = input()
        while len(temCharacter) == 0:
            print('Ingresa una letra')
            temCharacter = input()
        temCharacter = temCharacter[0]
        time.sleep(1)
        if not(temCharacter in usedWords):
            usedWords.append(temCharacter)
        else:
            print('════════Letra repetida!════════')

        if temCharacter in aws:
            characterCount = aws.count(temCharacter)
            start = 0
            for i in range(0,characterCount):
                changePosition = aws.find(temCharacter, start, end)
                start = changePosition + 1
                tempListWord = list(word)
                tempListWord[changePosition] = temCharacter
                word = ''.join(tempListWord)
        else:
            count += 1
            errorCount(count, aws)

    printWiningMeassage(aws)

def codeWord(word):
    temp = ['_' for i in word]
    return ''.join(temp)

def errorCount(count, correctAws):
    if count == 1:
        time.sleep(1)
        print('════════════════════════════════════════════')
        print("   _____ \n"
                "  |     | \n"
                "  |     O \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
        print("Letra incorrecta")
        print('════════════════════════════════════════════')
    elif count == 2:
        time.sleep(1)
        print('════════════════════════════════════════════')
        print("   _____ \n"
                "  |     | \n"
                "  |     O \n"
                "  |     | \n"
                "  |      \n"
                "__|__\n")
        print("Letra incorrecta")
        print('════════════════════════════════════════════')
    elif count == 3:
        time.sleep(1)
        print('════════════════════════════════════════════')
        print("   _____ \n"
                "  |     | \n"
                "  |     O \n"
                "  |     |\ \n"
                "  |      \n"
                "__|__\n")
        print("Letra incorrecta")
        print('════════════════════════════════════════════')
    elif count == 4:
        time.sleep(1)
        print('════════════════════════════════════════════')
        print("   _____ \n"
                "  |     | \n"
                "  |     O \n"
                "  |    /|\ \n"
                "  |      \n"
                "__|__\n")
        print("Letra incorrecta")
        print('════════════════════════════════════════════')
    elif count == 5:
        time.sleep(1)
        print('════════════════════════════════════════════')
        print("   _____ \n"
                "  |     | \n"
                "  |     O \n"
                "  |    /|\ \n"
                "  |    /  \n"
                "__|__\n")
        print("Letra incorrecta")
        print('════════════════════════════════════════════')
    elif count == 6:
        time.sleep(1)
        print('════════════════════════════════════════════')
        print("   _____ \n"
                "  |     | \n"
                "  |     O \n"
                "  |    /|\ \n"
                "  |    / \ \n"
                "__|__\n")
        print('La palabra era: ', correctAws)
        print('════════════════════════════════════════════')
        print("═══════════Fin del juego, perdiste══════════")
        print('════════════════════════════════════════════')
        play_loop()

if __name__ == "__main__":
    main()