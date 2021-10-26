# Abordagem utilizando MergeSort
def mergeSort(A):
    if (len(A) > 1):
        meio = len(A)//2
        B = A[:meio]
        C = A[meio:]
        mergeSort(B)
        mergeSort(C)
        merge(B, C, A)
    return A


def merge(B, C, A):
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


def maxProduct(lista):
    if(len(lista) == 1):
        return lista[0]
    else:
        first = lista[0] * lista[1]
        last = lista[len(lista)-1] * lista[len(lista)-2]
        if(first > last):
            return first
        else:
            return last

# Abordagem sem precisar ordenar


def maxProductLinear(lista):
    maiorPositivo_1 = 0
    maiorPositivo_2 = 0

    maiorNegativo_1 = 0
    maiorNegativo_2 = 0

    for i in lista:
        if (i > maiorPositivo_1):
            maiorPositivo_2 = maiorPositivo_1
            maiorPositivo_1 = i
        elif(i > maiorPositivo_2):
            maiorPositivo_2 = i
        if(i < 0 and abs(i) > abs(maiorNegativo_1)):
            maiorNegativo_2 = maiorNegativo_1
            maiorNegativo_1 = i
        elif(i < 0 and abs(i) > abs(maiorNegativo_2)):
            maiorNegativo_2 = i
    proc_positivos = maiorPositivo_1*maiorPositivo_2
    proc_negativos = maiorNegativo_1*maiorNegativo_2
    if(proc_positivos > proc_negativos):
        return proc_positivos
    else:
        return proc_negativos


print(maxProductLinear([5, -10, 4, 6, -2, -3]))
print(maxProduct(mergeSort([5, -10, 4, 6, -2, -3])))
