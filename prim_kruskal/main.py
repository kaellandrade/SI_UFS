#!/usr/bin/env python3
from __future__ import annotations;
from vertex import Vertex;
from graph import Graph;
from prim import prim;
from kruskal import kru;

if (__name__ == '__main__'):

    g1: Graph[Vertex] = Graph([
        Vertex('A'),#0
        Vertex('B'),#1
        Vertex('C'),#2
        Vertex('D'),#3
        Vertex('E'),#4
        Vertex('F'),#5
        Vertex('G'),#6
        Vertex('H'),#7
        Vertex('I'),#8
        Vertex('J')#9
    ], 'Grafo [Grafos] Aula 06 - Árvores Geradoras de Custo Mínimo(Grafo do exercício)');
    g1.add_edge_by_indices(0, 1, 6);
    g1.add_edge_by_indices(0, 2, 1);
    g1.add_edge_by_indices(0, 3, 14);
    g1.add_edge_by_indices(0, 3, 14);
    g1.add_edge_by_indices(1, 2, 10);
    g1.add_edge_by_indices(1, 4, 6);
    g1.add_edge_by_indices(1, 5, 8);
    g1.add_edge_by_indices(2, 3, 7);
    g1.add_edge_by_indices(2, 5, 7);
    g1.add_edge_by_indices(3, 5, 6);
    g1.add_edge_by_indices(3, 6, 6);
    g1.add_edge_by_indices(4, 5, 4);
    g1.add_edge_by_indices(4, 7, 3);
    g1.add_edge_by_indices(5, 7, 6);
    g1.add_edge_by_indices(5, 6, 1);
    g1.add_edge_by_indices(5, 8, 5);
    g1.add_edge_by_indices(6, 9, 5);
    g1.add_edge_by_indices(7, 8, 6);
    g1.add_edge_by_indices(8, 9, 5);

    g2: Graph[Vertex] = Graph([
        Vertex('V1'),#0
        Vertex('V2'),#1
        Vertex('V3'),#2
        Vertex('V4'),#3
        Vertex('V5'),#4
        Vertex('V6'),#5
    ], 'Grafo [Grafos] Aula 06 - Grafo usado no algoritmo de Prim');

    g2.add_edge_by_indices(0, 1, 1);
    g2.add_edge_by_indices(0, 2, 3);
    g2.add_edge_by_indices(1, 2, 1);
    g2.add_edge_by_indices(1, 3, 1);
    g2.add_edge_by_indices(1, 4, 4);
    g2.add_edge_by_indices(2, 4, 2);
    g2.add_edge_by_indices(3, 5, 1);
    g2.add_edge_by_indices(3, 4, -2);
    g2.add_edge_by_indices(4, 5, 2);

    g3: Graph[Vertex] = Graph([
        Vertex('V1'),#0
        Vertex('V2'),#1
        Vertex('V3'),#2
        Vertex('V4'),#3
        Vertex('V5'),#4
        Vertex('V6'),#5
        Vertex('V7')#6
    ], 'Grafo [Grafos] Aula 06 - Grafo usado no algoritmo de Kruskal');

    g3.add_edge_by_indices(0, 2, 6);
    g3.add_edge_by_indices(2, 1, 3);
    g3.add_edge_by_indices(2, 3, 9);
    g3.add_edge_by_indices(1, 5, 3);
    g3.add_edge_by_indices(1, 4, 8);
    g3.add_edge_by_indices(4, 5, 2);
    g3.add_edge_by_indices(5, 6, 5);
    g3.add_edge_by_indices(6, 5, 7);
    g3.add_edge_by_indices(6, 3, 1);
    g3.add_edge_by_indices(2, 5, 1);
    print('------Usando Kruskal------');
    print(kru(g1));
    print(kru(g2));
    print(kru(g3));

    print('-----Usando Prim-----');
    print(prim(g1));
    print(prim(g2));
    print(prim(g3)); 