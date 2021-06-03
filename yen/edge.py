
from __future__ import annotations;
from dataclasses import dataclass
from vertex import Vertex;

@dataclass #Cria automaticamente o método __init__
class WeightedEdge:
    u:Vertex # o vértice 'de';
    v:Vertex # o vértice 'para'
    weight:int #peso

    def reversed(self) -> WeightedEdge:
        return WeightedEdge(self.v, self.u, self.weight)
    

    def __str__(self) -> str:
        return f"{self.u}  {self.weight} -> {self.v}"
    
    #Paraque possamos ordenar as arestas por peso a fim de enctrar
    # a resta de menor peso
    def __lt__(self, other:WeightedEdge) ->bool:
        return self.weight < other.weight;
