import random
import re


def main():
    word = get_word()
    #word agr é uma lista
    hangman(word)


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
    for i in letters:
        print("_", end=' ')
    n = 5
    while n >= 0:
        try:
            letra = input("\nLetra:")
            print(letra)
            if (len(letra) != 1) or (re.search('\W', letra)):
                print("Invalido")
                pass
            else:
                print("Foi")
        except IndexError:
            print("erro")



if __name__ == "__main__":
    main()