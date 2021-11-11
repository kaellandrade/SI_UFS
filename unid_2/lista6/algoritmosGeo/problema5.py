from FramWorkGeometria import Point, Poligno


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


def calculaSlope(points: list) -> list:
    points[1].slope = (points[1].y-points[0].y)/(points[1].x-points[0].x)
    slopeMin = points[1].slope
    for i in range(2, len(points)):
        points[i].slope = (points[i].y-points[0].y)/(points[i].x-points[0].x)
        if(points[i].slope < slopeMin):
            slopeMin = points[i].slope
    return slopeMin


def polignoSimple(points: list):
    IndexPointExtre = pontoExtremo(points)
    points[0], points[IndexPointExtre] = points[IndexPointExtre], points[0]  # Trocando
    minSlope = calculaSlope(points)
    points[0].slope = minSlope - 10  # ??

    # ordeneSlope(points) ->  Ordene os slope
    # TODO: Adaptar HeapSort
    #TODO: Tratar o caso com pontos o mesmo valor X
    points.sort(key=lambda point: point.slope)
    return points


C = Point(16, 8, 'C')
D = Point(14, 8, 'D')
A = Point(12, 4, 'A')
G = Point(14, 10, 'G')
F = Point(10, 8, 'F')
E = Point(14, 6, 'E')
I = Point(8,  6, 'I')
H = Point(8, 10, 'H')
B = Point(17, 6, 'B')


points = [C, D, A, G, F, E, I, H, B]

res = polignoSimple(points)

print(list(map(str, res)))
