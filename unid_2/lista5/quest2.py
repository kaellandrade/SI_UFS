import numpy

# TODO: analizar esse código


def Knapsack(W: int, pesos: list, valores: list) -> int:
    n = len(valores)
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(0, n+1):
        for j in range(0, W+1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif(j - pesos[i-1] >= 0):
                K[i][j] = max(valores[i-1] + K[i-1][j-pesos[i-1]], K[i-1][j])
            else:
                K[i][j] = K[i-1][j]

    return K


W = 5

pesos =   [2,  1,  3,   2]  # peso
valores = [12, 10, 20, 15]  # valor

# print(numpy.matrix(Knapsack(5, pesos, valores)))


# Debugar o código e ler o artigo 
# https://www.geeksforgeeks.org/unbounded-knapsack-repetition-items-allowed/
def ilimite_Knapsack(W: int, pesos: list, valores: list) -> int:
    n = len(valores)
    maxTab = [0 for _ in range(W+1)]

    for i in range(W+1):
        for j in range(n):
            if(pesos[j] <= i):
                maxTab[i] = max(maxTab[i], maxTab[i-pesos[j]] + valores[j])
    
    return maxTab
    
print(ilimite_Knapsack(W, pesos, valores))