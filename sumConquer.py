def soma(arr):
    if(len(arr) == 0):
        return 0
    if(len(arr) == 1):
        return arr[0]
    else:
        meio = len(arr)//2
        A = arr[:meio]
        B = arr[meio:]
        s = soma(A) + soma(B)
        return s


print(soma([1,2,3,5,6,7,8,9,10]) == sum([1,2,3,5,6,7,8,9,10]))
