#!/usr/bin/env python3
from typing import Generic, Tuple, TypeVar, List
from edge import WeightedEdge
from vertex import Vertex

V = TypeVar('V')  #Tipo de vértices no grafo;

"""
Recebe uma lista de vértices para cosntrução do grafo;
"""
class Graph(Generic[V]):
    def __init__(self, vertices: List[V] = [], directed: bool = False) -> None:
        self._vertices: List[V] = vertices  #Lista de adj
        self._edges: List[List[WeightedEdge]] = [
            [] for _ in vertices
        ]  #Para cada vértices será será criada uma listas de listas de conexões
        self.directed = directed

    @property
    def vertex_count(self) -> int:
        return len(self._vertices)  #Número total de vértices;

    @property
    def edge_count(self) -> int:
        return sum(map(len, self._edges))  #Número de arestas;

    #Restaura o estado inicial dos vértices
    @property
    def resetGraph(self) -> None:
        for v in self._vertices:
            v.dist = float('inf');
            v.parent = None;
            v.cor = 'BRANCO';

    #Adicona um vértice ao grafo e devolve o seu índice
    def add_vertex(self, vertex: V) -> int:
        self._vertices.append(vertex)
        self._edges.append([])
        #Adiciona uma lista vazia para conectar as arestas
        return self.vertex_count - 1
        #Devolve o índice do vértice adicionado

    #Este é um grafo não direcionado
    #portanto, sempre adicionamos arestas nas duas direções
    def __add_edge(self, edge: WeightedEdge) -> None:
        self._edges[edge.u].append(edge)
        if (not self.directed):
            self._edges[edge.v].append(edge.reversed())

    # Adicona uma arestas usando índices dos vértices (método auxiliar)
    def add_edge_by_indices(self, u: int, v: int, weight: float) -> None:
        edge: WeightedEdge = WeightedEdge(u, v, weight)
        self.__add_edge(edge)

    # Adiciona uma aresta concultando os índices dos vértices (método auxiliar)
    def add_edge_by_vertices(self, first: V, second: V, weight: float) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v, weight)

    # Encontra o vértice em um índice específico
    def vertex_at(self, index: int) -> V:
        return self._vertices[index]

    #Encontra um índice de um vértice no grafo
    def index_of(self, vertex: V) -> int:
        return self._vertices.index(vertex)

    #Encontra os vértices aos quais um vértice com determinado índice está conectado
    def neightbors_for_index(self, index: int) -> List[Tuple[V, float]]:
        distance_tuples: List[Tuple[V, float]] = []
        for edge in self.edges_for_index(index):
            distance_tuples.append((self.vertex_at(edge.v), edge.weight))
        return distance_tuples

    #Consulta o índice de um vértice e encontra seus vizinhos (método auxiliar)
    def neightbors_for_vertex(self, vertex: V) -> List[V]:
        return self.neightbors_for_index(self.index_of(vertex))

    #Devolve todas as arestas associadas a um vértice em um índice
    def edges_for_index(self, index: int) -> List[WeightedEdge]:
        return self._edges[index]

    #Consulta um índice de um vértece e devolve suas arestas (método auxiliar)
    def edges_for_vertex(self, vertex: V) -> List[WeightedEdge]:
        return self.edges_for_index(self.index_of(vertex))

    #!(Função Peso) Dado dois vértices será mostrando o peso de suas arestas caso haja conexão
    #!Caso contrário será retronado infinito
    def get_weight_with_index(self, u: int, v: int) -> float:
        for edge in self.edges_for_index(u):
            if (edge.v == v):
                return edge.weight
        return float('inf')

    def get_weight_with_vertex(self, u: Vertex, v: Vertex) -> float:
        return self.get_weight_with_index(self.index_of(u), self.index_of(v))

    #Exibição do grafo
    def __str__(self) -> str:
        desc: str = ''
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} => {list(map(lambda edge:(edge[0].label, edge[1]),self.neightbors_for_index(i)))}\n"
        return desc
