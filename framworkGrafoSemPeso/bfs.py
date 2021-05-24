from graph import Graph
from vertex import Vertex


def bfs(G, startV):

    startV.cor = 'CINZA'
    startV.dist = 0

    fila = []
    fila.append(startV)

    while (fila):
        u = fila.pop(0)
        for v in G.neightbors_for_vertex(u):
            if (v.cor == 'BRANCO'):  #se ainda não foi descoberto
                v.cor = 'CINZA'
                v.dist = u.dist + 1
                v.parent = u
                fila.append(v)
        u.cor = 'PRETO'


def print_path(s, v):
    if (v == s): 
        print(s.label)
    elif (v.parent == None):  #Se for None
        print('Não existe caminho de {} para {}'.format(s, v))
    else:
        print_path(s, v.parent)
        print(v.label)


if (__name__ == '__main__'):
    cidade_grafo: Graph[Vertex] = Graph([
        Vertex('Seattle'), #0
        Vertex('San Francisco'),#1
        Vertex('Los Angeles'),#2
        Vertex('Riverside'),#2
        Vertex('Phoenix'),#3
        Vertex('Chicago'),#5
        Vertex('Boston'),#6
        Vertex('New York'),#7
        Vertex('Atlanta'),#8
        Vertex('Miami'),#9
        Vertex('Dallas'),#10
        Vertex('Houston'),#11
        Vertex('Detroint'),#12
        Vertex('Philadelphia'),#13
        Vertex('Washington')#14
    ])
    #adiciona todos os vértives que estão em vertices
    cidade_grafo.add_edge_by_indices(0, 5)
    cidade_grafo.add_edge_by_indices(0, 1)
    cidade_grafo.add_edge_by_indices(9, 11)
    cidade_grafo.add_edge_by_indices(1, 3)
    cidade_grafo.add_edge_by_indices(4, 11)
    cidade_grafo.add_edge_by_indices(1, 2)
    cidade_grafo.add_edge_by_indices(2, 3)
    cidade_grafo.add_edge_by_indices(2, 4)
    cidade_grafo.add_edge_by_indices(3, 4)
    cidade_grafo.add_edge_by_indices(3, 5)
    cidade_grafo.add_edge_by_indices(4, 10)
    cidade_grafo.add_edge_by_indices(10, 5)
    cidade_grafo.add_edge_by_indices(10, 8)
    cidade_grafo.add_edge_by_indices(10, 11)
    cidade_grafo.add_edge_by_indices(11, 8)
    cidade_grafo.add_edge_by_indices(8, 5)
    cidade_grafo.add_edge_by_indices(8, 14)
    cidade_grafo.add_edge_by_indices(8, 9)
    cidade_grafo.add_edge_by_indices(9, 14)
    cidade_grafo.add_edge_by_indices(5, 12)
    cidade_grafo.add_edge_by_indices(12, 6)
    cidade_grafo.add_edge_by_indices(12, 14)
    cidade_grafo.add_edge_by_indices(12, 7)
    cidade_grafo.add_edge_by_indices(6, 7)
    cidade_grafo.add_edge_by_indices(7, 13)
    cidade_grafo.add_edge_by_indices(13, 14)

    bfs(cidade_grafo, cidade_grafo.vertex_at(7));
    print_path(cidade_grafo.vertex_at(7), cidade_grafo.vertex_at(9));
    print(cidade_grafo);
