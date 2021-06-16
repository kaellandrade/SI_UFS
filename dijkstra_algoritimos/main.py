#!/usr/bin/env python3
from __future__ import annotations
from vertex import Vertex
from graph import Graph
from print_path import print_path
from dijkstras import dijkstra_heap, dijkstra_simples
from random_graph import random_graph

from datetime import datetime

if (__name__ == '__main__'):
    g1: Graph[Vertex] = Graph([
        Vertex('A'),#0
        Vertex('B'),#1
        Vertex('C'),#2
        Vertex('D'),#3
        Vertex('E'),#4
        Vertex('Z')#5
    ])
    g1.add_edge_by_indices(0, 1, -2);
    g1.add_edge_by_indices(0, 2, -3);
    g1.add_edge_by_indices(1, 3, 5);
    g1.add_edge_by_indices(1, 4, -2);
    g1.add_edge_by_indices(2, 4, -5);
    g1.add_edge_by_indices(4, 3, 1);
    g1.add_edge_by_indices(4, 5, 4);
    g1.add_edge_by_indices(3, 5, 2);
    dijkstra_heap(g1, 0);
    print_path(g1.vertex_at(0), g1.vertex_at(5))
    # print(g1)



