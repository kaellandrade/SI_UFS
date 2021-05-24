from __future__ import annotations
from typing import TypeVar

V = TypeVar('V')  #Tipo de vértices no grafo;
class Vertex:
    def __init__(self, vertex: V) -> None:
        self.label = vertex;
        self.dist = float('inf');
        self.parent = None;
        self.cor = 'BRANCO';
        
    def __str__(self) -> str:
        return f"({self.label}) -> {self.dist}"