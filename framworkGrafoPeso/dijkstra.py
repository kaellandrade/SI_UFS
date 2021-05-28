from __future__ import annotations, print_function
from graph import Graph;
from relax import relax;
from initialize_single_source import initialize_single_source;
# from vertex import Vertex;

import queue as Q;

def dijkstra(G: Graph, s: int) -> bool:
    initialize_single_source(G.vertex_at(s))
    q = Q.PriorityQueue()
    q.put(G.vertex_at(s));
    G.vertex_at(s).cor = 'PRETO'
    
    while not q.empty():
        U = q.get();
        for V in G.neightbors_for_vertex(U):
            relax(U, V[0], G.get_weight_with_vertex);
            if(V[0].cor == 'BRANCO'):
                q.put(V[0]);
            V[0].cor = 'PRETO'
