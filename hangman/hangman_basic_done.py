import random
import re


def main():
    word = get_word()
    print(hangman(word))


def get_word():
    word_list = [
            #"saude",
            #"pianos",
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

    for _ in letters:
        print("_", end=' ')
        checker.append("_")
    print(checker, end ='\n')

    while True:

        if count == 0:
            return 'Parabens'
        if n == 0:
            return "Falhou :("
        
        letra = input("Letra:")

        if len(letra) != 1:
            print("Invalido")
        elif letra.isnumeric():
            print("Invalido")
        elif letra in checker:
            print('Letra repetida')
        elif letra in wrong_l:
            print('Já não tem essas letras: ', end = '')
            print(wrong_l)

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
                        print(*wrong_l, sep = ', ')

                print(checker)

            except IndexError:
                print("erro")





if __name__ == "__main__":
    main()