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
