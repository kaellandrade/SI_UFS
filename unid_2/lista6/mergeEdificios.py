#!python3.8
from algoritmosGeo.FramWorkGeometria import Point
from typing import List
import sys
sys.path.insert(0, '../algoritmosGeo')


def mergeEdificio(L) -> List[Point]:

    n = len(L)
    # Tratando os casos bases.
    if(n == 0):
        return []
    if(n == 1):
        Pointleft = L[0].PointLeft
        PointRight = L[0].PointRight
        Height = L[0].Height
        return [(Pointleft.x, Height), (PointRight.x, 0)]

    # Para Ns prédios
    meio = len(L)//2
    left_skyline = mergeEdificio(L[:meio])
    right_skyline = mergeEdificio(L[meio:])
    # TODO: Combinar as soluções

# def merge(B, C, A):
#     '''
#     ENTRADA: Duas listas B e C e um vetor A
#     SAÍDA: A mesclagem de de B e C.
#     '''
#     i = j = k = 0
#     while(i < len(B) and j < len(C)):
#         if (B[i] <= C[j]):
#             A[k] = B[i]
#             i += 1
#         else:
#             A[k] = C[j]
#             j += 1
#         k += 1
#     if (i == len(B)):
#         A[k:len(A)] = C[j:len(C)]
#     else:
#         A[k:len(A)] = B[i:len(C)]
