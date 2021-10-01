from math import floor, inf

'''
Estrutura Heap
'''
class HeapMax:
    def __init__(self, A=[]) -> None:
        self.heapSize = len(A) - 1
        self.heapMax = A
        self.__buildMaxHeap(self.heapMax)

    def __str__(self):
        return str(self.heapMax)
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

    def maxHeapify(self, i) -> None:  # O(logn)
        l = self.left(i)
        r = self.right(i)
        if (l <= self.getHeapSize and self.heapMax[l] > self.heapMax[i]):
            maior = l
        else:
            maior = i
        if(r <= self.getHeapSize and self.heapMax[r] > self.heapMax[maior]):
            maior = r
        if (maior != i):
            self.heapMax[i], self.heapMax[maior] = self.heapMax[maior], self.heapMax[i]
            self.maxHeapify(maior)

    def __buildMaxHeap(self, A):  # O(n)
        for i in range(floor(self.heapSize/2), -1, -1):  # O(n/2)
            self.maxHeapify(i)  # O(n/2 * logn)
        return A
    '''
        TODO:Ajustar aqui
    '''

    def heapSort(self):
        for i in range(self.getHeapSize, 0, -1):  # O(nlogn)
            self.heapMax[0], self.heapMax[i] = self.heapMax[i], self.heapMax[0]
            self.heapSize -= 1
            self.maxHeapify(0)
        return self.heapMax
    
    def heapMaximo(self):
        return self.heapMax[0]
    
    def heap_extract_max(self):
        if(self.getHeapSize < 0):
            return 'Erro Heap Vazio!'
        maior = self.heapMax[0]
        self.heapMax[0] = self.heapMax[self.getHeapSize]
        self.heapSize -= 1
        self.maxHeapify(0)
        return maior

    def heap_increse_key(self, i, key):
        if (key < self.heapMax[i]):
            "Error! Nova chave é menor que chave atual!"
        self.heapMax[i] = key
        while (i > 0 and self.heapMax[self.parent(i)] < self.heapMax[i]):
            self.heapMax[i], self.heapMax[self.parent(i)] = self.heapMax[self.parent(i)], self.heapMax[i]
            i = self.parent(i)

    def push(self, key):
        self.heapSize += 1
        self.heapMax.append(-inf)
        self.heap_increse_key(self.getHeapSize, key)









