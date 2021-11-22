
class LCS:
    def __init__(self, tam=0, dir='*') -> None:
        self.tam = tam
        self.dir = dir

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
                matrixLcs[i][j].dir = 'D'
            elif(matrixLcs[i-1][j].tam >= matrixLcs[i][j-1].tam):
                matrixLcs[i][j].tam = matrixLcs[i-1][j].tam
                matrixLcs[i][j].dir = 'A'
            else:
                matrixLcs[i][j].tam = matrixLcs[i][j-1].tam
                matrixLcs[i][j].dir = 'E'
    return matrixLcs


def print_LCS(LCS: LCS, X, i, j):
    if(i == 0 or j == 0):
        return
    if(LCS[i][j].dir == 'D'):
        print_LCS(LCS, X, i-1, j-1)
        print(X[i-1])
    elif(LCS[i][j].dir == 'A'):
        print_LCS(LCS, X, i-1, j)
    else:
        print_LCS(LCS, X, i, j-1)


X = 'ABC'
Y = 'ACF'


i = len(X)
j = len(Y)
print_LCS(longaSubSeq(X, Y), X, i, j)

# ABCBDCABA