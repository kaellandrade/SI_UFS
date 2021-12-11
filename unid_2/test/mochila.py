#!python3.8
import typing


class Matriz:
    def __init__(self, exist=False, pertence=False) -> None:
        self.exist = exist
        self.pertence = pertence


def mochila(s: list, n: int, K: int):
    MATRIX = [[Matriz() for _ in range(K+1)] for _ in range(n+1)]
    MATRIX[0][0].exist = True

    for i in range(1, n+1):
        for j in range(0, K+1):
            if(MATRIX[i-1][j].exist):
                MATRIX[i][j].exist = True
                MATRIX[i][j].pertence = False
            elif(j - s[i-1] >= 0):
                if(MATRIX[i-1][j-s[i-1]].exist):
                    MATRIX[i][j].exist = True
                    MATRIX[i][j].pertence = True
    return MATRIX[n][K].exist


S = [2,6,3]
K = 5
N = len(S)

print(mochila(S, N, K))
