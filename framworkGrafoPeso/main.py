
from __future__ import annotations
from bellman_ford import bellman_ford
from vertex import Vertex
from graph import Graph
from print_path import print_path
from dijkstra import dijkstra


if (__name__ == '__main__'):
    cidade_grafo: Graph[Vertex] = Graph([
        Vertex("1"),  #0
        Vertex("2"),  #1
        Vertex("3"),  #2
        Vertex("4"),  #3
        Vertex("5"),  #4
        Vertex("6"),  #5
        Vertex("7"),  #6
        Vertex("8"),  #7
        Vertex("9"),  #8
        Vertex("10"),  #9
        Vertex("11"),  #10
        Vertex("12"),  #11
        Vertex("13"),  #12
        Vertex("14"),  #13
        Vertex("Ourivesaria"),  #14
    ], True)

    #adiciona todos os vértives que estão em vertices
    cidade_grafo.add_edge_by_indices(0, 12, 10);
    cidade_grafo.add_edge_by_indices(0, 1, 8);
    cidade_grafo.add_edge_by_indices(1, 2, 10);
    cidade_grafo.add_edge_by_indices(2, 3, 12);
    cidade_grafo.add_edge_by_indices(3, 7, 14);
    cidade_grafo.add_edge_by_indices(2, 4, 9);
    cidade_grafo.add_edge_by_indices(1, 13, 7);
    cidade_grafo.add_edge_by_indices(4, 5, 4);
    cidade_grafo.add_edge_by_indices(4, 6, 3);
    cidade_grafo.add_edge_by_indices(13, 5, 8);
    cidade_grafo.add_edge_by_indices(13, 12, 6);
    cidade_grafo.add_edge_by_indices(6, 5, 5);
    cidade_grafo.add_edge_by_indices(7, 6, 9);
    cidade_grafo.add_edge_by_indices(7, 14, 10);
    cidade_grafo.add_edge_by_indices(12, 11, 13);
    cidade_grafo.add_edge_by_indices(11, 10, 8);
    cidade_grafo.add_edge_by_indices(10, 9, 11);
    cidade_grafo.add_edge_by_indices(10, 8, 16);
    cidade_grafo.add_edge_by_indices(9, 8, 4);
    cidade_grafo.add_edge_by_indices(8, 14, 9);
    
    
    bellman_ford(cidade_grafo,0)
    # dijkstra(cidade_grafo,0)
    print_path(cidade_grafo.vertex_at(0), cidade_grafo.vertex_at(14))
    # print(cidade_grafo)