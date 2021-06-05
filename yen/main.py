#!/usr/bin/env python3
from __future__ import annotations
from yen import yen
from vertex import Vertex
from graph import Graph
from dijkstras import dijkstra_heap
from random_graph import random_graph
from yen import yen, setValueEdge

from datetime import datetime

if (__name__ == '__main__'):

    g1: Graph[Vertex] = Graph(
        [
            Vertex('C'),  #0
            Vertex('D'),  #1
            Vertex('E'),  #2
            Vertex('F'),  #3
            Vertex('G'),  #4
            Vertex('H')  #5
        ],
        True)

    g1.add_edge_by_indices(0, 1, 3)
    g1.add_edge_by_indices(0, 2, 2)
    g1.add_edge_by_indices(1, 3, 4)
    g1.add_edge_by_indices(2, 1, 1)
    g1.add_edge_by_indices(2, 3, 2)
    g1.add_edge_by_indices(2, 4, 3)
    g1.add_edge_by_indices(3, 4, 2)
    g1.add_edge_by_indices(3, 5, 1)
    g1.add_edge_by_indices(4, 5, 2)

    print([list(map(lambda x:x.label, paths)) for paths in yen(g1, 0, 5, 3)])
    # print(g1)
