'''
Recebe um vetor x e seu respectivo e tamanho.
'''
def maiorValor(x: list, n: int, maior: int) -> int:
    if n == 0:
        return maior
    if(x[n-1] >= maior):
        return maiorValor(x, n-1, x[n-1])
    else:
        return maiorValor(x, n-1, maior)


arrayX = [100, 3,1000, 0, 500]
print(maiorValor(arrayX, len(arrayX)-1,  arrayX[len(arrayX)-1]))