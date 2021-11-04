
class LCS:
    def __init__(self, tam=0) -> None:
        self.tam = tam

    def __lt__(self, other):
        return self.tam < other.tam

    def __le__(self, other):
        return self.tam <= other.tam

    def __eq__(self, other):
        return self.tam == other.tam

    def __ne__(self, other):
        return self.tam != other.tam

    def __gt__(self, other):
        return self.tam > other.tam

    def __ge__(self, other):
        return self.tam >= other.tam

    def __str__(self):
        return str(self.tam)


def longaSubSeq(x, y):
    m = len(x)
    n = len(y)
    matrixLcs = [[LCS() for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if(i == 0 or j == 0):
                matrixLcs[i][j].tam = 0
            elif(x[i-1] == y[j-1]):
                matrixLcs[i][j].tam = 1 + matrixLcs[i-1][j-1].tam
            elif(matrixLcs[i-1][j].tam >= matrixLcs[i][j-1].tam):
                matrixLcs[i][j].tam = matrixLcs[i-1][j].tam
            else:
                matrixLcs[i][j].tam = matrixLcs[i][j-1].tam
    return matrixLcs[m][n].tam


X = 'ABCBDAB'
Y = 'BDCABA'



def superMinSubSeq(stringx, stringy):
    '''
        Entra: Duas string.
        SAÍDA: Tamanho da supersequência mais curta das duas strings.
        A estratégia aqui é utilizar o algoritmo da mais longa subsequencia.
    '''
    lcs = longaSubSeq(stringx, stringy)
    return (len(stringx) + len(stringy)) - lcs


print(superMinSubSeq(X, Y))
