from util import calculateTime


def AcomplementoBSimple(A: int, An: int, B: int, Bn: int) -> list:
    W = []
    for i in range(0, An):
        eDiferente = True
        for j in range(0, Bn):
            if(A[i] == B[j]):
                eDiferente = False
        if(eDiferente and A[i] not in W):
            W.append(A[i])
    return W


def bi_search(B: int, element: int) -> bool:
    baixo = 0
    alto = len(B) - 1
    while(baixo <= alto):
        meio = (baixo+alto)//2  # Divisão inteira
        if(B[meio] == element):
            return meio
        elif(element > B[meio]):
            baixo = meio + 1
        else:
            alto = meio - 1
    return None


def AcomplementoBBinary(A: int, An: int, B: int, Bn: int) -> list:  # O(n.log(n))
    W = []
    for i in range(0, An):  # O(n)
        if(bi_search(B, A[i]) == None):  # O(log(n))
            W.append(A[i])
    return W


A = [x for x in range(999, 10000)]
B = [x for x in range(0, 1000)]

print(AcomplementoBBinary(A, len(A), B, len(B)))
print(AcomplementoBSimple(A, len(A), B, len(B)))

print(f'Binária: {calculateTime.calcTime(lambda: AcomplementoBBinary(A, len(A), B, len(B)))}')
print(f'Simples: {calculateTime.calcTime(lambda: AcomplementoBSimple(A, len(A), B, len(B)))}')
