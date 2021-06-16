#!/usr/bin/env python3
from __future__ import annotations
from bellman_ford import bellman_ford;
from vertex import Vertex;
from graph import Graph;
from print_path import print_path;
from dijkstra import dijkstra;
from random_graph import random_graph;

from datetime import datetime;

if (__name__ == '__main__'):
    g1: Graph[Vertex] = Graph([
        Vertex('s'),#0
        Vertex('x'),#1
        Vertex('t'),#2
        Vertex('y'),#3
        Vertex('z'),#4
    ],  True)
    g1.add_edge_by_indices(0, 2, 6);
    g1.add_edge_by_indices(0, 3, 7);
    g1.add_edge_by_indices(2, 1, 5);
    g1.add_edge_by_indices(1, 2, -2);
    g1.add_edge_by_indices(2, 3, 8);
    g1.add_edge_by_indices(3, 4, 9);
    g1.add_edge_by_indices(4, 0, 2);
    g1.add_edge_by_indices(2, 4, -4);
    g1.add_edge_by_indices(3, 1, -3);
    g1.add_edge_by_indices(4, 1, 7);







    # dijkstra(g1, 0);
    # print(g1);
    # print_path(g1.vertex_at(0), g1.vertex_at(5))
    # g1.resetGraph;
    bellman_ford(g1, 0);
    print(g1);
    print_path(g1.vertex_at(0), g1.vertex_at(4))

    


