from kmp import KMP


def shifttable(padrao: str):
    tabela = [len(padrao)]*256  # Alfabeto 255 caracters.
    for i in range(len(padrao)-1):
        tabela[ord(padrao[i])] = len(padrao) - 1 - i

    return tabela


def horspoolMatching(texto, padrao):
    tabelaPre = shifttable(padrao)
    m = len(padrao)
    n = len(texto)
    i = len(padrao) - 1
    ultimaOcorr = -1
    while(i <= n-1):
        k = 0
        while(k <= m-1 and padrao[m-1-k] == texto[i-k]):
            k += 1
        if(k == m):
            ultimaOcorr = i-m+1
        i = i + tabelaPre[ord(texto[i])]
    return ultimaOcorr