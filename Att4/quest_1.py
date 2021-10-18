def shifttable(padrao: str):
    '''
    Entrada: Padrão P [0..m - 1] e um alfabeto de caracteres possíveis.
    Saída: Tabela [0..size - 1] indexada pelos caracteres do alfabeto e
           preenchido com tamanhos de deslocamento calculados.
    '''
    tabela = [len(padrao)]*256  # Alfabeto 255 caracters. Tabela ASCII
    for i in range(len(padrao)-1):
        tabela[ord(padrao[i])] = len(padrao) - 1 - i

    return tabela


def horspoolMatching(texto, padrao):
    '''
    Entrada: Padrão P [0..m - 1] e texto T [0..n - 1]
    Saída:O índice da extremidade esquerda da última substring correspondente.
    ou -1 caso não seja encontrado um padrão.
    '''
    tabelaPre = shifttable(padrao) #Gerando a tabela de deslocamentos.
    m = len(padrao)
    n = len(texto)
    i = len(padrao) - 1 #Posição da extremidade direita do padrão.
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