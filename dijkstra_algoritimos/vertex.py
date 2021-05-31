from __future__ import annotations
from typing import TypeVar

V = TypeVar('V')  #Tipo de vértices no grafo;
"""
Cria um vértice com um rótulo, uma distância, pai e seu estado de visitado;
"""
class Vertex:
    def __init__(self, vertex: V):
        self.label = vertex;
        self.dist = float('inf');
        self.parent = None;
        self.cor = 'BRANCO';
        
    def __str__(self):
        return f"({self.label}) -> {self.dist}"

    def __lt__(self, other):
        return self.dist < other.dist;