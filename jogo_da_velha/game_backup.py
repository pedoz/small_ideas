import random



def main():
    n = [0,1,2,3,4,5,6,7,8,9]
    while True:
        jogo = f'''
        {n[1]} | {n[2]} | {n[3]}
        -----------
        {n[4]} | {n[5]} | {n[6]} 
        -----------
        {n[7]} | {n[8]} | {n[9]}
        '''
        print(jogo)
        n = jogada_jogador(n)
        n = jogada_maquina(n)
        print(jogo)

def jogada_jogador(n):
    x = 'X'
    o = 'O'
    symbol = x
    while True:
        try:
            j_jogador = int(input("Qual posição tu quer colocar? "))
            if 9 >= j_jogador >= 1:
                for number in n:
                    if j_jogador == number:
                        n.pop(number)
                        n.insert(number, symbol)
                        return n
                    elif number == len(n)-1:
                        print('Coloque uma posição válida, por favor')
            else:
                print('Coloque uma posição válida, por favor')
                pass
        except ValueError:
            print('Coloque uma posição válida, por favor')

def jogada_maquina(n):
    x = "X"
    o = "O"
    symbol = o
    while True:
        try:
            jogada = random.choice(n)
            if jogada == 'O' or jogada == 'X' or jogada == 0:
                pass
            else:
                for number in n:
                    if number == jogada:
                        n.pop(number)
                        n.insert(number, symbol)
                        return n
        except ValueError:
            print("Erro indesejado")


if __name__ == '__main__':
    main()