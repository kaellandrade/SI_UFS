from __future__ import annotations, print_function
from graph import Graph;
from dijkstras import dijkstra_heap;
from vertex import Vertex;
from edge import WeightedEdge;
from copy import copy;
def yen(G:Graph, de:int, para:int, K:int):
    A = [dijkstra_heap(G, de, para)];
    backUpEdge = [list(map(copy, edge)) for edge in G._edges]; # Matém um copia de todas as listas de adjacências
    B = [];
    for k in range(1, K):
        for i in range(len(A[k-1]) - 2):
            rootPath = A[k-1][:i+1];
            for path in A:
                if(rootPath == path[:i+1]):
                    setValueEdge(G, path[i], path[i+1], float('inf'));

            G.resetGraph; #Reseta o grafo;
            spurPath = dijkstra_heap(G, de, para);

            if(spurPath not in B and spurPath):
                T = tuple((list(map(lambda x:x, spurPath)), spurPath[-1].dist));
                B.append(T);

            G._edges = [list(map(copy, edge)) for edge in backUpEdge]

        if(len(B) == 0):
            break;

        B.sort(key=lambda tup:tup[1]);
        A.append(B[0][0]);
        B.pop(0);
    return A;
    
def setValueEdge(G:Graph, u:Vertex, v:Vertex, value: float) -> None:
    edge: WeightedEdge = G.give_edge(G.index_of(u), G.index_of(v));
    edge.weight = value;
    return edge;