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


def findIntesec(Pl1: Point, Pr1: Point, Pl2: Point, Pr2: Point):
    x_dir = min(Pr1.x, Pr2.x)
    x_esq = max(Pl1.x, Pl2.x)

    y_dir = min(Pr1.y, Pr2.y)
    y_esq = max(Pl1.y, Pl2.y)

    if(x_dir - x_esq > 0 and y_dir - y_esq > 0):
        return [(Point(x_esq, y_esq), Point(x_dir, y_dir))]
    return []


def mergeIntersec(L):
    n = len(L)
    # Tratando os casos bases.
    if(n == 1):
        return []
    if(n == 2):
        retangulo1: tuple = L[0]
        retangulo2: Point = L[1]
        return findIntesec(retangulo1[0], retangulo1[1], retangulo2[0], retangulo2[1])

    meio = len(L)//2
    left_recs = mergeIntersec(L[:meio])
    right_recs = mergeIntersec(L[meio:])

    return merge_lines(left_recs, right_recs)


def merge_lines(left, right):
    n_l, n_r = len(left), len(right)
    p_l = p_r = 0

    saida = []

    def append_skyline(p, lst, n):
        while p < n:
            p1 = lst[p][0]
            p2 = lst[p][1]
            p += 1
            saida.append((p1, p2))

    while p_l < n_l and p_r < n_r:
        # Captura os primeiros pontos superior de dois horizontes.
        rec_l, rec_r = left[p_l], right[p_r]

        teste = findIntesec(rec_l[0], rec_l[1], rec_r[0], rec_r[1])
        if(teste):
            saida.append(teste[0])
            p_l+=1
        else:
            saida.append(rec_r)
            p_r += 1

    append_skyline(p_l, left, n_l)
    append_skyline(p_r, right, n_r)

    return saida


# ----------Teste------------
p1: Point = Point(2, 2, 'Pl1')
p2: Point = Point(5, 7, 'Pr1')

p3: Point = Point(3, 4, 'Pl2')
p4: Point = Point(6, 9, 'Pr2')

p5: Point = Point(4, 8, 'Pl3')
p6: Point = Point(8, 10, 'Pr3')

retangulos = [(p1, p2), (p3, p4), (p5, p6)]

for point in mergeIntersec(retangulos):
    print(point)
