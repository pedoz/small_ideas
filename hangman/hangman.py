import random
import re


def main():
    word = get_word()
    print(hangman(word))


def get_word():
    word_list = [
            "saude",
            "pianos",
            "casa",
    ]

    sel_word =  random.choice(word_list)
    return list(sel_word)



def hangman(word):
    letters = word
    count = len(word)
    checker = list()
    n = 5
    wrong_l = list()
    letras_utilizadas = list()

    for _ in letters:
        print("_", end=' ')
        checker.append("_")
    print(checker, end ='\n')

    while True:

        if count == 0:
            return 'Parabens'
        
        letra = input("Letra:")

        if len(letra) != 1:
            print("Invalido")
        elif letra.isnumeric():
            print("Invalido")
        elif letra == 
        else:
            if n == 0:
                return "Falhou :("
            else:
                try:
                    j = 0
                    for i in range(len(letters)):
                        if letters[i] == letra:
                            count = count - 1
                            checker.pop(i)
                            checker.insert(i, letra)
                            j = j + 1
                        elif ((i + 1) == len(letters)) and (j == 0):
                            n = n - 1
                            wrong_l.append(letra)
                            print("letras que não tem:", end = ' ')
                            for i in wrong_l:
                                print(i, sep = ', ')

                    print(checker)

                except IndexError:
                    print("erro")





if __name__ == "__main__":
    main()