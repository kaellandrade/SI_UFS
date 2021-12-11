from FramWorkGeometria import Point
from funcoesUtil import intersecaoSegmento
from problema5 import polignoSimple

# Testando intersecaoSegmento
A = Point(4, 6)
B = Point(8, 2)
C = Point(6, 4)
D = Point(4, 2)

E = Point(10, 8)
F = Point(14, 4)
G = Point(8, 8)
H = Point(10, 10)

print(intersecaoSegmento(A, B, C, D))
print(intersecaoSegmento(E, F, G, H))

