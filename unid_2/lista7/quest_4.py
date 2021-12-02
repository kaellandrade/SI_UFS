#!python3.8

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

print(check_array_valid([1,2,9,10,21,12,23,8,25,20,27,4]))
