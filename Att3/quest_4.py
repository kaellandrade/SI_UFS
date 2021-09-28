from math import floor

'''
Estrutura Heap
'''


class HeapMax:
    def __init__(self, A, key=lambda item: item) -> None:
        self.heapSize = len(A) - 1
        self.heapMax = A
        self.__buildMaxHeap(self.heapMax, key)

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

    def maxHeapify(self, i, key) -> None:  # O(logn)
        l = self.left(i)
        r = self.right(i)
        if (l <= self.heapSize and key(self.heapMax[l]) > key(self.heapMax[i])):
            maior = l
        else:
            maior = i
        if(r <= self.heapSize and key(self.heapMax[r]) > key(self.heapMax[maior])):
            maior = r
        if (maior != i):
            self.heapMax[i], self.heapMax[maior] = self.heapMax[maior], self.heapMax[i]
            self.maxHeapify(maior, key)

    def __buildMaxHeap(self, A, key):  # O(n)
        for i in range(floor(self.heapSize/2), -1, -1):  # O(n/2)
            self.maxHeapify(i, key)  # O(n/2 * logn)
        return A
    '''
        TODO:Ajustar aqui
    '''
    def heapSort(A, key=lambda item: item):
        heapSort = HeapMax(A, key)
        for i in range(len(A)-1, 0, -1):  # O(nlogn)
            A[0], A[i] = A[i], A[0]
            heapSort.heapSize -= 1
            heapSort.maxHeapify(0, key)
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


a = [('sorting', 70), ('heapsort', 200), ('heapsort', 100), ('sorting', 190), ('tree', 80),
     ('sorting', 90), ('heap', 60), ('list', 30), ('tree', 50)]

def contabiliza(palavra_pagina: tuple):
    dici = {}
    HeapMax.heapSort(palavra_pagina, key=lambda item:item[1])
    for palavra, pagina in a:
        if(dici.get(palavra) != None):
            dici[palavra].append(pagina)
        else:
            dici[palavra] = [pagina]
    return dici


def imprime(dict):
    palavra_pagina = []
    for item in dict:
        palavra_pagina.append((item, dict[item]))

    HeapMax.heapSort(palavra_pagina, key=lambda x:x[1])

    for palavra, paginas in palavra_pagina:
        print(f'{palavra}   {str(paginas)[1:-1]}')


imprime(contabiliza(a))
