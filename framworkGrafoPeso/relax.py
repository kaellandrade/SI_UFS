#!/usr/bin/env python3
from typing import Callable;
from vertex import Vertex;

#! Relaxa uma aresta para usar os algoritmos de camihnos mins
def relax(U: Vertex, V: Vertex, w: Callable) -> None:
    if (V.dist > U.dist + w(U, V)):
        V.dist = U.dist + w(U, V)
        V.parent = U