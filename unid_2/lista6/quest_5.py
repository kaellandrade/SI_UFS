#!python3.8
from algoritmosGeo.FramWorkGeometria import Point
import sys
sys.path.insert(0, '../algoritmosGeo')


def calcAreaRetangulo(Pl: Point, Pr: Point):
    '''
    ENTRADA: Dois pontos representando os lados extremos de um retângulo.
    Paralelo aos eixos XY
    SAÍDA: Área do retângulo.
    '''
    return abs(Pl.x - Pr.x) * abs(Pl.y - Pr.y)


def calcAreaSobreposicaoRetangulo(Pl1: Point, Pr1: Point, Pl2: Point, Pr2: Point):
    '''
    ENTRADA: Dois retângulos representado por seus pontos extremos esq e dir.
    os retângulos podem sobrepor um ao outro.
    OBS:Retângulos são paralelos aos eixos.
    SAÍDA: Calculo da área.
    '''
    retang1: float = calcAreaRetangulo(Pl1, Pr1)
    retang2: float = calcAreaRetangulo(Pl2, Pr2)

    intersec_area = 0
    dist_x_intersecao = min(Pr1.x, Pr2.x) - max(Pl1.x, Pl2.x)
    dist_y_intersecao = min(Pr1.y, Pr2.y) - max(Pl1.y, Pl2.y)

    if(dist_x_intersecao > 0 and dist_y_intersecao > 0):
        intersec_area = dist_x_intersecao*dist_y_intersecao

    return (retang1+retang2) - intersec_area


def findTotalAreaUnion(L) -> float:
    n = len(L)
    # Tratando os casos bases.
    if(n == 0):
        return 0
    if(n == 1):
        unicoRetangulo:tuple = L[0]
        return calcAreaRetangulo(unicoRetangulo[0], unicoRetangulo[1])

    # Para Ns prédios
    # meio = len(L)//2
    # left_area = findSkyline(L[:meio])
    # right_area = findSkyline(L[meio:])

    # Combinando as soluções
    # return merge_lines(left_skyline, right_skyline)


# ----------Teste------------
p1: Point = Point(2, 2, 'Pl1')
p2: Point = Point(5, 7, 'Pr1')

p3: Point = Point(3, 4, 'Pl2')
p4: Point = Point(6, 9, 'Pr2')


print(findTotalAreaUnion([(p1, p2)]))
