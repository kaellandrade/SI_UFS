'''
    Estrutura de dados para representar um grafo direcionado e não direcionado
'''
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
    
    def khanTopOrdem(self):
        # Armazena os graus dos vértices
        graus = [0] * (self.NumeroVertices);

        for i in self.ListaAdj:
            for j in self.ListaAdj[i]:
                graus[j] += 1;
        
        fila = [];
        for i in range(self.NumeroVertices):
            if(graus[i] == 0):
                fila.append(i);

        contador = 0;

        top_ordem = [];
        while(fila):
            u = fila.pop(0);
            top_ordem.append(u);

            for i in self.ListaAdj[u]:
                graus[i] -= 1;
                if graus[i] == 0:
                    fila.append(i);
            contador += 1;

        print(top_ordem);
        
G1 = Grafo(6, True);

G1.addVertice(0);
G1.addVertice(1);
G1.addVertice(2);
G1.addVertice(3);
G1.addVertice(4);
G1.addVertice(5);




G1.addAresta(5, 2);
G1.addAresta(5, 0);
G1.addAresta(4, 0);
G1.addAresta(4, 1);
G1.addAresta(2, 3);
G1.addAresta(3, 1);

G1.khanTopOrdem();

G1.imprimeGrafo();