
from __future__ import annotations;
from dataclasses import dataclass;

@dataclass #Cria automáticamente o método __init__
class Edge:
    u:int # o vértice 'de';
    v:int # o vértice 'para'

    def reversed(self) -> Edge:
        return Edge(self.v, self.u)
    

    def __str__(self) -> str:
        return f"{self.u} -> {self.v}"
