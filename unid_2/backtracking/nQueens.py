#!python3.8
def nQueens(n_board: int) -> list:
    '''
        ENTRADA: o tamanho do tabuleiro.
        SAÍDA: Caso exista solução para estância do problema devolvemos uma lista.
    '''
    x: list = [0]*(n_board+1)
    nq(1, n_board, x)  # Aplicando backtracking
    print('Sem solução!')


def nq(i: int, n_board: int, x: list) -> int:
    '''
    ENTRADA:Rainha i, tamanho do tabuleiro n, solução x
    SAÍDA: X[0] indicando se tem soução (1) ou (0) caso contrário.

    '''
    for j in range(1, n_board+1): #valor da coluna
        if(posicaoValida(x, i, j)):
            # Coloque a rainha i na coluna j
            x[i] = j
            # Cheque se já posicionou todas as rainhas ou se precisa continuar a busca da soução
            if(i == n_board): 
                x[0] = 1 #Existe solução
                print(f'Solução -> {x[1:]}')
                exit()
            else:
                nq(i+1, n_board, x)  # backtracking


def posicaoValida(x, r, col) -> bool:
    '''
        ENTRADA: Rainha r e coluna col
        SAÍDA: True se a rainha r pode ser alicada na coluna cool, False caso contrário.
    '''

    '''
     Checa se a col já foi utilizada por uma rainha de índice anterior a r
     e também se a rainha k não ataca em diagonal da rainha r
    '''
    for k in range(1, r):
        if((x[k] == col) or (abs(x[k] - col) == abs(k - r))):
            return False
    return True


nQueens(4)
