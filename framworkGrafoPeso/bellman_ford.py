from __future__ import annotations
from graph import Graph;
from relax import relax;
from initialize_single_source import initialize_single_source;


def bellman_ford(G: Graph, s: int) -> bool:
    # Inicializa o vértece
    initialize_single_source(G, G.vertex_at(s))

    #Armazena o conjunto de toodas as arestas de G
    conjuntoTotalAretas = []

    for edge in G._edges:  #Retorna G(E)
        conjuntoTotalAretas += edge

    for _ in range(1, G.vertex_count - 1):
        for edge in conjuntoTotalAretas:
            relax(G.vertex_at(edge.u), G.vertex_at(edge.v),
                  G.get_weight_with_vertex)

    for edge in conjuntoTotalAretas:
        if (G.vertex_at(edge.v).dist > G.vertex_at(edge.u).dist +
                G.get_weight_with_index(edge.u, edge.v)):
            return False
    return True
