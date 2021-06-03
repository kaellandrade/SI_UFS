from __future__ import annotations
from vertex import Vertex
from graph import Graph
from random_vertex import random_vertex
from random_weight import random_weight

"""
Recebe a quantidade de vértices e retorna um grafo ponderado e completo aleatório
"""
def random_graph(totalVerteces: int) -> Graph:
    grafo: Graph[Vertex] = Graph(random_vertex(totalVerteces))

    # Gerando o grafo aleatório completo
    for v in range(grafo.vertex_count):
        for u in range(grafo.vertex_count):
            
            if (v == u or grafo.get_weight_with_index(v, u) != float('inf')):  #Evitando ciclos e arestas múltiplas
                continue;

            peso = random_weight(20, 100)
            grafo.add_edge_by_indices(v, u, peso)

    return grafo
