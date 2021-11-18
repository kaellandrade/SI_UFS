#!python3.8
from typing import List
from algoritmosGeo.FramWorkGeometria import Point
from MaxHeap import MaxHeap
import sys
sys.path.insert(0, '../algoritmosGeo')


def comparador(hl, l, i):
    if(hl[l].y > hl[i].y):
        return l
    elif(hl[l].y < hl[i].y):
        return i
    else:
        if(hl[l].x >= hl[i].x):
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
    # TODO: Retirar a restrinção de coordenadas iguais (Adaptar Heap)
    points = MaxHeap(points, comparador).heapSort()
    points.reverse()
    # return points
    # pointsCopy = points.heap_list[1:]
    # return points
    points_maxi = []

    pointMax = points.pop(0)

    points_maxi.append(pointMax)

    for point in points:
        if(point.x >= pointMax.x):
                points_maxi.append(point)
    return points_maxi


lista_pontos = [Point(2,4), Point(4,4),Point(5,3), Point(7,4)]
list(map(print, novaSolucao(lista_pontos)))
# novaSolucao(lista_pontos)

# --------------------------------------------------------


# // TODO: Criar função pontoDomina
# !DICA: Pode precisar usar algoritmo de ordenação
# !DICA: Pensar em uma solução por indução(Fraca)
# !DICA: Talve os mergesort seja uma boa ideia
