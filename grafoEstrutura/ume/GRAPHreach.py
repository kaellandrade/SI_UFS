#!/usr/bin/env python3
from graph import Graph;

'''
    Afunção GRAPHReachrecebe vértices s e t de um grafo G
    e decide se t está ao alcance de s ou não;
'''
def GRAPHReach(grafo, s, t):
    visitados = [False]*grafo.N_vertices;
    reachR(grafo,visitados, s);
    if(not visitados[t]): 
        return False;
    else:
        return True;
    
'''
    Função recursiva
'''
def reachR(grafo, visitados, v):
    visitados[v] = True;
    print(v); # Ordem de visitar os vétices
    for vert in grafo.adj[v]:
        if(not visitados[vert]):
            reachR(grafo, visitados, vert);
    
g1 = Graph(5, True) # Grafo direcionado;
g1.iniciar_vertices();

g1.addArestas(0,1); 
g1.addArestas(0,2); 
g1.addArestas(2,3);
g1.addArestas(2,4); 
g1.addArestas(1,3); 
g1.addArestas(3,4); 




print(g1.adj);
print(GRAPHReach(g1, 0, 3));