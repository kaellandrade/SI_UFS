#!/usr/bin/env python3

from __future__ import annotations;
from bellman_ford import bellman_ford;
from vertex import Vertex;
from graph import Graph;
from print_path import print_path;
from dijkstra import dijkstra;

if (__name__ == '__main__'):
    cidade_grafo: Graph[Vertex] = Graph([
        Vertex("Seattle"),  #0
        Vertex("San Francisco"),  #1
        Vertex("Los Angeles"),  #2
        Vertex("Riverside"),  #3
        Vertex("Phoenix"),  #4
        Vertex("Chicago"),  #5
        Vertex("Boston"),  #6
        Vertex("New York"),  #7
        Vertex("Atlanta"),  #8
        Vertex("Miami"),  #9
        Vertex("Dallas"),  #10
        Vertex("Houston"),  #11
        Vertex("Detroit"),  #12
        Vertex("Philadelphia"),  #13
        Vertex("Washington")  #14
    ])
    #adiciona todos os vértives que estão em vertices
    cidade_grafo.add_edge_by_indices(0, 5, 1737)
    cidade_grafo.add_edge_by_indices(0, 1, 678)
    cidade_grafo.add_edge_by_indices(1, 3, 386)
    cidade_grafo.add_edge_by_indices(1, 2, 348)
    cidade_grafo.add_edge_by_indices(2, 3, 50)
    cidade_grafo.add_edge_by_indices(2, 4, 357)
    cidade_grafo.add_edge_by_indices(3, 4, 307)
    cidade_grafo.add_edge_by_indices(3, 5, 1704)
    cidade_grafo.add_edge_by_indices(4, 10, 887)
    cidade_grafo.add_edge_by_indices(4, 11, 1015)
    cidade_grafo.add_edge_by_indices(10, 5, 805)
    cidade_grafo.add_edge_by_indices(10, 8, 721)
    cidade_grafo.add_edge_by_indices(10, 11, 225)
    cidade_grafo.add_edge_by_indices(11, 8, 702)
    cidade_grafo.add_edge_by_indices(11, 9, 968)
    cidade_grafo.add_edge_by_indices(8, 5, 588)
    cidade_grafo.add_edge_by_indices(8, 14, 543)
    cidade_grafo.add_edge_by_indices(8, 9, 604)
    cidade_grafo.add_edge_by_indices(9, 14, 923)
    cidade_grafo.add_edge_by_indices(5, 12, 238)
    cidade_grafo.add_edge_by_indices(12, 6, 613)
    cidade_grafo.add_edge_by_indices(12, 14, 396)
    cidade_grafo.add_edge_by_indices(12, 7, 482)
    cidade_grafo.add_edge_by_indices(6, 7, 190)
    cidade_grafo.add_edge_by_indices(7, 13, 81)
    cidade_grafo.add_edge_by_indices(13, 14, 123)


    # bellman_ford(cidade_grafo,3)
    dijkstra(cidade_grafo,3)

    print_path(cidade_grafo.vertex_at(3), cidade_grafo.vertex_at(9))