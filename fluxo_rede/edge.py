
from __future__ import annotations
from dataclasses import dataclass


class WeightedEdge:
    def __init__(self, u: int, v: int, capacidade: float, fluxo: float = 0) -> WeightedEdge:
        self.u = u
        self.v = v
        self.capacidade = capacidade
        self.fluxo = fluxo
        self.arestaRetorno = None

    def reversed(self) -> WeightedEdge:
        return WeightedEdge(self.v, self.u, 0);

    def __str__(self) -> str:
        return f"{self.u}  {self.capacidade} -> {self.v}"

    # Paraque possamos ordenar as arestas por peso a fim de enctrar
    # a resta de menor peso
    def __lt__(self, other: WeightedEdge) -> bool:
        return self.capacidade < other.capacidade
