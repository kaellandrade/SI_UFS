from __future__ import annotations, print_function
from graph import Graph;
from relax import relax;
from initialize_single_source import initialize_single_source;
# from vertex import Vertex;

import queue as Queue;

def dijkstra(G: Graph, s: int) -> bool:
    initialize_single_source(G.vertex_at(s))
    S : list = []
    Q: Queue = Queue.PriorityQueue();

    for v in G._vertices:
        Q.put((v.dist, v));
    
    while not Q.empty():
        U = Q.get();
        for V in G.neightbors_for_vertex(U[1]):
            relax(U[1], V[0], G.get_weight_with_vertex);