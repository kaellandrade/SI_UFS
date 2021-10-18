import sys
sys.path.insert(0, '../SI_UFS/algoritmosPrimeiraProva')

from outros.MinHeap import MinHeap

def k_merge(arrays):
    minHeap = MinHeap()  # Criando meu MinHeap
    arrOrd = []

    for i in range(len(arrays)):
        # Vamos armazenar no Heap uma tupla do tipo (primeiro_valor, index_do_seu_array)
        minHeap.insert((arrays[i].pop(0), i))

    while(minHeap.current_size):
        tupla = minHeap.heap_extract_min()

        elemento = tupla[0]  # Extraindo o valor
        index = tupla[1]  # Extraindo o index
        arrOrd.append(elemento)
        # Se existir elemeto no array do elemento que acabou de ser removido
        if (arrays[index]):
            minHeap.insert((arrays[index].pop(0), index))

    return arrOrd


print(k_merge([
    [10, 20, 30, 40, 60],
    [0, 2, 3, 4, 5, 6, 7, 8],
    [9, 11, 12, 13, 14, 15, 16, 17, 18, 19]
]))
