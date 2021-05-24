
from __future__ import annotations;
from dataclasses import dataclass;

class Vertex:
    def __init__(self, vertex:V) -> None:
        self.vertex = vertex;
        self.dist = float('inf');
        self.parent = None;

    @property
    def get_name(self):
        return self.vertex;