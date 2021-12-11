#!python3.8
from typing import List


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


class Edificio:
    '''
    Classe que representa um edifícil.
    Recebe um ponto extremo esquerdo, ponto extremo direito e sua altura.
    '''

    def __init__(self, PointLeft: Point, Height: float, PointRight: Point) -> None:
        self.PointLeft: Point = PointLeft
        self.PointRight: Point = PointRight
        self.Height: float = Height

    def __str__(self) -> str:
        res: str = f'{self.PointLeft}, {self.Height}, {self.PointRight}'
        return res


def findSkyline(L: List[Edificio]) -> List[Point]:
    '''
    ENTRADA:Conjunto de Edifícios.
    SAÍDA: Linha do horizonte a partir da junçã de todos edifícios.
    '''
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
    left_skyline = findSkyline(L[:meio])
    right_skyline = findSkyline(L[meio:])

    # Combinando as soluções
    return merge_lines(left_skyline, right_skyline)


def merge_lines(left, right):
    '''
    ENTRADA: Conjunto de linhas do horizontes 
    SAÍDA: A mesclage de duas linhas do horizontes que faz parte da 
        solução final.
    '''
    n_l, n_r = len(left), len(right)
    p_l = p_r = 0
    curr_y = left_y = right_y = 0

    saida = []

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
    while p_l < n_l and p_r < n_r:
        # Captura os primeiros pontos superior de dois horizontes.
        point_l, point_r = left[p_l], right[p_r]

        # Capturando o menor x
        if(point_l[0] < point_r[0]):
            x, left_y = point_l  # Foi capturado um ponto da linha do horizonte esq
            p_l += 1
        else:
            x, right_y = point_r
            p_r += 1  # Foi capturando um ponto da linha do horizonte direita.
        # capturando a altura máxima (ou seja, y) entre os dois horizontes.
        max_y = max(left_y, right_y)

        # Caso se houver uma mudança no horizonte
        if(curr_y != max_y):
            atualiza_saida(x, max_y)
            curr_y = max_y
    append_skyline(p_l, left, n_l, curr_y)
    append_skyline(p_r, right, n_r, curr_y)

    return saida

# Testando: Edifício(PONTO_ESQ, ALTURA, PONTO_DIR)
ed1 = Edificio(Point(3, 0, 'L'), 9.0, Point(7, 0, 'R'))
ed2 = Edificio(Point(6, 0,  'L'), 7, Point(10, 0,  'R'))
ed3 = Edificio(Point(8, 0,  'L'), 6, Point(9, 0, 'R'))
ed4 = Edificio(Point(11, 0,  'L'), 10, Point(12, 0, 'R'))

edificios = [ed1, ed2, ed3, ed4]
print(findSkyline(edificios))
