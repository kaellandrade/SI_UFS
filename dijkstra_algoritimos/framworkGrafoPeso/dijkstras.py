from __future__ import annotations, print_function
from graph import Graph;
from relax import relax;
from initialize_single_source import initialize_single_source;
from vertex import Vertex;
import heapq;

#Utilizando heap
def dijkstra_heap(G: Graph, s: int) -> bool:
    initialize_single_source(G.vertex_at(s))
    unvisiteed_queue  = [(v.dist,v) for v in G._vertices]
    heapq.heapify(unvisiteed_queue);
    
    while len(unvisiteed_queue):
        uv = heapq.heappop(unvisiteed_queue);
        atual = uv[1];
        atual.cor = 'PRETO';
        for prox in G.neightbors_for_vertex(uv[1]):
            if prox[0].cor == 'PRETO':
                continue;  
            relax(atual, prox[0], G.get_weight_with_vertex);

        while len(unvisiteed_queue):
            heapq.heappop(unvisiteed_queue)

        unvisiteed_queue = [(v.dist,v) for v in G._vertices if v.cor == 'BRANCO']
        heapq.heapify(unvisiteed_queue)

#Versão com busca sequencial
def dijkstra_simples(G: Graph, s: int) -> bool:
    initialize_single_source(G.vertex_at(s));
    u = min_vertex(G._vertices);

    while u != None:
        for V in G.neightbors_for_vertex(u):
            relax(u, V[0], G.get_weight_with_vertex);
        u.cor ='PRETO';
        u = min_vertex(G._vertices);

#Seleciona todos o vértices que estão abertos e pega o que tiver a manor distância;
def min_vertex(vertices:list[Vertex]) -> Vertex:
    min_vertice = float('inf');
    v_min = None; 
    for v in vertices:
        if(v.cor == 'BRANCO' and v.dist < min_vertice):
            min_vertice = v.dist;
            v_min = v;
    return v_min;