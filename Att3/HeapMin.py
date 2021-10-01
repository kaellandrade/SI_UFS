from math import floor, inf

'''
Estrutura Heap
'''


class HeapMin:
    def __init__(self, A=[]) -> None:
        self.heapSize = len(A) - 1
        self.heapMin = A
        self.__buildMinHeap(self.heapMin)

    def __str__(self):
        return str(self.heapMin)
    '''
        Retorna o filho esquerdo
    '''
    @property
    def getHeapSize(self):
        return self.heapSize

    def parent(self, i):
        return floor(i/2)

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
        if (l <= self.getHeapSize and self.heapMin[l] < self.heapMin[i]):
            maior = l
        else:
            maior = i
        if(r <= self.getHeapSize and self.heapMin[r] < self.heapMin[maior]):
            maior = r
        if (maior != i):
            self.heapMin[i], self.heapMin[maior] = self.heapMin[maior], self.heapMin[i]
            self.minHeapify(maior)

    def __buildMinHeap(self, A):  # O(n)
        for i in range(floor(self.heapSize/2), -1, -1):  # O(n/2)
            self.minHeapify(i)  # O(n/2 * logn)
        return A

    def heapMin(self):
        return self.heapMin[0]

    def heap_extract_min(self):
        if(self.getHeapSize < 0):
            return 'Erro Heap Vazio!'
        maior = self.heapMin[0]
        self.heapMin[0] = self.heapMin[self.getHeapSize]
        self.heapSize -= 1
        self.minHeapify(0)
        return maior

    def heap_increse_key(self, i, key):
        if (key[0][0] < self.heapMin[i]):
            return "Error! Nova chave é menor que chave atual!"
        self.heapMin[i] = key
        while (i > 0 and self.heapMin[self.parent(i)] > self.heapMin[i]):
            self.heapMin[i], self.heapMin[self.parent(
                i)] = self.heapMin[self.parent(i)], self.heapMin[i]
            i = self.parent(i)

    def push(self, key):
        self.heapSize += 1
        self.heapMin.append(key)
        self.heapMin[self.heapSize] = -inf
        self.heap_increse_key(self.getHeapSize, key)


hepmin = HeapMin([])

# print(hepmin)
# hepmin.heap_extract_min()
# hepmin.heap_extract_min()
# hepmin.heap_extract_min()
# hepmin.heap_extract_min()
# hepmin.heap_extract_min()
# hepmin.heap_extract_min()
# hepmin.heap_extract_min()
# hepmin.heap_extract_min()
# hepmin.heap_extract_min()
# print(hepmin.heap_extract_min())

