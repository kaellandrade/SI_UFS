'''
Encontra o maior valor em um vetor X com n elementos.
'''
def maiorValor(x: list, n: int, maior: int) -> int:
    if n == 0:
        return maior
    elif(x[n-1] >= maior):
        return maiorValor(x, n-1, x[n-1])
    else:
        return maiorValor(x, n-1, maior)


def maior(arrayX: list):
    return maiorValor(arrayX, len(arrayX)-1, arrayX[len(arrayX)-1])


print(maior([1000, 2, 30, 400, 5, 2, 3, 4, 5, 600, 7, 8, 9, 0, 100]))
