from __future__ import annotations;
from vertex import Vertex;
from graph import Graph;
from edge import WeightedEdge;
from copy import copy;
"""
Recebe um grafo e retorna sua árvore de custo min;
"""
def kru(G:Graph) -> Graph:

    T:Graph[Vertex] = Graph([copy(x) for x in G._vertices], G.label);
    set_edges = []; #Conjunto de arestas do grafo;

    for edge in G._edges: set_edges += edge;
    set_edges.sort(key=lambda edge:edge.weight);

    parent = [i for i in range(G.vertex_count)];
    rank = [0]*G.vertex_count;

    while(set_edges):
        aresta = set_edges.pop(0);
        x = find(parent, aresta.u);
        y = find(parent, aresta.v);
        if x!=y:
            T.add_edge_by_indices(aresta.v, aresta.u, aresta.weight);
            union(parent, rank, x, y);
    return T;
    
def find(parent, i):
    if(parent[i] == i):
        return i
    return find(parent, parent[i]);

def union(parent, rank, x, y):
    xroot = find(parent, x);
    yroot = find(parent, y);
    if (rank[xroot] < rank[yroot]):
        parent[xroot] = yroot;
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot;
    else:
        parent[yroot] = xroot;
        rank[xroot] += 1;
