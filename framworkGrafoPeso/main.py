#!/usr/bin/env python3
from __future__ import annotations;
from vertex import Vertex;
from graph import Graph;
from print_path import print_path;
from dijkstra import dijkstra;
from random_graph import random_graph;
from datetime import datetime;

if (__name__ == '__main__'):
    tempo_inicio = datetime.now()
    g1: Graph[Vertex] = random_graph(100)

    dijkstra(g1,0) #Algoritmo Heap
    print_path(g1.vertex_at(0), g1.vertex_at(2))
    # print(g1)

    print(datetime.now() - tempo_inicio)