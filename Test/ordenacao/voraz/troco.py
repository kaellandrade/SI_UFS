def troco(moedas: tuple, n) -> list:
    troco = []
    for i in range(0, len(moedas)):
        while(n >= moedas[i]):
            troco.append(moedas[i])
            n = n - moedas[i]
    return troco


print(troco((100, 25, 10, 5, 1), 100))
