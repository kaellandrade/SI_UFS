from FramWorkGeometria import Point, Poligno
from funcoesUtil import intersecaoSegmento


def pontoNoPoligno(P: Poligno, q: Point):
    '''
    ENTRADA: Um popolígno P representado por um vetor de coordenadas de 
    de seus vértices e um ponto q.

    SAÍDA: True caso q esteja contido em P e False caso contrário.
    OBS: Devemos ficar a tentos aos casos epeciais que não está contemplado aqui.
    '''

    # Pegando um ponto qualquer fora do poligno
    r: float = max(P, key=lambda point: point.x).x
    s: float = max(P, key=lambda point: point.y).y

    pFora: Point = Point(r+1, s+1)  # Ponto fora
    # Compuntando interseções
    cont = 0
    for i in range(len(P)-1):
        if(intersecaoSegmento(q, pFora, P[i], P[i+1])):
            cont += 1
    if(cont % 2 == 0):
        return False
    else:
        return True


A = Point(12, 4)
B = Point(16, 6)
C = Point(16, 8)
D = Point(14, 8)
E = Point(14, 6)
F = Point(10, 8)
G = Point(14,10)
H = Point(8, 10)
I = Point(8,  6)

J = Point(15, 7)

polignoDoido = Poligno([A, B, C, D, E, F, G, H, I])

print(pontoNoPoligno(polignoDoido.poligno, J))
