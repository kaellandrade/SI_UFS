#!python3.8
from algoritmosGeo.FramWorkGeometria import Point
from typing import List
import sys
sys.path.insert(0, '../algoritmosGeo')

def mergeEdificio(L) -> List[Point]:
    n = len(L)
    # Tratando os casos bases.
    if(n == 0):
        return []
    if(n == 1):
        Pointleft = L[0].PointLeft
        PointRight = L[0].PointRight
        Height = L[0].Height
        return [(Pointleft.x, Height), (PointRight.x, 0)]

    # Para Ns prédios
    meio = len(L)//2
    left_skyline = mergeEdificio(L[:meio])
    right_skyline = mergeEdificio(L[meio:])

    # Combinando as soluções
    return merge_lines(left_skyline, right_skyline)


def merge_lines(left, right):
    def atualiza_saida(x, y):
        # Se a mudança no horizonte não for vertical adiciona o novo ponto.
        if not saida or saida[-1][0] != x:
            saida.append((x, y))
        else:
            saida[-1][1] = y

    def append_skyline(p, lst, n, curr_y):
        while p < n:
            x, y = lst[p]
            p += 1
            if(curr_y != y):
                atualiza_saida(x, y)
                curr_y = y
    n_l, n_r = len(left), len(right)
    p_l = p_r = 0
    curr_y = left_y = right_y = 0

    saida = []

    while p_l < n_l and p_r < n_r:
        # Captura os primeiros pontos superior de dois horizontes.
        point_l, point_r = left[p_l], right[p_r]

        # Capturando o menor x
        if(point_l[0] < point_r[0]):
            x, left_y = point_l #Foi capturado um ponto da linha do horizonte esq
            p_l += 1
        else:
            x, right_y = point_r
            p_r += 1 # Foi capturando um ponto da linha do horizonte direita.
        # capturando a altura máxima (ou seja, y) entre os dois horizontes.
        max_y = max(left_y, right_y)

        #Caso se houver uma mudança no horizonte
        if(curr_y != max_y):
            atualiza_saida(x, max_y)
            curr_y = max_y
    append_skyline(p_l, left, n_l, curr_y)
    append_skyline(p_r, right, n_r, curr_y)

    return saida
