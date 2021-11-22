#!python3.8
from typing import List
from algoritmosGeo.FramWorkGeometria import Point
from Heap import Heap
import sys
sys.path.insert(0, '../algoritmosGeo')


def comparador(hl, l, i):
    if(hl[l].y < hl[i].y):
        return l
    elif(hl[l].y > hl[i].y):
        return i
    else:
        if(hl[l].x <= hl[i].x):
            return l
        else:
            return i


def pontosMaximais(points: List[Point]) -> List[Point]:
    # ! HeapSort em ordem decrescente. Ou seja, maior cordenada Y e caso de empate maior coordenada x 
    points = Heap(points, comparador).heapSort()
    points_maxi = []
    pointMax = points.pop(0)
    points_maxi.append(pointMax)

    for point in points:
        if(point.x >= pointMax.x):
                points_maxi.append(point)
    return points_maxi


lista_pontos = [Point(2,4), Point(4,4),Point(5,3), Point(6,2)]
list(map(print, pontosMaximais(lista_pontos)))
