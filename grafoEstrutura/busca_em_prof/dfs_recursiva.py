#!/usr/bin/env python3
'''
Versão recursiva
'''
class Grafo():
    def __init__(self, NumeroVertices, direcionado = False):
        self.Direcionado = direcionado; 
        self.NumeroVertices = NumeroVertices;
        self.ListaAdj = dict();
    
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
    
    def dfs(self, v_inicio):
        print('Varredura DFS iniciando pelo vértice {}'.format(v_inicio));
        # Constantes para guiar o percurso;
        BRANCO = 'BRANCO';
        PRETO = 'PRETO';
        CINZA = 'CINZA';
        global ciclo 
        ciclo = False;

        cor = [BRANCO]*self.NumeroVertices; # inicializa todos os vértices como BRANCO

        # verifica se todos os vértices foram visitados
        #Ou seja, se não há vértices pintados de brancos
        def e_conexo():
            return len(list(filter(lambda x:x==BRANCO, cor))) == 0; 

        # DFS recursiva
        def dfs_visita(u):
            cor[u] = CINZA;
            for j in self.ListaAdj[u]:
                if cor[j] == BRANCO:
                    dfs_visita(j);

                if(cor[j] == CINZA): # Verifica um Ciclo
                    global ciclo;
                    ciclo = True;

            cor[u] = PRETO;
            print(u, end='->');
        
        dfs_visita(v_inicio);

        print('\n')
        if(ciclo):
            print('Há um ciclo!');
            
        if(e_conexo()):
            print('Grafo conexo!');
        else:
            print('Grafo não conexo!');

G1 = Grafo(5, True);
G1.addVertice(0);
G1.addVertice(4);
G1.addVertice(2);
G1.addVertice(1);
G1.addVertice(3);


G1.addAresta(0,1);
G1.addAresta(1,2);
G1.addAresta(2,3);
G1.addAresta(0,4);
G1.addAresta(4,0);

G1.dfs(0); #Inicializa pelo vértice 0
G1.imprimeGrafo();
