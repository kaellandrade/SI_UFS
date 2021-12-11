#!python3.8
from typing import List


def K_backtracking(n: int, i: int, c: list, m: list[list]) -> None:
    '''
        ENTRADA: Inteiro n representando a quantidade de dígitos.
        inteiro i inicialmente como 0, lista de combicações c, matrix m
        onde será armazenado todos k_dígitos.
    '''
    if(i == n):
        m.append(c.copy())
    else:
        for j in range(0, 10):
            c[i] = j
            K_backtracking(n, i+1, c, m)


def ValidSum(digits: list):
    '''
        ENTRADA: Uma lista de dígitos no formato [n1, n2, n3 ... nk]
        SAÍDA: False caso n1 seja 0 ou a soma dos itens nas posições pares
        forem diferentes da soma das posições ímpares.
    '''
    soma_pares = 0
    soma_impares = 0

    if(digits[0] == 0):
        return False
    for i in range(len(digits)):
        if(i % 2 == 0):
            soma_pares += digits[i]
        else:
            soma_impares += digits[i]
    return soma_impares == soma_pares


def k_digits(n: int) -> list[List]:
    '''
        ENTRADA: Um inteiro N, um inteiro i iniciando em 0 e uma lista c
        representando uma possível combinação.
        SAÍDA: Uma matrix contendo os possíveis k_digítos, tal que a soma
        dos elementos em posições pares é iagual a soma dos elementos nas 
        posições ímapres. Ex: para n=3 -> [[1, 1, 0], [1, 2, 1], [1, 3, 2]...]
    '''
    combinacoes = [0]*n
    matrix_k_digits = []
    K_backtracking(n, 0, combinacoes, matrix_k_digits)
    k_digits_valid = list(map(lambda l: "".join(map(str, l)), filter(ValidSum, matrix_k_digits)))

    return k_digits_valid


print(k_digits(3))
