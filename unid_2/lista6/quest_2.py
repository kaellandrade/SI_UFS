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


def pontoDomina(p: Point, q: Point) -> bool:
    '''
    ENTRADA: Dois pontos p e q
    SAÍDA: True caso p domine q, False caso contrário.

    OBS: Um ponto p domina outro ponto q se ambas as coordenadas x e y de p
    forem maiores ou iguais que as respectivas coordenadas de q
    '''
    return (p.x >= q.x) and (p.y >= q.y)


# Solução ingênua para testes.
def setMaximalQudratica(points: List[Point]) -> List[Point]:
    sets = []
    domina = False
    for point_i in points:
        domina = False
        for point_y in points:
            if(point_i != point_y):
                if(pontoDomina(point_y, point_i)):
                    domina = True
        if(not domina):
            sets.append(point_i)
    return sets


def novaSolucao(points: List[Point]) -> List[Point]:
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
list(map(print, novaSolucao(lista_pontos)))
