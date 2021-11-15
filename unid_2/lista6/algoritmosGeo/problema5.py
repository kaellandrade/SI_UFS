from FramWorkGeometria import Point
from funcoesUtil import PolignoSimples
#Testando função de criar poligno simples
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

res = PolignoSimples(points)
print(res)