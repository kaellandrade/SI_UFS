def ilimite_Knapsack(W: int, pesos: list, valores: list) -> int:
    n = len(valores) #total de itens
    maxTab = [0 for _ in range(W+1)] #Tamanho de mochilas diferentes

    for i in range(W+1): #Para cada capacidade de mochila diferente
        for j in range(n): #Para cada item
            if(pesos[j] <= i): #se cabe na capacidade da mochila atual
                # Considera a solução a tual ou a solução anterior.
                maxTab[i] = max(maxTab[i], maxTab[i-pesos[j]] + valores[j])

    return maxTab[W]

W = 13

pesos =   [1, 5]  # peso
valores = [1, 10]  # valor

print(ilimite_Knapsack(W, pesos, valores))
