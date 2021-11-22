#!python3.8
from algoritmosGeo.metodo_graham import graham
from algoritmosGeo.FramWorkGeometria import Point
from algoritmosGeo.problema4 import pontoNoPoligno
import sys
sys.path.insert(0, '../algoritmosGeo')


A = Point(3, 3, 'A')
B = Point(4, 5, 'B')
C = Point(7, 5, 'C')
D = Point(7, 3, 'D')
E = Point(5, 1, 'E')
F = Point(5, 4, 'F')
G = Point(4, 3, 'G')
H = Point(9, 1, 'H')
profund = dict()
poligno = list([A, B, C, D, E, F, G, H])


def profundidadePontos():
    profundidade = 0
    while poligno:
        envoltoria = graham(poligno).poligno
        for point in envoltoria:
            if(point != None):
                poligno.remove(point)
                profund.setdefault(point.r, profundidade)
        profundidade += 1
    return profund


print(profundidadePontos())
