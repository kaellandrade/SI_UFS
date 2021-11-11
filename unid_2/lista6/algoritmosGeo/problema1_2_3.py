from FramWorkGeometria import Point
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


def direcao(v: Point, w: Point, z: Point) -> float:
    return (z.x - v.x) * (w.y - v.y) - (w.x - v.x) * (z.y - v.y)


def noSeguimento(v: Point, w: Point, z: Point) -> bool:
    menorX = min(v.x, w.x)
    menorY = min(v.y, w.y)

    maiorX = max(v.x, w.x)
    maiorY = max(v.y, w.y)

    if((menorX <= z.x) and (z.x <= maiorX) and (menorY <= z.y) and (z.y <= maiorY)):
        return True
    else:
        return False


def intersecaoSegmento(p: Point, q: Point, r: Point, s: Point) -> bool:
    '''
    Entrada: Pontos dos segmentos pq e rs
    SAÍDA: True se pq e rs inteceptam, False caso contrário.
    Complexidade O(1)
    '''
    # calcula a orientação relativa de um extremo ao outro segmento
    dp = direcao(r, s, p)
    dq = direcao(r, s, q)
    dr = direcao(p, q, r)
    ds = direcao(p, q, s)
    if((dp > 0 and dq < 0) or (dp < 0 and dq > 0)) and ((dr > 0 and ds < 0) or (dr < 0 and ds > 0)):
        return True
    else:
        if(dp == 0 and noSeguimento(r, s, p)):
            return True
        elif (dq == 0 and noSeguimento(r, s, q)):
            return True
        elif (dr == 0 and noSeguimento(p, q, r)):
            return True
        elif (ds == 0 and noSeguimento(p, q, s)):
            return True
        else:
            return False


# A = Point(4, 6)
# B = Point(8, 2)
# C = Point(6, 4)
# D = Point(4, 2)

# E = Point(10, 8)
# F = Point(14, 4)
# G = Point(8, 8)
# H = Point(10, 10)

# print(intersecaoSegmento(A, B, C, D))
# print(intersecaoSegmento(E, F, G, H))
