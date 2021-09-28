from HeapMin import HeapMin


def conecta_fios(fios: list) -> int:
    heapmin = HeapMin(fios)
    custo_total = 0
    conectados = 0
    while(heapmin.getHeapSize > 1):
        conectados = heapmin.popMin + heapmin.popMin
        custo_total += conectados 
        heapmin.push(conectados) #Olog(n)
    return custo_total

print(f'{conecta_fios([2, 4, 8, 4, 5, 3])}x')
