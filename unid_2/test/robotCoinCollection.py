
def RobotCoinCollection(matrix: list) -> int:
    '''
        Aplicando programação dinâmica para computar o maior
        número de moedas que um robô pode coletar em um tabuleiro 
        n x m iniciando em (1,1) e movendo para direita e para baixo.

        ENTRADA: Matriz n x m onde os elementos contém 0 ou 1 para
        representar a falta de uma moeda ou a existência, respectivamente.
        SAÍDA: Maior número de moedas coletadas.
    '''
    n = len(matrix)
    m = len(matrix[0])
    F = [[0 for i in range(m)] for j in range(n)]
    F[0][0] = matrix[0][0]
    for j in range(1, m):
        F[0][j] = F[0][j-1] + matrix[0][j]

    for i in range(1, n):
        F[i][0] = F[i-1][0]+matrix[i][0]
        for j in range(1, m):
            F[i][j] = max(F[i-1][j], F[i][j-1])+matrix[i][j]

    return F[n-1][m-1]


print(RobotCoinCollection([
    [0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0],
]))
