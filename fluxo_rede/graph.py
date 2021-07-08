#!/usr/bin/env python3
from typing import Generic, Tuple, TypeVar, List
from edge import WeightedEdge
from vertex import Vertex

V = TypeVar('V')  # Tipo de vértices no grafo;


class Graph(Generic[V]):
    def __init__(self, vertices: List[V] = [], directed: bool = False) -> None:
        self._vertices: List[V] = vertices  # Lista de adj
        self._edges: List[List[WeightedEdge]] = [
            [] for _ in vertices
        ]  # Para cada vértices será será criada uma listas de listas de conexões
        self.directed = directed

    @property
    def vertex_count(self) -> int:
        return len(self._vertices)  # Número total de vértices;

    @property
    def edge_count(self) -> int:
        return sum(map(len, self._edges))  # Número de arestas;

    # Restaura o estado inicial dos vértices
    @property
    def resetGraph(self) -> None:
        for v in self._vertices:
            v.dist = float('inf')
            v.parent = None
            v.cor = 'BRANCO'
    # TODO: colocar fora do grafo

    def getPath(self, u, v, path):
        if u == v:
            return path
        for edge in self._edges[u]:
            residualCapacity = edge.capacidade - edge.fluxo
            if residualCapacity > 0 and not (edge, residualCapacity) in path:
                result = self.getPath(
                    edge.v, v, path + [(edge, residualCapacity)])
                if result != None:
                    return result
    # TODO: Colocar fora algoritkmo Ford-Fulkerson

    def calculateMaxFlow(self, fonte, fim):
        source = self.vertex_at(fonte)
        sink = self.vertex_at(fim)
        if source == None or sink == None:
            return "Network does not have source and sink"
        path = self.getPath(self.index_of(source), self.index_of(sink), [])
        while path != None:
            flow = min(edge[1] for edge in path)
            for edge, res in path:
                edge.fluxo += flow
                edge.arestaRetorno.fluxo -= flow
            path = self.getPath(self.index_of(source), self.index_of(sink), [])
        # return sum(edge.fluxo for edge in self.network[source.name])

    # Adicona um vértice ao grafo e devolve o seu índice
    def add_vertex(self, vertex: V) -> int:
        self._vertices.append(vertex)
        self._edges.append([])
        # Adiciona uma lista vazia paindera conectar as arestas
        return self.vertex_count - 1
        # Devolve o índice do vértice adicionado

    # Este é um grafo não direcionado
    # portanto, sempre adicionamos arestas nas duas direções
    def __add_edge(self, edge: WeightedEdge) -> None:
        self.retorno = edge.reversed()
        edge.arestaRetorno = self.retorno
        self.retorno.arestaRetorno = edge
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(self.retorno)

    # Adicona uma arestas usando índices dos vértices (método auxiliar)
    def add_edge_by_indices(self, u: int, v: int, capacidade: float) -> None:
        edge: WeightedEdge = WeightedEdge(u, v, capacidade)
        self.__add_edge(edge)

    # Adiciona uma aresta concultando os índices dos vértices (método auxiliar)
    def add_edge_by_vertices(self, first: V, second: V, capacidade: float) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v, capacidade)

    # Encontra o vértice em um índice específico
    def vertex_at(self, index: int) -> V:
        return self._vertices[index]

    # Encontra um índice de um vértice no grafo
    def index_of(self, vertex: V) -> int:
        return self._vertices.index(vertex)

    # Encontra os vértices aos quais um vértice com determinado índice está conectado
    def neightbors_for_index(self, index: int) -> List[Tuple[V, float]]:
        distance_tuples: List[Tuple[V, float]] = []
        for edge in self.edges_for_index(index):
            distance_tuples.append(
                (self.vertex_at(edge.v), edge.fluxo, edge.capacidade))
        return distance_tuples

    # Consulta o índice de um vértice e encontra seus vizinhos (método auxiliar)
    def neightbors_for_vertex(self, vertex: V) -> List[V]:
        return self.neightbors_for_index(self.index_of(vertex))

    # Devolve todas as arestas associadas a um vértice em um índice
    def edges_for_index(self, index: int) -> List[WeightedEdge]:
        return self._edges[index]

    # Consulta um índice de um vértece e devolve suas arestas (método auxiliar)
    def edges_for_vertex(self, vertex: V) -> List[WeightedEdge]:
        return self.edges_for_index(self.index_of(vertex))

    #!(Função Peso) Dado dois vértices será mostrando a capacidade de suas arestas caso haja conexão
    #!Caso contrário será retronado infinito
    def get_weight_with_index(self, u: int, v: int) -> float:
        for edge in self.edges_for_index(u):
            if (edge.v == v):
                return edge.capacidade
        return float('inf')

    def get_weight_with_vertex(self, u: Vertex, v: Vertex) -> float:
        return self.get_weight_with_index(self.index_of(u), self.index_of(v))

    # Exibição do grafo
    def __str__(self) -> str:
        desc: str = ''
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} => {list(map(lambda edge:(edge[0].label, edge[1], edge[2]),self.neightbors_for_index(i)))}\n"
        return desc
