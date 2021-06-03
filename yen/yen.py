from __future__ import annotations, print_function
from graph import Graph;
from dijkstras import dijkstra_heap;
from vertex import Vertex;

def yen(G:Graph, de:int, para:int, K:int):
    #Determina o caminho principal usando Dijkstra
    A = [[]]*K; #Inicializa o vetor que irá aramzenar os caminhos mais curtos;
    A[0] = dijkstra_heap(G, de, para);

    # Inicializa a lista para armazenar os possíveis kth caminhos mais curtos.
    B = [];

    for k in range(1, K):
        #O nó spur varia do primeiro ao próximo ao último nó no caminho k-mais curto anterior
        for i in range(len(A[k-1]) - 2):
            # O nó de estimulação é recuperado do caminho anterior do K-Curtest, K - 1.
            spurNode = A[k-1][i];
            # A sequência de nós da fonte para o nó de estimulação do caminho anterior do K-Curtest.
            rootPath = A[k-1][i];
            print(rootPath);
            for path in A:
                if(rootPath == path[:i]):
                    #Remova os links que fazem parte dos caminhos mais curtos anteriores que compartilham o mesmo caminho da raiz.
                    G.remove_edge(i, i+1);

            for node in rootPath:
                if(node != spurNode):
                remove rootPathNode from Graph
                #Continuar...