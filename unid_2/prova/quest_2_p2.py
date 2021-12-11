#!python3.8
from typing import List
from algoritmosGeo.FramWorkGeometria import Point
import uuid
import sys
sys.path.insert(0, '../algoritmosGeo')
global count
count = 0


class Circle:
    def __init__(self, x: float, r: float) -> None:
        self.ref = str(uuid.uuid4())
        self.cordenadas = [Point(x-r, 0, f'{self.ref} ESQ'), Point(
            x+r, 0, f'{self.ref} DIR')]


def flatList(list: list[List]):
    '''
    Recebe uma lista de listas e retorna todos em uma única lista
    '''
    flat = []
    for lista in list:
        flat += lista.cordenadas
    return flat


def checkInsedCircle(c: Circle, openEvent: dict):
    '''
        Recebe um círculo e todos os segmentos em abertos.
    '''
    for k, v in openEvent.items():
        if(c.ref != v.ref):
            if(c.cordenadas[0].x >= v.cordenadas[0].x and c.cordenadas[1].x <= v.cordenadas[1].x):
                global count
                count += 1


def sweep(list: Point, circles: dict):
    openEvent = {

    }
    for point in list:
        label, side = point.r.split()
        if(side == 'ESQ'):
            openEvent.setdefault(label, circles[label])
        elif(side == 'DIR'):
            checkInsedCircle(circles[label], openEvent)
            openEvent.pop(label)
    return count


C1 = Circle(10, 9)
C2 = Circle(4, 2)
C3 = Circle(20, 5)

circles = {
    C1.ref: C1,
    C2.ref: C2,
    C3.ref: C3,
}


todos_pontos = flatList([C1, C2, C3])
todos_pontos.sort(key=lambda t: t.x)

print(sweep(todos_pontos, circles))
