def trocaPosicao(lista: list) -> list:
    for i in range(1, len(lista)):
        if(i % 2 == 0):  # Par
            if(lista[i] > lista[i-1]):
                lista[i-1], lista[i] = lista[i], lista[i-1]
        else:  # ímpar
            if(lista[i] < lista[i-1]):
                lista[i-1], lista[i] = lista[i], lista[i-1]

    return lista


def trocaPosicao2(lista: list) -> list:
    copia = [item for item in lista]
    copia.sort()
    esq = 0
    dir = len(lista) - 1
    for i in range(len(lista)):
        if(i+1) % 2 == 0:
            lista[i] = copia[dir]
            dir = dir-1
        else:
            lista[i] = copia[esq]
            esq = esq+1
    return lista


print(trocaPosicao([9,5, 8, 2, 6]))
print(trocaPosicao2([9,5, 8, 2, 6]))
