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


class Poligno:
    '''
        Classe que representa um poligno dada uma 
        sequencia de pontos [p1, p2, p3, p1]
    '''

    def __init__(self, points: list) -> None:
        self.poligno = points

    def __str__(self) -> str:
        print('Sua sequência para formar o poligno é: ')
        res: str = ''
        for point in self.poligno:
            res += f'\n{str(point)}'
        return res


class PolignoSimples(Poligno):  # Poligno Simples extende de Poligno

    '''
        Entrada: Recebe uma lista de pontos em qualquer ordem.
        SAÍDA: Uma sequencia representando um poligno simples
    '''

    def __init__(self, points: list) -> None:
        super().__init__(points)

        IndexPointExtre = pontoExtremo(points)
        # Trocando
        points[0], points[IndexPointExtre] = points[IndexPointExtre], points[0]
        minSlope = calculaSlope(points)
        points[0].slope = minSlope - 10
        points.sort(key=lambda point: point.slope)

# Conjunto de funções úteis para ser usadas


def orientacaoSegmento(p: Point, q: Point, r: Point) -> int:
    '''
    Entrada: Pontos dos segmentos pq e pr
    SAÍDA: -1, se pq for anti-horário em relação a pr,
    0 caso sejem colinear e 1 no sentido horário
    Complexidade O(1)
    TODO: Perguntar se não precisaria inserir o sinal -
    '''
    prodVetorial = -((q.x - p.x) * (r.y-p.y) - (r.x - p.x) * (q.y-p.y))
    if(prodVetorial == 0):
        return 0
    elif(prodVetorial > 0):
        return 1
    else:
        return -1


def orientacaoVirada(p: Point, q: Point, r: Point) -> int:
    '''
    Entrada: Pontos dos segmentos pq e pr
    SAÍDA: R caso para ir de pq e qr precise virar a direita
    L caso precise virar a esquerda e S caso for reto.
    '''
    res = orientacaoSegmento(p, q, r)
    if(res == 1):
        return 'R'
    elif (res == -1):
        return 'L'
    else:
        return 'S'


def calculaSlope(points: list) -> list:
    points[1].slope = (points[1].y-points[0].y)/(points[1].x-points[0].x)
    slopeMin = points[1].slope
    for i in range(2, len(points)):
        points[i].slope = (points[i].y-points[0].y)/(points[i].x-points[0].x)
        if(points[i].slope < slopeMin):
            slopeMin = points[i].slope
    return slopeMin


def pontoExtremo(points: list) -> int:
    '''
        ENTRADA: Vetor W de n pontos
        SAÍDA: índice do ponto extremo W
        TODO: Adaptar para outras casos.
    '''
    pointEx = 0
    for i in range(1, len(points)):
        if (points[i].x > points[pointEx].x) or ((points[i].x == points[pointEx].x) and (points[i].y < points[pointEx].y)):
            pointEx = i
    return pointEx


def graham(P: Poligno) -> Poligno:
    '''
    ENTRADA: Conjuntos de pontos em P.
    SAÍDA: Envoltória convexa.
    '''
    # ! Não trata os casos especiais
    P: PolignoSimples = PolignoSimples(P)
    # Aqui ficará minha Envoltória.
    H: Poligno = Poligno([None] * (len(P.poligno) - 3))

    # Inicializando os três primeiros pontos da envoltória.
    H.poligno.insert(0, P.poligno[0])
    H.poligno.insert(1, P.poligno[1])
    H.poligno.insert(2, P.poligno[2])
    m = 2

    for i in range(3, len(P.poligno)):
        while(orientacaoVirada(H.poligno[m-1], H.poligno[m], P.poligno[i]) == 'R'):
            m -= 1
        m += 1
        H.poligno[m] = P.poligno[i]

    return H


# Testando o algoritmos
def profundidadePontos(Pontos: List[Point]) -> dict:
    '''
    ENTRADA: Uma lista de pontos.
    SAÍDA: Um dicionário com a profundiade de cada ponto Ex: {P1:0, P2:2}
    '''
    profundade_pontos = dict()
    nivel_profundidade_atual = 0
    while pontos:
        envoltoria = graham(pontos).poligno
        for point in envoltoria:
            if(point != None):
                pontos.remove(point)
                profundade_pontos.setdefault(point.r, nivel_profundidade_atual)
        nivel_profundidade_atual += 1
    return profundade_pontos


A = Point(3, 3, 'A')
B = Point(4, 5, 'B')
C = Point(7, 5, 'C')
D = Point(7, 3, 'D')
E = Point(5, 1, 'E')
F = Point(5, 4, 'F')
G = Point(4, 3, 'G')
H = Point(9, 1, 'H')

I = Point(5, 3.18, 'I')
J = Point(5.4, 3.48, 'J')
K = Point(5.41782, 3.14704, 'K')

pontos = [A, B, C, D, E, F, G, H, I, J, K]


print(profundidadePontos(pontos))
