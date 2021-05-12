#!/usr/bin/env python3
from math import inf as Infinity
from typing import Pattern;

class Grafo():
    def __init__(self, NumeroVertices, direcionado = False):
        self.Direcionado = direcionado; 
        self.NumeroVertices = NumeroVertices;
        self.ListaAdj = dict();

        for i in range(self.NumeroVertices): #Inicializa todos os Vértices
            self.ListaAdj.setdefault(i, []);

    '''
    Retorna uma string com o tipo do grafo [direcionado ou não direcionado]
    '''
    def __tipografo(self):
        if(self.Direcionado):
            return 'GD'
        else:
            return 'GND'
    '''
        Adiciona um vértice ao Grafo
    '''
    def addVertice(self, v):
        if(v not in self.ListaAdj):
            self.ListaAdj.setdefault(v,[]);
    '''
        Adiciona uma Aresta ao grafo
    '''
    def addAresta(self, v1, v2):
        try:
            self.ListaAdj.get(v1).append(v2);
            if(not self.Direcionado): 
                self.ListaAdj.get(v2).append(v1);
            
        except :
            print(f"Arestas ({v1}, {v2}) inválidas!");

    '''
        Dada uma aresta (v1,v2) de G essa aresta será removida
        caso exista.
    '''
    def removerAresta(self, v1, v2): 
        listV1 = self.ListaAdj.get(v1);
        listV2 = self.ListaAdj.get(v2);
        
        try:
            listV1.remove(v2);
            listV2.remove(v1);
        except:
            print("Aresta não existe!");

    '''
        Remove um vértice v do grafo e todas suas conexões;
    '''
    def removerVertice(self, v):
        for vertice in self.ListaAdj:
            newDict = { vertice : list(filter(lambda x : x != v, self.ListaAdj.get(vertice)))}
            self.ListaAdj.update(newDict);
        try:    
            self.ListaAdj.pop(v); 
        except:
            print(f"Vertice {v} inválido") 

    def imprimeGrafo(self):
        print("\nLista ADJ {}".format(self.__tipografo()));
        for item in self.ListaAdj:
            print(f"[{item}]:", self.__imprimeAdjList(self.ListaAdj.get(item)));
    
    def __imprimeAdjList(self, lista):
        if(len(lista) == 0):
            return 'NULL';
        else:
            return " -> ".join(tuple(map(lambda x:str(x),lista)))+' -> NULL';



'''
Algoritmo de busca em profundidade;
Inspirado no livro de Thomas H.Cormen (Algoritmos Teoria e Prática)
'''
def bfs(G, startV, destino, predecessor, distancia):
    contador = 0;
    num = [-1] * G.NumeroVertices; # vetor de enumeração (ordem em que os vértices são descobertos); 
    num[startV] = contador;

    contador+=1;
    fila = [];
    
    arvore_bfs = Grafo(G.NumeroVertices, G.Direcionado); 
    fila.append(startV);

    while(fila):
        u = fila.pop();
        for v in G.ListaAdj[u]:
            if(num[v] == -1): #se ainda não foi descoberto
                num[v] = contador;
                contador+=1;

                distancia[v] = distancia[u]+1;
                predecessor[v] = u;

                arvore_bfs.addAresta(u, v)
                fila.append(v);
                if(v == destino):
                    print(arvore_bfs.ListaAdj);
                    return True;
    print(arvore_bfs.ListaAdj);
    return False;
'''
    Algoritmo de Bellman–Ford 
    Inspirado no livro de Thomas H.Cormen (Algoritmos Teoria e Prática)
'''
def caminhoMin(Grafo, inicio, destino):

    predecessor = [None] * Grafo.NumeroVertices;
    distancia = [0] * Grafo.NumeroVertices;

    if(not bfs(Grafo, inicio, destino, predecessor, distancia)):
        print('Verteces não conectados!');
    else:
        caminho = [];
        c = destino;
        caminho.insert(0, c);
        while(predecessor[c] != None):
            caminho.insert(0,predecessor[c]);
            c = predecessor[c];

        print(caminho);
        print(distancia[destino]);

    

G1 = Grafo(3,True);


G1.addAresta(0, 1);
G1.addAresta(1, 2);
G1.addAresta(0, 2);




caminhoMin(G1, 0, 2);
