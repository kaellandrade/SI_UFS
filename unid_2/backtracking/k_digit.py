#!python3.8
DIGITS = 10
def k_digit(k: int) -> list:
    resposta = []
    nk(0, k, resposta)


def nk(i: int, k: int, resposta: list) -> int:
    resposta.append(i)
    for j in range(0, DIGITS):
        if(i==9):
            exit()
        else:
            nk(i+1, k, resposta)


def verificaSoma(numeros: list) -> bool:
    '''
    ENTRADA: Recebe uma lista de números e verifica se a soma
    das posições pares equivale a soma das posições ímpares.
    SAÍDA: True caso essa soma seja igual, ou False caso contrário.
    '''
    soma_dos_pares = 0
    soma_dos_impares = 0
    for i in range(len(numeros)):
        if(i % 2 == 0):
            soma_dos_pares += numeros[i]
        else:
            soma_dos_impares += numeros[i]
    return soma_dos_impares == soma_dos_pares


k_digit(2)
