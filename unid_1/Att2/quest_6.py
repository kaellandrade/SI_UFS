def trocaZeros(lista):
    ultimaPosicao = len(lista) - 1

    for i in range(len(lista)):
        if(lista[i] == 0 and i < ultimaPosicao):
            while(lista[ultimaPosicao] == 0 and ultimaPosicao != -1):
                ultimaPosicao -= 1
            if(i <= ultimaPosicao):
                lista[i], lista[ultimaPosicao] = lista[ultimaPosicao], lista[i]

    return lista

def trocaZeros2(lista):
    contador = 0;

    for i in range(len(lista)):
        if(lista[i] != 0):
            lista[contador] =lista[i]
            contador += 1
    for i in range(contador, len(lista)):
        lista[i]= 0
    
    return lista
    
print(trocaZeros([0,1,0,1]))
print(trocaZeros2([0,1,0,1]))