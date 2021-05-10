from random import random;
from math import floor;

'''
Representação de um grafo
'''
class Graph():
    def __init__(self, vertices, direcionado = False):
        self.N_vertices = vertices;
        self.N_arestas = 0;
        self.direcionado = direcionado;
        self.adj = dict();
    '''
        Inicializa todos os vértices
    '''
    def iniciar_vertices(self):
        for i in range(self.N_vertices):
            self.adj.setdefault(i, []);
    
    def addArestas(self, v , w):
        self.adj.get(v).append(w);
        if(not self.direcionado): # se não for direcionado adiciona v,w e w,v
            self.adj.get(w).append(v);
        self.N_arestas += 1; # Inclremetna o número de arestas

    '''
        Constrói um grafo aleatório com base no números de vertices passados
    '''
    def grafoRandom(self):
        for i in self.adj:
            v = floor(random() * self.N_vertices);
            w = floor(random() * self.N_vertices);
            self.addArestas(v, w);

