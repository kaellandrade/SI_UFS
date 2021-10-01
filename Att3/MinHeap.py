"""
Heap min Em Python
"""
from math import floor

class MinHeap:
    def __init__(self, arr=[]):
        """
        Nesta implementação o Heapinicializa com um valor;
        """
        self.heap_list = [None]+arr
        self.current_size = len(arr)
        #Monta nosso Heap
        for i in range(floor(len(self.heap_list)/2),0,-1):
            self.min_heapify(i)

    def getMin(self):
        if(self.current_size == 0):
            return 'Vazio!'
        return self.heap_list[1]
    
    def parent(self, i):
        return i//2

    def left(self, i):
        '''
            Retorna o filho Esquerdo
        '''
        return 2*i
            
    def right(self, i):
        '''
            Retorna o filho direito
        '''
        return (2*i)+1
    def heap_increse_key(self, i):
        """
        Move o valor para cima para manter a propriedade do heapFy.
        """
        # Rearanjando os elementos.
        while self.parent(i) > 0:
            # Se o elemento for menorque seu pai. Então troque.
            if (self.heap_list[i] < self.heap_list[self.parent(i)]):
                self.heap_list[i], self.heap_list[self.parent(i)] = self.heap_list[self.parent(i)], self.heap_list[i]
            # Move o index para o pai para manter a propriedade.
            i = self.parent(i)
 
    def insert(self, k):
        """
        Insere um valor no nosso Heap
        """
        # Inserindo o novo valor.
        self.heap_list.append(k)
        # Incrementando o tamanho do heap.
        self.current_size += 1
        # Movendo o elemento de sua posição de baixo para cima.
        self.heap_increse_key(self.current_size)
 
    def min_heapify(self, i):
        '''
            Mantém a propriedade Heap.
        '''
        l = self.left(i)
        r = self.right(i)
        if(l <= self.current_size and self.heap_list[l] < self.heap_list[i]):
            menor = l
        else:
            menor = i
        if(r<= self.current_size and self.heap_list[r] < self.heap_list[menor]):
            menor = r
        if menor != i:
            self.heap_list[i], self.heap_list[menor] = self.heap_list[menor], self.heap_list[i]
            self.min_heapify(menor)

    def heap_extract_min(self):
        '''
            Extrai o valor mínimo  do Heap
        '''
        if len(self.heap_list) == 1:
            return 'Heap Vazio!'
 
        # Pegando a raiz do heap. (O menor valor)
        root = self.heap_list[1]
 
        # Move o último valor do Heap para raiz.
        self.heap_list[1] = self.heap_list[self.current_size]
 
        # Removendo o último valor, pois fizemos uma cópia para raiz.
        *self.heap_list, _ = self.heap_list
 
        # Diminuindo o tamanho do heap
        self.current_size -= 1
 
        # Mantendo a propriedade heap
        self.min_heapify(1)
 
        # retornando o menor valor
        return root
