from graph import Graph
from vertex import Vertex

if (__name__ == '__main__'):
    redeFluxo: Graph[Vertex] = Graph([
        Vertex('S', True),  # 0 (É afonte)
        Vertex('A', ),  # 1
        Vertex('B', ),  # 2
        Vertex('C', ),  # 3
        Vertex('D', ),  # 4
        Vertex('T', False, True),  # 5 (É o sorvedouro)

    ])
    redeFluxo.add_edge_by_indices(0, 1, 4)
    redeFluxo.add_edge_by_indices(0, 3, 3)
    redeFluxo.add_edge_by_indices(1, 2, 4)
    redeFluxo.add_edge_by_indices(2, 3, 3)
    redeFluxo.add_edge_by_indices(2, 5, 2)
    redeFluxo.add_edge_by_indices(4, 5, 6)
    redeFluxo.add_edge_by_indices(3, 4, 6)
    redeFluxo.calculateMaxFlow(0,5);
    print(redeFluxo);
    print(sum(edge.fluxo for edge in redeFluxo._edges[0]));