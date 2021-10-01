from math import floor

'''
Minha estrutura Heap
'''


class HeapMin:
    def __init__(self, A=[]) -> None:
        self.__heapSize = len(A)
        self.__heapMin = A
        self.__buildMinHeap(self.__heapMin)
 

    def left(self, i):
        return 2*i + 1  # Pois começamos do 0 aqui

    '''
        Retorna o filho direito
    '''

    def right(self, i):
        return 2*i+2

''''''
def k_merge(arrays):
    minHeap = HeapMin()  # Criando meu MinHeap
    arrOrd = []

    for i in range(len(arrays)):
        #Vamos armazenar no Heap uma tupla do tipo (primeiro_valor, index_do_seu_array)
        minHeap.push((arrays[i].pop(0), i))

    while(minHeap.getHeapSize):
        elemento = minHeap.popMin
        arrOrd.append(elemento[0])

        if (arrays[elemento[1]]):
            minHeap.push((arrays[elemento[1]].pop(0), elemento[1]))

    return arrOrd

''''''
# print(k_merge(
#     [
#         [0],
#         [1],
#         [0,2,3,4],
#         [-1]
#     ]
# ))

hep = HeapMin([i for i in range(5, -1,-1)])
while(hep.getHeapSize):
    print(hep.popMin)