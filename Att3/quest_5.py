#!python3
from HeapMin import HeapMin
from dados_ordenados import cadastro


def k_merge(arrays):
    minHeap = HeapMin([], key=lambda tupla: tupla[0])  # Criando meu MinHeap
    arrOrd = []

    for i in range(len(arrays)):
        # Vamos armazenar no Heap uma tupla do tipo (primeiro_valor, index_do_seu_array)
        minHeap.push((arrays[i].pop(0), i))

    while(minHeap.getHeapSize):
        tupla = minHeap.popMin

        elemento = tupla[0]  # Extraindo o valor
        index = tupla[1]  # Extraindo o index

        arrOrd.append(elemento)

        # Se existir elemeto no array do elemento que acabou de serremovido
        if (arrays[index]):
            minHeap.push((arrays[index].pop(0), index))

    return arrOrd


def verifyOrder(array: list, key=lambda item: item) -> bool:
    for i in range(1, len(array)):
        if(key(array[i-1]) > key(array[i])):
            print(key(array[i-1]), key(array[i]))
            return False
    return True


# res = k_merge(cadastro)
# print(verifyOrder(res, key=lambda item: item[0]))

heap = HeapMin([item for item in range(10, -1, -1)])
while(heap.getHeapSize):
    print(heap.popMin)
