from math import floor

'''
Minha estrutura Heap
'''


class HeapMin:
    def __init__(self, A=[]) -> None:
        self.__heapSize = len(A) - 1
        self.__heapMin = A
        self.__buildMinHeap(self.__heapMin)

    def __str__(self):
        return str(self.__heapMin)
    '''
        Retorna o filho esquerdo
    '''
    @property
    def getHeapSize(self):
        return self.__heapSize + 1

    def left(self, i):
        return 2*i + 1  # Pois começamos do 0 aqui

    '''
        Retorna o filho direito
    '''

    def right(self, i):
        return 2*i+2

    '''
    Matém a propriedade Heap-Max
    '''

    def minHeapify(self, i) -> None:  # O(logn)
        l = self.left(i)
        r = self.right(i)
        if (l <= self.__heapSize and self.__heapMin[l] < self.__heapMin[i]):
            maior = l
        else:
            maior = i
        if(r <= self.__heapSize and self.__heapMin[r] < self.__heapMin[maior]):
            maior = r
        if (maior != i):
            self.__heapMin[i], self.__heapMin[maior] = self.__heapMin[maior], self.__heapMin[i]
            self.minHeapify(maior)

    def __buildMinHeap(self, A):  # O(n)
        for i in range(floor(self.__heapSize/2), -1, -1):
            self.minHeapify(i)
        return A

    '''
        Remove o elemento do Heap e atualizando o Heap
    '''
    @property
    def popMin(self):
        elemento = self.__heapMin.pop(0)
        self.__heapSize -= 1
        self.minHeapify(0)
        return elemento
    '''
    Insere um elemento no meu Heap-Min e atualiza.
    '''

    def push(self, elemento):
        self.__heapMin.insert(0, elemento)
        self.__heapSize += 1
        self.minHeapify(0)


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


print(k_merge(
    [
        [2, 6, 12],
        [1, 9],
        [-1000,-1,0]
    ]
))
