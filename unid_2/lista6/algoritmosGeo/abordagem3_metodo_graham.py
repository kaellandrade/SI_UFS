from FramWorkGeometria import Point, Poligno
from funcoesUtil import PolignoSimples, orientacaoVirada

# Conjunto de pontos como exemplos
A = Point(3, 1, 'A')
B = Point(4, 2, 'B')
C = Point(5, -1, 'C')
D = Point(3, 2, 'D')
E = Point(2, 3, 'E')
F = Point(1, 0, 'F')

G = Point(5, 4, 'G')
H = Point(6, 3, 'H')
I = Point(8, 1, 'I')
J = Point(7, 3, 'J')


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


print(graham([A, B, C, D, E, F, G, H, I, J]))
