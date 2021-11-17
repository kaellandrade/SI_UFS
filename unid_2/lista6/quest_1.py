#!python3.8
from algoritmosGeo.FramWorkGeometria import Point
import sys
sys.path.insert(0, '../algoritmosGeo')

from mergeEdificios import mergeEdificio

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


ed1 = Edificio(Point(3, 0, 'L'), 9.0, Point(7, 0, 'R'))
ed2 = Edificio(Point(6, 0,  'L'), 7, Point(10, 0,  'R'))
ed3 = Edificio(Point(8, 0,  'L'), 6, Point(9, 0, 'R'))
ed4 = Edificio(Point(11, 0,  'L'), 10, Point(12, 0, 'R'))

edificios = [ed1, ed2, ed3, ed4]

# -----------------------------------------------------
# ed1 = Edificio(Point(4, 0, 'L'), 6, Point(8, 0, 'R'))
# ed2 = Edificio(Point(6, 0,  'L'), 4, Point(10, 0,  'R'))
# edificios = [ed1,ed2]
# TODO: Estudar novamente esse algoritmo.
# list(map(print, edificios))
print(mergeEdificio(edificios))