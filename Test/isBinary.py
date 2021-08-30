'''
Dada uma string binária contZeroOne verifica
se a quantidade dee 0s é a mesma que a quantidade de 1s;
'''

'''
strBinaria -> arraycom n elementos do tipo char temos n bytes de espaço
lengBinaria consiste no tamanho de strBinaria (int), logo temos 2bytes
'''
def contZeroOne(strBinaria: str, lengbinaria: int) -> bool:
    totalZeros = totalUns = 0  # O(1)
    for char in range(0, lengbinaria):  # O(n) LINEAR
        if strBinaria[char] == '0':  # O(1)
            totalZeros += 1  # O(1)
        else:
            totalUns += 1  # O(1)
    return totalUns == totalZeros  # O(1)

'''
x -> Para um array com n elementos do tipo char temos n bytes de espaço
i, n, qt0 e qt1 são interios logo: 8 bytes
'''
def binary(x: list, i: int, n: int, qt0: int, qt1: int): #O(n)
    if qt1 > qt0:  # O(1)
        return False  # O(1)
    elif (i <= n):  # O(n)
        if(x[i] == '1'):  # O(1)
            return binary(x, i+1, n, qt0, qt1+1)  # O(1)
        else:
            return binary(x, i+1, n, qt0+1, qt1)  # O(1)
    return contZeroOne(x, len(x))  # O(n)


string = '00101'
print(binary(string, 0, len(string)-1, 0, 0))
