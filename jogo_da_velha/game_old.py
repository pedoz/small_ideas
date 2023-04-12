import random

n = [0,1,2,3,4,5,6,7,8,9]

jogo = f'''
 {n[1]} | {n[2]} | {n[3]}
-----------
 {n[4]} | {n[5]} | {n[6]} 
-----------
 {n[7]} | {n[8]} | {n[9]}
 '''
posições = n[1:]

def main():
    print(jogo)
    print(posições)
    jogada_jogador()
    print(posições)

def jogada_jogador():
    global posições
    x = 'X'
    o = 'O'
    while True:
        try:
            j_jogador = int(input("Qual posição tu quer colocar? "))
            for number in posições:
                if j_jogador == number:
                    posições.pop(number-1)
                    posições.insert(number-1, x)
                    return posições
        except ValueError:
            print('Coloque uma posição válida, por favor')





if __name__ == '__main__':
    main()