from __future__ import annotations;
from vertex import Vertex;
from graph import Graph;
from edge import WeightedEdge;
from copy import copy;
"""
Recebe um Grafo e retorna sua árvore de custo min;
"""
def kruskal(G:Graph) -> Graph:

    T:Graph[Vertex] = Graph([copy(x) for x in G._vertices], G.label);
    set_edges = []; #Conjunto de arestas do grafo;

    for edge in G._edges: set_edges += edge;
    set_edges.sort(key=lambda edge:edge.weight);

    parente = [i for i in range(G.vertex_count)];
    ranque = [0]*G.vertex_count;

    while(set_edges):
        aresta = set_edges.pop(0);
        x = find(parente, aresta.u);
        y = find(parente, aresta.v);
        if x!=y:
            T.add_edge_by_indices(aresta.v, aresta.u, aresta.weight);
            union(parente, ranque, x, y);
    return T;

'''
Dado um vértice j, find irá encontrar em qual
conjunto j pertence. 
'''
def find(parente, j):
    if(parente[j] == j):
        return j
    return find(parente, parente[j]);

'''
Dado dois conjuntos X e Y (disjuntos) union irá unir X e Y
'''
def union(parente, ranque, x, y):
    xroot = find(parente, x);
    yroot = find(parente, y);
    if (ranque[xroot] < ranque[yroot]):
        parente[xroot] = yroot;
    elif ranque[xroot] > ranque[yroot]:
        parente[yroot] = xroot;
    else:
        parente[yroot] = xroot;
        ranque[xroot] += 1;
