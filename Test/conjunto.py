'''
Recebe um vetor A de tamanho An e um vetor
B de tamanho Bn. Retorna um vetor W, sendo W = A-B.
Utilizei aqui a busca simples, pois o vetores estão 
desordenado.
'''
def AcomplementoBSimple(A: int, An: int, B: int, Bn: int) -> list:
    W = []
    for i in range(0, An):
        eDiferente = True
        for j in range(0, Bn):
            if(A[i] == B[j]):
                eDiferente = False
                break
        if(eDiferente and A[i] not in W):
            W.append(A[i])
    return W

'''
Recebe um vetor e determinado elemento.
Se o elemento estiver em B será retornado seu índice,
None caso contrário.
'''
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

'''
Recebe um vetor A de tamanho An e um vetor
B. Retorna um vetor W, sendo W = A-B.
Como temos o vetor B ordenado utilizei aqui
a busca binária.
'''
def AcomplementoBBinary(A: list, An: int, B: list) -> list:
    W = []
    for i in range(0, An):  # O(n)
        if(bi_search(B, A[i]) == None): #Verifica se A[i] não está em B
            W.append(A[i])
    return W


A = [1, 2, 3, 4, 5, 6, 9]
B = [6, 7, 8, 10]

print(AcomplementoBBinary(A, len(A), B))
print(AcomplementoBSimple(A, len(A), B, len(B)))

