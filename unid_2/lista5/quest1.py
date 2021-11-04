from math import inf


def minCut(precos: list, n: int) -> int:
    F = [0 for i in range(n+1)]
    
    precos = [1] + precos # Começamos do índice 1 agora
    m = len(precos)
    for i in range(1, n+1):
        temp = inf
        j = 1
        while (j <= m and i >= precos[j-1]):
            temp = min(F[i-precos[j-1]], temp)
            j += 1
        F[i] = temp + 1

    return F[n-1]


print(minCut([2, 6, 8, 9, 10, 17, 17, 20], 4))
