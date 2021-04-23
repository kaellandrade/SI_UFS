'''
    Implementação dos algoritmos de Kahn e Busca em profundidade para encontrar uma ordenação linear. 
    Os algoritmos devem ser testados com os dois grafos dos slides.
'''

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

        graus_entrada = [0] * self.NumeroVertices; # inicializa todos os vértices com grau de entrada 0
        vertices_vistados = 0;
        fila_graus_0 = [];
        ordenacao_top = []; #Aqui será armazenada a ordenação topologica

        #Realiza a contagem dos graus de entrada para cada vértice
        for v in self.ListaAdj:
            for u in self.ListaAdj[v]:
                graus_entrada[u]+=1;
        
        #Para cada vertice com graude entrada 0 será adicionado na fila;
        for v in range(self.NumeroVertices):
            if(graus_entrada[v] == 0) : fila_graus_0.append(v);

        while(fila_graus_0):
            vertice = fila_graus_0.pop(0);
            ordenacao_top.append(vertice);

            for v in self.ListaAdj[vertice]:
                graus_entrada[v] -= 1;
                if(graus_entrada[v] == 0):
                    fila_graus_0.append(v);

            vertices_vistados += 1;
        if(vertices_vistados == self.NumeroVertices):
            print("Ordenação TOP: {}".format(self.__imprimeAdjList(ordenacao_top)));
        else:
            print('Não há uma ordenação, pois G contém ciclos!');

G1 = Grafo(5, True);

G1.addVertice(0);
G1.addVertice(1);
G1.addVertice(2);
G1.addVertice(3);
G1.addVertice(4);




G1.addAresta(0, 1);
G1.addAresta(0, 2);
G1.addAresta(2, 3);
G1.addAresta(3, 4);


G1.khanTopOrdem();

# G1.imprimeGrafo();