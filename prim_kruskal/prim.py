from __future__ import annotations;
from vertex import Vertex;
from graph import Graph;
from edge import WeightedEdge;
from copy import copy;
"""
Recebe um grafo e retorna sua árvore de custo min;
"""
def prim(G:Graph) -> Graph:
    v_i = G._vertices[0]; #Seleciona o primeiro vértice do grafo;
    v_i.cor = 'PRETO'; #Marca como selecionado;


    T:Graph[Vertex] = Graph([copy(x) for x in G._vertices], G.label); #árvore inicialmente Vazia, ou seja, apenas com vértices;
    T_count = 1;

    while(T_count != G.vertex_count):
        min_edge = select_min_edge(G);
        k = G.vertex_at(min_edge.v)
        k.cor = 'PRETO'; #add k ao conjuntos de visitados;
        T.add_edge_by_indices(min_edge.v, min_edge.u, min_edge.weight);
        T_count+=1;
    return T;

def select_min_edge(G:Graph)->WeightedEdge:
    set_edges = []; #Conjunto de arestas do grafo;
    for edge in G._edges: set_edges += edge;

    min_weight = float('inf');
    edge_min = None;

    for edge in set_edges:
        if(G.vertex_at(edge.u).cor == 'PRETO') and (G.vertex_at(edge.v).cor == 'BRANCO'):
            if edge.weight < min_weight:
                edge_min = edge;
                min_weight = edge.weight;

    return edge_min;
