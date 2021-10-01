from math import floor

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

    '''
        Remove o elemento do Heap e atualizando o Heap
    '''

    def popFisrt(self):
        elemento = self.heapMax[0]
        self.heapMax[0], self.heapMax[self.getHeapSize] = self.heapMax[self.getHeapSize], self.heapMax[0]
        self.heapSize -= 1
        self.rearanjeMaxHeap(self.getHeapSize)

        return elemento

    def push(self, elemento):
        self.heapMax.insert(0, elemento)
        self.heapSize += 1
        filho = self.getHeapSize
        pai = self.heapSize % 2
        while(pai >= 1):
            if(self.heapMax[pai] < self.heapMax[filho]):
                self.heapMax[pai], self.heapMax[filho] = self.heapMax[filho], self.heapMax[pai]
                filho = pai
                pai = pai % 2
            else:
                pai = 0

    def rearanjeMaxHeap(self, n):
        pai = 0
        filho = 1
        while(filho <= n-1):
            if(self.heapMax[filho] < self.heapMax[filho + 1]):
                filho += 1
            if(self.heapMax[filho] > self.heapMax[pai]):
                self.heapMax[pai], self.heapMax[filho] = self.heapMax[filho], self.heapMax[pai]
                pai = filho
                filho = 2 * filho
            else:
                filho = n


h = HeapMax([4, 3, 2, 1, 1000])
print(h.heapSort())
