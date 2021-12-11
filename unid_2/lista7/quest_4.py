#!python3.8
from random import randrange
TOLERANCIA = 3


def check_array_valid(arr: list) -> bool:
    for i in range(len(arr)):
        par = 0
        impar = 0
        for j in arr[i:TOLERANCIA+i]:
            if(j % 2 == 0):
                par += 1
            else:
                impar += 1
        if(par == TOLERANCIA or impar == TOLERANCIA):
            return False
    return True


def lasVegas(arr: list):
    result = []
    while(len(arr)):
        index = randrange(len(arr))
        result.insert(0, arr.pop(index))
        if(not check_array_valid(result)):
            arr.insert(0, result.pop(0))

    return result


print(lasVegas([1, 2, 4, 8, 9, 10, 12, 20, 21, 23, 25, 27]))