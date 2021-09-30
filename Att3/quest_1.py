from HeapMin import HeapMin


def k_esimo_menor(vetor: list, k:int) -> int:
    heapmin = HeapMin(vetor)
    for _ in range(1, k):
        if(heapmin.getHeapSize):
            heapmin.popMin
    return vetor[0]

print(k_esimo_menor([100, 1, 0, -2], 4))
