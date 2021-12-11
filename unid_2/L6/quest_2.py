#!python3.8
from math import floor
from typing import List


def comparador(hl, l, i):
    '''
    Função auxiliar para ser chamada na comparação do Heap.
    ENTRADA: Vetor que está sendo ordenadao, e os indíces dos elementos comparados no heap.
    SAÍDA: O índice da menor coordenada Y e caso tenha duas coordenadas Y captura aquela com menor X
    '''
    if(hl[l].y < hl[i].y):
        return l
    elif(hl[l].y > hl[i].y):
        return i
    else:
        if(hl[l].x <= hl[i].x):
            return l
        else:
            return i


class Point:
    '''
        Classe que representa um ponto (x,y)
    '''

    def __init__(self, x: float, y: float, r: str = 'None') -> None:
        self.x = x
        self.y = y
        self.slope = 0
        self.r = r

    def __str__(self) -> str:
        return f'({self.r}, x={self.x}, y={self.y})'


class Heap:
    def __init__(self, arr=[], key=lambda item: item):
        """
        Nesta implementação o Heapinicializa com um valor;
        """
        self.heap_list = [None]+arr
        self.current_size = len(arr)
        self.key = key
        # Monta nosso Heap
        for i in range(floor(len(self.heap_list)/2), 0, -1):
            self.max_heapify(i)

    def getMax(self):
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

    def heapSort(self):
        for i in range(self.current_size, 1, -1):  # O(nlogn)
            self.heap_list[1], self.heap_list[i] = self.heap_list[i], self.heap_list[1]
            self.current_size -= 1
            self.max_heapify(1)
        return self.heap_list[1:]

    def heap_increse_key(self, i):
        """
        Move o valor para cima para manter a propriedade do heapFy.
        """
        # Rearanjando os elementos.
        while self.parent(i) > 0:
            # Se o elemento for maior que seu pai. Então troque.
            menor = comparador(self.heap_list, i, self.parent(i))
            if(self.heap_list[menor] < self.heap_list[self.parent(i)]):
                self.heap_list[i], self.heap_list[self.parent(
                    i)] = self.heap_list[self.parent(i)], self.heap_list[i]
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

    def max_heapify(self, i):
        '''
            Mantém a propriedade Heap.
        '''
        l = self.left(i)
        r = self.right(i)
        if(l <= self.current_size):
            menor = self.key(self.heap_list, l, i)
        else:
            menor = i

        if(r <= self.current_size):
            menor = self.key(self.heap_list, r, menor)

        if menor != i:
            self.heap_list[i], self.heap_list[menor] = self.heap_list[menor], self.heap_list[i]
            self.max_heapify(menor)

    def heap_extract_max(self):
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
        * self.heap_list, _ = self.heap_list

        # Diminuindo o tamanho do heap
        self.current_size -= 1

        # Mantendo a propriedade heap
        self.max_heapify(1)

        # retornando o menor valor
        return root


def pontosMaximais(points: List[Point]) -> List[Point]:
    '''
        ENTRADA: Conjunto de pontos P.
        SAÍDA: Conjunt M de pontos maximais.
    '''

    # HeapSort em ordem decrescente. Ou seja, maior cordenada Y e caso de empate maior coordenada x
    points = Heap(points, comparador).heapSort()
    points_maxi = []
    pointMax = points.pop(0)
    points_maxi.append(pointMax)

    for point in points:
        if(point.x >= pointMax.x):
            points_maxi.append(point)
    return points_maxi


lista_pontos = [Point(1, 5, 'P1'), Point(2, 4, 'P2'), Point(3, 3, 'P3'),  Point(4, 2, 'P4'),  Point(5, 1, 'P5')]
list(map(print, pontosMaximais(lista_pontos)))
