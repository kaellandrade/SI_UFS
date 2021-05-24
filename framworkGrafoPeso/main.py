#!/usr/bin/env python3.8

from __future__ import annotations
import bellman_ford
from vertex import Vertex
from graph import Graph
from print_path import print_path

if (__name__ == '__main__'):
    grafo1: Graph[Vertex] = Graph([
        Vertex("s"),  #0
        Vertex("t"),  #1
        Vertex("x"),  #2
        Vertex("z"),  #3
        Vertex("y"),  #4
    ], True) #Grafo direcinado
    #adiciona todos os vértives que estão em vertices
    grafo1.add_edge_by_indices(0, 1, 6)
    grafo1.add_edge_by_indices(0, 4, 7)
    grafo1.add_edge_by_indices(1, 2, 5)
    grafo1.add_edge_by_indices(2, 1, -2)
    grafo1.add_edge_by_indices(3, 2, 7)
    grafo1.add_edge_by_indices(1, 3, -4)
    grafo1.add_edge_by_indices(3, 0, 2)
    grafo1.add_edge_by_indices(4, 2, -3)
    grafo1.add_edge_by_indices(1, 4, 8)
    grafo1.add_edge_by_indices(4, 3, 9)

    res = print(bellman_ford.bellman_ford(grafo1, 0))  # Executando o algoritmo de bell
    print_path(grafo1.vertex_at(0), grafo1.vertex_at(1))
