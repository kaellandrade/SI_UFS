from math import floor

'''
Estrutura Heap
'''


class HeapMax:
    def __init__(self, A) -> None:
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
        return self.heapSize + 1

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
        if (l <= self.heapSize and self.heapMax[l] > self.heapMax[i]):
            maior = l
        else:
            maior = i
        if(r <= self.heapSize and self.heapMax[r] > self.heapMax[maior]):
            maior = r
        if (maior != i):
            self.heapMax[i], self.heapMax[maior] = self.heapMax[maior], self.heapMax[i]
            self.maxHeapify(maior)

    def __buildMaxHeap(self, A):  # O(n)
        for i in range(floor(self.heapSize/2), -1, -1):
            self.maxHeapify(i)
        return A
    '''
        TODO:Ajustar aqui
    '''
    def heapSort(A):
        heapSort = HeapMax(A)
        for i in range(len(A)-1, 0, -1):  # O(nlogn)
            A[0], A[i] = A[i], A[0]
            heapSort.heapSize -= 1
            heapSort.maxHeapify(0)
        return heapSort
    '''
        Remove o elemento do Heap e atualizando o Heap
    '''
    @property
    def popFisrt(self):
        elemento = self.heapMax.pop(0)
        self.heapSize -= 1
        self.maxHeapify(0)
        return elemento


print(HeapMax.heapSort([2,1]))
# h = HeapMax([0, 10, -1, 40, 100, 200])