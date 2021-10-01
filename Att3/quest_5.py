#!python3
from HeapMin import MinHeap
from dados_ordenados import cadastro


def k_merge(arrays):
    minHeap =MinHeap()  # Criando meu MinHeap
    arrOrd = []

    for i in range(len(arrays)):
        # Vamos armazenar no Heap uma tupla do tipo (primeiro_valor, index_do_seu_array)
        minHeap.insert((arrays[i].pop(0), i))

    while(minHeap.current_size):
        tupla = minHeap.heap_extract_min()
        

        elemento = tupla[0]  # Extraindo o valor
        index = tupla[1]  # Extraindo o index
        arrOrd.append(elemento)
        # Se existir elemeto no array do elemento que acabou de serremovido
        if (arrays[index]):
            minHeap.insert((arrays[index].pop(0), index))

    return arrOrd


res = k_merge(cadastro)
print(res)