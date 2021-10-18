def mergeSort(A):
    '''
        ENTRADA: Vetor A em ordem arbitrária.
        SAÍDA: Vator A em ordem crescente.
    '''
    if (len(A) > 1):
        meio = len(A)//2
        B = A[:meio]
        C = A[meio:]
        mergeSort(B)
        mergeSort(C)
        merge(B, C, A)
    return A


def merge(B, C, A):
    '''
    ENTRADA: Duas listas B e C e um vetor A
    SAÍDA: A mesclagem de de B e C.
    '''
    i = j = k = 0
    while(i < len(B) and j < len(C)):
        if (B[i] <= C[j]):
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1
        k += 1
    if (i == len(B)):
        A[k:len(A)] = C[j:len(C)]
    else:
        A[k:len(A)] = B[i:len(C)]

print(mergeSort([10,20,0,-1,0,-1,100]))