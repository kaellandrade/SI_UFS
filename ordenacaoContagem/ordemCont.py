def contSort(lista: list) -> list:
    V_contador = [0] * (max(lista) + 1)
    V_ordenado = [0] * (len(lista)+1)
    for elemento in lista:
        V_contador[elemento] += 1

    for i in range(1, len(V_contador)):
        V_contador[i] = V_contador[i] + V_contador[i-1]

    for i in range(0, len(lista)):
        index = V_contador[lista[i]]
        V_ordenado[index] = lista[i]
        V_contador[lista[i]] -= 1
    return V_ordenado[1:]


print(contSort([100,1,2,4,0, 40,30,10,1000]))
