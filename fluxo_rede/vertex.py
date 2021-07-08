from __future__ import annotations
from typing import TypeVar

V = TypeVar('V')


class Vertex:
    def __init__(self, vertex: V, fonte: bool = False, sorvedouro: bool = False):
        self.label = vertex;
        self.fonte = fonte;
        self.sorvedouro = sorvedouro

    def __str__(self):
        if self.sorvedouro:
            return f"{self.label}(Sumidouro)"
        elif self.fonte:
            return f"{self.label}(Fonte)"
        else:
            return f"{self.label}"
