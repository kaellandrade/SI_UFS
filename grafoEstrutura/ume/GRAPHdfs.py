#!/usr/bin/env python3
from graph import Graph;
'''
VISITA TODOS OS VÉRTICES DO GRAFO
A função GRAPHdfs faz uma busca em profundidade no grafo G
Ela atribui um número de ordem pre[x] a cada vértice x
de modo que o k-ésimo vértice descoberto receba o número 
de ordem k. No finaal será devolvida a floresta da busca.
'''
cont = 0;
def GRAPHdfs(Grafo):
    pre = [-1] * Grafo.N_vertices;
    # pais = [None] * Grafo.N_vertices; #Vetor de pais 

    floresta = Graph(Grafo.N_vertices, Grafo.direcionado); #Armazena a floresta encontrada depois da busca DFS
    floresta.iniciar_vertices();
    
    for v in Grafo.adj:
        if(pre[v] == -1):
            # floresta.addArestas(v,w);
            # pais[v] = v; # V é a raiz da floresta;
            dfsR(Grafo, pre, v, floresta); #Começa nova etapa, pos nem todos os vértices podem está ao alcance de v
    # print(pais)
    return floresta.adj;

'''
    A função dfsR visita os vértices de G que podem ser
    alcançados a partir do vértice v sem passar por vértices
    já descobertos. A função atribui cnt+k a pre[x] se x é 
    k-ésimo vértice descoberto.
'''
def dfsR(Grafo, pre, v, floresta):
    global cont;
    pre[v] = cont;
    cont+=1;
    for w in Grafo.adj[v]:
        if(pre[w] == -1):
            floresta.addArestas(v,w);
            # pais[w] = v; # v-w é arco da floresta
            dfsR(Grafo, pre, w, floresta);

G1 = Graph(13);
 
G1.iniciar_vertices();

G1.addArestas(0, 1);
G1.addArestas(0, 9);
G1.addArestas(1, 3);
G1.addArestas(1, 4);
G1.addArestas(1, 6);
G1.addArestas(1, 7);
G1.addArestas(1, 9);
G1.addArestas(2, 5);
G1.addArestas(2, 8);
G1.addArestas(2, 10);
G1.addArestas(3, 7);
G1.addArestas(4, 6);
G1.addArestas(6, 12);
G1.addArestas(8, 10);


# print(g1.adj);
print(GRAPHdfs(G1));