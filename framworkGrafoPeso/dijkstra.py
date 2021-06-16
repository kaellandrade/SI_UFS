from __future__ import annotations, print_function
from graph import Graph;
from relax import relax;
from initialize_single_source import initialize_single_source;
import heapq
# from vertex import Vertex;

import queue as Q;

def dijkstra(G: Graph, s: int) -> bool:
    initialize_single_source(G.vertex_at(s))
    nao_visitados  = [(v.dist,v) for v in G._vertices]
    heapq.heapify(nao_visitados);
    
    while len(nao_visitados):
        uv = heapq.heappop(nao_visitados);
        atual = uv[1];
        atual.cor = 'PRETO';
        for prox in G.neightbors_for_vertex(uv[1]):
            if prox[0].cor == 'PRETO':
                continue;  
            relax(atual, prox[0], G.get_weight_with_vertex);

        while len(nao_visitados):
            heapq.heappop(nao_visitados)

        nao_visitados = [(v.dist,v) for v in G._vertices if v.cor == 'BRANCO']
        heapq.heapify(nao_visitados)
