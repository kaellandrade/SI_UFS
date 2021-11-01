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


W = 13

pesos =   [1, 5]  # peso
valores = [1, 10]  # valor
# Para essa solução posso adicionar (item 5 + item 5) + (3*item1) 
# print(numpy.matrix(Knapsack(W, pesos, valores)))


def ilimite_Knapsack(W: int, pesos: list, valores: list) -> int:
    n = len(valores) #total de itens
    maxTab = [0 for _ in range(W+1)] #Tamanho de mochilas diferentes

    for i in range(W+1): #Para cada capacidade de mochila diferente
        for j in range(n): #Para cada item
            if(pesos[j] <= i): #se cabe na capacidade da mochila atual
                # Considera a solução a tual ou a solução anterior.
                maxTab[i] = max(maxTab[i], maxTab[i-pesos[j]] + valores[j])

    return maxTab[W]


print(ilimite_Knapsack(W, pesos, valores))
