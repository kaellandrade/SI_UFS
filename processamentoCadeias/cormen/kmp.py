class KMP:
    '''
    Recebe uma String T e um padrão P. Verifica as ocorrências 
    de P em T.
    '''
    def __init__(self, StringT, StringP) -> list:
        self.N = len(StringT)
        self.M = len(StringP)
        self.StringT = StringT
        self.StringP =StringP
        self.ARR_PRE = self.__compute_prefix_function()
        self.__KMP_algoritmo()

    def __KMP_algoritmo(self)->None:
        q = 0
        for i in range(0, self.N):
            while(q > 0 and self.StringP[q] != self.StringT[i]):
                q = self.ARR_PRE[q-1]
            if(self.StringP[q] == self.StringT[i]):
                q += 1
            if (q == self.M):
                print(f'Padrão ocorre deslocamento {(i-self.M)+1}')
                q = self.ARR_PRE[q-1]

    def __compute_prefix_function(self) -> list:
        ARR_PRE = [0] * self.M
        k = 0
        for q in range(1, self.M):
            while(k > 0 and self.StringP[k] != self.StringP[q]):
                k = ARR_PRE[k]
            if(self.StringP[k] == self.StringP[q]):
                k += 1
            ARR_PRE[q] = k
        return ARR_PRE

KMP('hoje o dia está lindo para viver.', 'está')