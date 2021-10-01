from MinHeap import MinHeap


def k_esimo_menor(vetor: list, k:int) -> int:
    heapmin = MinHeap(vetor)
    for _ in range(1, k):
        if(heapmin.current_size):
            heapmin.heap_extract_min()
    return heapmin.getMin()

print(k_esimo_menor([100, 1, 0, -2], 2))
