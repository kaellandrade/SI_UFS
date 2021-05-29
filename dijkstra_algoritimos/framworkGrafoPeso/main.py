#!/usr/bin/env python3
from __future__ import annotations;
from vertex import Vertex;
from graph import Graph;
from print_path import print_path;
from dijkstras import dijkstra_heap, dijkstra_simples;
from random_graph import random_graph;



from datetime import datetime;

if (__name__ == '__main__'):
    g1: Graph[Vertex] = random_graph(100)

    tempo_heap = datetime.now()
    dijkstra_heap(g1,0) #Algoritmo Heap
    print(f'Dijkstra HEAP TIME  {datetime.now() - tempo_heap}')
    print_path(g1.vertex_at(0), g1.vertex_at(6))

    g1.resetGraph;
    print('\n');

    tempo_seque = datetime.now()
    dijkstra_simples(g1,0) 
    print(f'Dijkstra Sequencial  {datetime.now() - tempo_seque}')

    print_path(g1.vertex_at(0), g1.vertex_at(6))

