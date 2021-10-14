
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
        self.ARR_PRE = [0] * self.M #Array dos deslocamentos.
        self.__compute_prefix_function(self.StringP, self.M, self.ARR_PRE)
        self.ocorre = self.__KMP_algoritmo()

    @property
    def getOcorre(self) -> int:
        return self.ocorre

    def __KMP_algoritmo(self) -> None:
        i = 0
        j = 0
        ocorre = False
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
                ocorre = True
                return ocorre
        return ocorre

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

def invertString(string):
    '''
        Entrada: String s 
        Saida: String s invertida, porém com o primeiro caracter no final.
        Ex: (original) CASA
            (invertida) ASAC
            (desloca o primeiro caracter para o final) SACA
    '''
    M = len(string)-1
    nova_string = ''
    lastChar = ''
    for i in range(M, -1, -1):
        if(i != M):
            nova_string += string[i]
        else:
            lastChar = string[i]

    return nova_string + lastChar

def isCircular(T: str, S: str):
    '''
        ENTRADA: Padrao T e um string circular S
        SAÍDA: True se T for substring de S, false caso contrário. 
    '''
    firstTest = KMP(S, T).ocorre #Verificamos se o padrão é substring do texto original.
    if(not firstTest): #Se não for, vamos verificar se é substring do texto invertido.
        Sreversed = invertString(S)
        firstTest = KMP(Sreversed, T).ocorre
    return firstTest


print(isCircular('saca', 'casa'))
print(isCircular('sacas', 'casa'))
print(isCircular('paca', 'capa'))
print(isCircular('ta', 'pata'))
