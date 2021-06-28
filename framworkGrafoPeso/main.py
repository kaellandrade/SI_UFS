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
        Vertex('A'),#0
        Vertex('B'),#1
        Vertex('C'),#2
        Vertex('D'),#3
        Vertex('E'),#4
        Vertex('F'),#5  

    ],  True)

    g1.add_edge_by_indices(0, 1, 8);
    g1.add_edge_by_indices(0, 2, 8);
    g1.add_edge_by_indices(0, 3, 8);
    g1.add_edge_by_indices(0, 4, 8);
    g1.add_edge_by_indices(0, 5, 2);

    g1.add_edge_by_indices(1, 0, 8);
    g1.add_edge_by_indices(1, 2, -2);
    g1.add_edge_by_indices(1, 3, 7);
    g1.add_edge_by_indices(1, 4, 6);
    g1.add_edge_by_indices(1, 5, 2);

    g1.add_edge_by_indices(2, 0, 8);
    g1.add_edge_by_indices(2, 1, 4);
    g1.add_edge_by_indices(2, 3, 3);
    g1.add_edge_by_indices(2, 4, 2);
    g1.add_edge_by_indices(2, 5, 3);

    g1.add_edge_by_indices(3, 0, 8);
    g1.add_edge_by_indices(3, 1, 4);
    g1.add_edge_by_indices(3, 1, 4);
    g1.add_edge_by_indices(3, 4, -1);
    g1.add_edge_by_indices(3, 5, 4);

    g1.add_edge_by_indices(4, 0, 8);
    g1.add_edge_by_indices(4, 1, 2);
    g1.add_edge_by_indices(4, 2, 2);
    g1.add_edge_by_indices(4, 3, 3);
    g1.add_edge_by_indices(4, 5, 8);

    g1.add_edge_by_indices(5, 0, 8);
    g1.add_edge_by_indices(5, 1, 3);
    g1.add_edge_by_indices(5, 2, 2);
    g1.add_edge_by_indices(5, 3, -1);
    g1.add_edge_by_indices(5, 4, 4);



    bellman_ford(g1, 0);
    print_path(g1.vertex_at(0), g1.vertex_at(2))
    # print(g1);

    


