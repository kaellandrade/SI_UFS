#!python3.8
from algoritmosGeo.funcoesUtil import PolignoSimples, orientacaoVirada
from algoritmosGeo.FramWorkGeometria import Point, Poligno
import sys
sys.path.insert(0, '../algoritmosGeo')


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
