#!/usr/bin/env python3

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
Algoritmo de busca em profundidade;
Inspirado no livro de Thomas H.Cormen (Algoritmos Teoria e Prática)
'''
def bfs(G, startV):
    BRANCO = 'BRANCO';
    CINZA =  'CINZA';
    PRETO = 'PRETO';

    cor = [BRANCO]*G.NumeroVertices;
    distancia = [float('inf')] * G.NumeroVertices;
    predecessor = [None] * G.NumeroVertices;
    arvore_bfs = Grafo(G.NumeroVertices, G.Direcionado); 

    cor[startV] = CINZA;
    distancia[startV] = 0;
    predecessor[startV] = None;

    fila = [];
    fila.append(startV);

    while(fila):
        u = fila.pop();
        for v in G.ListaAdj[u]:
            if(cor[v] == BRANCO): #se ainda não foi descoberto
                cor[v] = CINZA;
                distancia[v] = distancia[u] + 1;
                predecessor[v] = u;
                arvore_bfs.addAresta(u, v)
                fila.append(v);
        cor[u] = PRETO;

    print(predecessor);
    print(arvore_bfs.ListaAdj);
    return predecessor;


def print_path(s,v, predecessor):
    if(v==s): print(s);
    elif(predecessor[v] == None): #Se for None
        print('Não existe caminho de {} para {}'.format(s,v));
    else:
        print_path(s, predecessor[v], predecessor);
        print(v);

def path_s_to_w(G, s, w):
    pre = bfs(G, s);
    print_path(s, w, pre);



G1 = Grafo(4,True);


G1.addAresta(0, 1);
G1.addAresta(1,2);
G1.addAresta(3,2);
# G1.addAresta(0,2);



path_s_to_w(G1, 3, 0);