#!/usr/bin/env python3
'''
    A busca em largura deve ser testada utilizando três grafos. 
    A variante deve ser testada para alguns pares de vértices. 
    Um documento também deve ser enviado para apresentar os grafos testados, 
    as árvores de busca resultantes e os caminhos mínimos entre os pares de vértices testados.
'''
class Grafo():
    def __init__(self, NumeroVertices, direcionado = False):
        self.Direcionado = direcionado; 
        self.NumeroVertices = NumeroVertices;

        self.distancia = [float('inf')] * self.NumeroVertices;
        self.predecessor = [None] * self.NumeroVertices;
        self.peso = [1] * self.NumeroVertices;

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
        u = fila.pop(0);
        for v in G.ListaAdj[u]:
            if(cor[v] == BRANCO): #se ainda não foi descoberto
                cor[v] = CINZA;
                distancia[v] = distancia[u] + 1;
                predecessor[v] = u;
                arvore_bfs.addAresta(u, v)
                fila.append(v);
        cor[u] = PRETO;

    print('Árvore busca BFS: ');
    print(arvore_bfs.ListaAdj);
    print(predecessor)
    return predecessor;


def print_path(s,v, predecessor):
    if(v==s): print(s, end='-');
    elif(predecessor[v] == None): #Se for None
        print('Não existe caminho de {} para {}'.format(s,v));
    else:
        print_path(s, predecessor[v], predecessor);
        print(v, end='-');

def path_s_to_w(G, s, w):
    pre = bfs(G, s);
    print('\nCaminho mínimo:')
    print_path(s, w, pre);
    print('FIM\n');

def inicialize_single_sorce(G, s):
    G.distancia[s] = 0;

def  relax(G,u,v,w):
    if(G.distancia[v] > G.distancia[u] + peso(u, v)):
        G.distancia[v] = G.diatancia[u] + peso(u, v)
        G.predecessor[v] = u
 
'''
GND = Grafo(5);
GND.addAresta(0,1);
GND.addAresta(1,2);
GND.addAresta(2,3);
GND.addAresta(3,4);
GND.addAresta(2,4);


GD1 = Grafo(7, True);
GD1.addAresta(0,1);
GD1.addAresta(1,2);
GD1.addAresta(2,3);
GD1.addAresta(2,4);
GD1.addAresta(4,5);
GD1.addAresta(0,4);
GD1.addAresta(4,6);
GD1.addAresta(6,5);


GD2 = Grafo(6, True);
GD2.addAresta(1,3);
GD2.addAresta(1,2);
GD2.addAresta(1,0);
GD2.addAresta(0,4);
'''
GD3 = Grafo(15);
GD3.addAresta(0, 5)
GD3.addAresta(0, 1)
GD3.addAresta(9, 11)
GD3.addAresta(1, 3)
GD3.addAresta(4, 11)
GD3.addAresta(1, 2)
GD3.addAresta(2, 3)
GD3.addAresta(2, 4)
GD3.addAresta(3, 4)
GD3.addAresta(3, 5)
GD3.addAresta(4, 10)
GD3.addAresta(10, 5)
GD3.addAresta(10, 8)
GD3.addAresta(10, 11)
GD3.addAresta(11, 8)
GD3.addAresta(8, 5)
GD3.addAresta(8, 14)
GD3.addAresta(8, 9)
GD3.addAresta(9, 14)
GD3.addAresta(5, 12)
GD3.addAresta(12, 6)
GD3.addAresta(12, 14)
GD3.addAresta(12, 7)
GD3.addAresta(6, 7)
GD3.addAresta(7, 13)
GD3.addAresta(13, 14)















# path_s_to_w(GND, 0, 4);
# path_s_to_w(GD1, 0, 4);
# path_s_to_w(GD2, 1, 5);

path_s_to_w(GD3, 0, 9);

# inicialize_single_sorce(GD3, 0)
# print(GD3.distancia)