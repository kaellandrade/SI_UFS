from math import floor


def binaryRec(arr, x, left, right) -> int:
    if(left == right):
        if(arr[left] == x):
            return left
        else:
            return -1
    else:
        meio = (left + right)//2
        
        if(arr[meio] == x):
            return meio

        if(x < arr[meio]):
            return binaryRec(arr, x, left, meio-1)

        else:
            return binaryRec(arr, x, meio+1, right)


vetor = [0, 5, 6, 40, 50, ]
LEFT = 0
print(binaryRec(vetor, 50, LEFT, len(vetor)))
