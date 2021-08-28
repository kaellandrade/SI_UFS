'''
Dada uma string binária contZeroOne verifica
se a quantidade dee 0s é a mesma que a quantidade de 1s;
'''


def contZeroOne(strBinaria: str, lengbinaria: int) -> bool:
    totalZeros = totalUns = 0  # O(1)
    for char in range(0, lengbinaria):  # O(n) LINEAR
        if strBinaria[char] == '0':  # O(1)
            totalZeros += 1  # O(1)
        else:
            totalUns += 1  # O(1)
    return totalUns == totalZeros  # O(1)


def binary(x: list, i: int, n: int, qt0: int, qt1: int):
    if qt1 > qt0:
        return False
    elif (i <= n):
        if(x[i] == '1'):
            return binary(x, i+1, n, qt0, qt1+1)
        else:
            return binary(x, i+1, n, qt0+1, qt1)
    return contZeroOne(x, len(x))


string = '00101'
print(binary(string, 0, len(string)-1, 0, 0))