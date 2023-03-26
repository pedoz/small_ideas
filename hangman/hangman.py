import random
import re


def main():
    word = get_word()
    #word agr é uma lista
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
    checker = list()
    for _ in letters:
        print("_", end=' ')
        checker.append("_")
    
    print(checker)
    print("\n")
    n = 5
    while n >= 0:
        letra = input("Letra:")
        print(word)
        print(letra)
        if len(letra) != 1:
            print("Invalido")
        if letra.isnumeric():
            print("Invalido")
        else:
            try:
                j = 0
                for i in range(len(letters)):
                    if letters[i] == letra:
                        checker.pop(i)
                        checker.insert(i, letra)
                        j = j + 1
                    if (i + 1) == len(letters) and j == 0:
                        n = n - 1
                print(checker)

            except IndexError:
                print("erro")

    for i in range(len(checker)):
        if checker[i] == "_":
            return "Não conseguiu :("

    else:
        return "Congrats"



if __name__ == "__main__":
    main()