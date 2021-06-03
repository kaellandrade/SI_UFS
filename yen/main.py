#!/usr/bin/env python3
from __future__ import annotations
from vertex import Vertex
from graph import Graph
from dijkstras import dijkstra_heap
from random_graph import random_graph
# from yen import yen;


from datetime import datetime

if (__name__ == '__main__'):
    g1: Graph[Vertex] = Graph([
        Vertex('A'),#0 
        Vertex('B'),#1
        Vertex('C'),#2
        ])
    g1.add_edge_by_indices(0, 1, 5);
    g1.add_edge_by_indices(2, 1, 7);

    g1.remove_vertex_by_index(0);
    print(g1);
    # print(dijkstra_heap(g1, 0, 1));

