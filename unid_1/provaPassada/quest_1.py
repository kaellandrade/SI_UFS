from math import ceil, floor


def binaryRec(arr, x, left, right) -> int:
    meio = ceil((left + right)/2)

    if(right < left):
        if(meio > len(arr)-1):  # Se o meio estourar não encontramos esse valor z
            return -1
        else:
            return meio  # Caso contrário ele está na posição [meio]

    if(arr[meio] == x):
        return meio
    else:
        if (arr[meio] > x):
            return binaryRec(arr, x, left, meio - 1)
        else:
            return binaryRec(arr, x, meio + 1, right)


vetor = [13]
LEFT = 0
print(binaryRec(vetor, 13, LEFT, len(vetor)-1))
