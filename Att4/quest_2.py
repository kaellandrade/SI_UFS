def rabin_karp_MATCHER(texto, padrao, d=256, q=3354393):

    totalOcorr = 0
    for pat in padrao:
        D = d  # Tabela ASCII
        M = len(pat)
        h = pow(d, M-1) % q
        p = 0  # Valor hash para o padrão
        N = len(texto)
        t = 0  # Valor hash para o texto

        for i in range(M):  # Pré-Processamento
            p = (d*p + ord(pat[i])) % q
            t = (d*t + ord(texto[i])) % q

        for s in range(N-M+1):
            if(p == t):
                if(pat == texto[s:s+M]):
                    totalOcorr += 1
            if(s < N-M):
                t = (D*(t-ord(texto[s])*h) + ord(texto[s+M])) % q
                if(t < 0):
                    t = t+q
    return totalOcorr


def findPrefix(pat: str, sufix=[]):
    '''
    Entrada: Uma String S
    Saída: Todos o possíveis prefixos de S
    Ex: 'casa' -> ['c','ca','cas','casa']
    '''
    if(len(pat) == 0):
        return sufix
    else:
        return findPrefix(pat[0:len(pat)-1], [pat[0:len(pat)]] + sufix)


TEXTO = 'agora é hora de tocar violão, em casa.'
PADRAO = 'casa'
PREFIX_PAT = findPrefix(PADRAO)

print(rabin_karp_MATCHER(TEXTO, PREFIX_PAT))
