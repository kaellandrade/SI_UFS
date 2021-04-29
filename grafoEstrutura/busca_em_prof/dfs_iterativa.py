#!/usr/bin/env python3
import functools;

class Grafo():
    def __init__(self, NumeroVertices, direcionado = False):
        self.Direcionado = direcionado; 
        self.NumeroVertices = NumeroVertices;
        self.ListaAdj = dict();

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
        print(f"\nLista ADJ");
        for item in self.ListaAdj:
            print(f"[{item}]:", self.__imprimeAdjList(self.ListaAdj.get(item)));
    
    def __imprimeAdjList(self, lista):
        if(len(lista) == 0):
            return 'NULL';
        else:
            return " -> ".join(tuple(map(lambda x:str(x),lista)))+' -> NULL';
    
    def dfs_iterativa(self,v_inicio):
        pilha_nos = []; # armazena os nós que estão sendo visitados
        pilha_visitados = [False]*self.NumeroVertices; # Inicializa todos os vértices como não visitados;
        resultado_da_varredura = [];


        pilha_nos.append(v_inicio);
        while(pilha_nos):
            removido = pilha_nos.pop();

            if(not pilha_visitados[removido]):
                resultado_da_varredura.append(removido);
                pilha_visitados[removido] = True;

            for w in self.ListaAdj[removido]:
                if(not pilha_visitados[w]):
                    pilha_nos.append(w);

        print(self.__imprimeAdjList(resultado_da_varredura));

        # Verifica se todos os vértices doram visitados
        def conexo():
            return functools.reduce(lambda a,b:a and b, pilha_visitados);
        if(conexo()):
            print('Grafo conexo!');
        else:
            print('Grafo não conexo!')

G1 = Grafo(5,True); #Grafo direcionado
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

G1.dfs_iterativa(4); #Inicializa pelo vértice 0
G1.imprimeGrafo();
