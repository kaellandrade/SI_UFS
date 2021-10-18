from math import floor


def binaryRec(arr, x, left, right) -> int:
    if(right < left):
        return -1
    meio = floor((left + right)/2)
    if(arr[meio] == x):
        return meio
    elif (arr[meio] > x):
        return binaryRec(arr, x, left, meio - 1)
    else:
        return binaryRec(arr, x, meio + 1, right)


vetor = [0, 1, 2, 3, 4, 5, 6, 50]
LEFT = 0
print(binaryRec(vetor, 50, LEFT, len(vetor)-1))
