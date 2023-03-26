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
    n = 5
    wrong_l = list

    for _ in letters:
        print("_", end=' ')
        checker.append("_")
    print(checker + len(checker), end ='\n')

    while n >= 0:

        if len(word) == 0:
            return 'Parabens'
        
        letra = input("Letra:")
        print(word)
        print(letra)

        if len(letra) != 1:
            print("Invalido")
        elif letra.isnumeric():
            print("Invalido")
        
        else:
            try:
                j = 0
                for i in range(len(letters)):
                    if letters[i] == letra:
                        word.remove(i)
                        checker.pop(i)
                        checker.insert(i, letra)
                        j = j + 1
                    elif ((i + 1) == len(letters)) and (j == 0):
                        n = n - 1
                        wrong_l.append(letra)
                        print("Nâo contém essa letra")
                        print("letras que não tem:" + wrong_l, sep = " ")

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