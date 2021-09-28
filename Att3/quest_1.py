from HeapMin import HeapMin


def k_esimo_menor(vetor: list) -> int:
    heapmin = HeapMin(vetor)
    if(heapmin.getHeapSize < 1):
        return 'HEAP VAZIA!'
    return heapmin.popMin

print(k_esimo_menor([9,8,7,6,5,4,3,2]))
