from MinHeap import MinHeap


def conecta_fios(fios: list) -> int:
    heapmin = MinHeap(fios)
    custo_total = 0
    conectados = 0
    while(heapmin.current_size > 1):
        conectados = heapmin.heap_extract_min() + heapmin.heap_extract_min()
        custo_total += conectados 
        heapmin.insert(conectados) #Olog(n)

    return custo_total

print(f'{conecta_fios([2, 4, 8, 4, 5, 3])}x')
