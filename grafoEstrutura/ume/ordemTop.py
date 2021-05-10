from graph import Graph;
'''
Algoritmo de Khan para encontrar uma ordenaçã top
'''
def ordemTop(grafo):
    top = []; #ordenação TOP
    fila = [];
    visitados = 0;
    indeg = [0]*grafo.N_vertices; #Graus de entrada
        
    for v in grafo.adj:
        for a in grafo.adj[v]:
            indeg[a] += 1;
    
    for v in range(grafo.N_vertices):
        if(indeg[v] == 0): fila.append(v);
    
    while(fila): #Enquanto houver elemento na fila
        u = fila.pop(0); # Primeiro elemento da fila
        top.append(u);

        for v in grafo.adj[u]:
            indeg[v] -= 1; #Remoção virtual do arco 
            if(indeg[v] == 0 ): 
                fila.append(v);
        visitados += 1;
    

    if(visitados >= grafo.N_vertices): #se for verdade há uma ordenação top
        top = list(map(lambda x:str(x), top));
        return '->'.join(top);
        return top;
        
    else:
        return 'Não há ordenção Topológica';

g1 = Graph(8, True);
g1.iniciar_vertices();
# g1.grafoRandom();
# print(g1.adj);
g1.addArestas(0,1);
g1.addArestas(0,2);
g1.addArestas(0,4);
g1.addArestas(1,2);
g1.addArestas(2,3);
g1.addArestas(4,2);
g1.addArestas(4,5);
g1.addArestas(5,3);
g1.addArestas(6,4);
g1.addArestas(6,7);
g1.addArestas(7,5);

print(ordemTop(g1));