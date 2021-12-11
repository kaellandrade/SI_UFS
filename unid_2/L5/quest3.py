
class TotSubSeq:
    def __init__(self, tam=0) -> None:
        self.tam = tam

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __str__(self):
        return str(self.tam)


def ocorrSubSeq(x, y):
    '''
    Estou utilizando a mesma estratégia do slide 9.
    porém, não preciso do atributo de direção aqui.
    '''
    m = len(x)
    n = len(y)

    matrixTotSubSeq = [[TotSubSeq() for _ in range(n+1)] for _ in range(m+1)]

    #Caso a primeira string seja vazia
    for i in range(n+1): 
        matrixTotSubSeq[0][i].tam = 0
    
    #Caso a segunda estring seja vazia.
    for j in range(m+1):
        matrixTotSubSeq[j][0].tam = 1

    for i in range(1, m+1):
        for j in range(1, n+1):
            if(x[i-1] == y[j-1]):  # Se os último caracteres forem iguais
                matrixTotSubSeq[i][j].tam = matrixTotSubSeq[i-1][j-1].tam + matrixTotSubSeq[i-1][j].tam
                
            else: #Caso contrário ignoramos o caracter da primeira string.
                matrixTotSubSeq[i][j].tam = matrixTotSubSeq[i-1][j].tam
    return matrixTotSubSeq[m][n]


print(ocorrSubSeq('arraial', 'ra'))
