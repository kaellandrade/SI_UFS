from __future__ import annotations
from vertex import Vertex


"""
Recebe um número inteiro e retorna uma lista de vértices
"""
def random_vertex(total: int) -> list[Vertex]:
    return [Vertex(f"v{i}") for i in range(1, total+1)]
