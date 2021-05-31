#!/usr/bin/env python3
from typing import Callable;
from vertex import Vertex;

"""
Recebe dois vértices e uma função que retorna o peso da
aresta entre esses dois vértices.
Em seguinda, relaxa a aresta que conecta esses dois vértices.
"""
def relax(U: Vertex, V: Vertex, w: Callable) -> None:
    if (V.dist > U.dist + w(U, V)):
        V.dist = U.dist + w(U, V)
        V.parent = U