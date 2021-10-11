#TODO Transformar em Class
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


class KMP:
    '''
    Recebe uma String T e um padrão P. Verifica as ocorrências 
    de P em T.
    '''
    def __init__(self, StringT, StringP) -> None:
        self.N = len(StringT)
        self.M = len(StringP)
        self.StringT = StringT
        self.StringP = StringP
        self.ARR_PRE = [0] * self.M
        self.__compute_prefix_function(self.StringP, self.M, self.ARR_PRE)
        # print(self.ARR_PRE)
        self.ultimaOcorr = self.__KMP_algoritmo()
        
    @property
    def getUltimaOcorr(self) -> int:
        return self.ultimaOcorr

    def __KMP_algoritmo(self) -> None:
        i = 0
        j = 0
        ultimaOcorr = -1
        while i < self.N:
            if(self.StringT[i] == self.StringP[j]):
                i += 1
                j += 1
            else:
                if(j != 0):
                    j = self.ARR_PRE[j-1]
                else:
                    i += 1
            if(j == self.M):
                ultimaOcorr = i-j
                j = self.ARR_PRE[j-1]
        return ultimaOcorr

    def __compute_prefix_function(self, pat, M, ARR_PRE) -> list:
        '''
            Calcula o vetor pre-processador.
        '''
        len = 0
        i = 1
        while(i < M):
            if(pat[i] == pat[len]):
                ARR_PRE[i] = len + 1
                len += 1
                i += 1
            else:
                if(len != 0):
                    len = ARR_PRE[len-1]
                else:
                    ARR_PRE[i] = 0
                    i += 1



TEXTO = "Deslumbrem-se com a beleza das araras durante o passeio."
PADRAO = 'ara'

print('Horspool:')
print(horspoolMatching(TEXTO, PADRAO))

print('\nKMP')
print(KMP(TEXTO, PADRAO).getUltimaOcorr)