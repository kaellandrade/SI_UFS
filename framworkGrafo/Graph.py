from typing import Generic, TypeVar, List, Optional;
from edge import Edge;

V = TypeVar('V') #Tipo de vértices no grafo;

class Graph(Generic[V]):
    def __init__(self, vertices:List[V]=[]) -> None:
        self._vertices:List[V] = vertices; #Lista de adj
        self._edges: List[List[Edge]] = [[] for _ in vertices] #Para cada vértices será será criada uma listas de listas de conexões

    @property
    def vertex_count(self) -> int:
        return len(self._vertices) #Número total de vértices;
    
    @property
    def edge_count(self) -> int:
        return sum(map(len, self._adges)) #Número de arestas;
    
    #Adicona um vértice ao grafo e devolve o seu índice
    def add_vertix(self, vertex:V) -> int:
        self._vertices.append(vertex);
        self._edges.append([]); #Adiciona uma lista vazia para conectar as arestas
        return self.vertex_count - 1; #Devolve o índice do vértice adicionado

    #Este é um grafo não direcionado
    #portanto, sempre adicionamos arestas nas duas direções
    def add_edge(self, edge:Edge) ->None:
        self._edges[edge.u].append(edge);
        self._edges[edge.v].append(edge.reversed());

    # Adicona uma arestas usando índices dos vértices (método auxiliar)
    def add_edge_by_indices(self, u:int, v:int) -> None:
        edge:Edge(u,v);
        self.add_edge(edge);

    # Adicoina uma aresta concultando os índices dos vértices (método auxiliar)
    def add_edge_by_vertices(self, first:V, second:V) -> None:
        u: int = self._vertices.index(first);
        v: int = self._vertices.index(second);
        self.add_edge_by_indices(u, v);
    
    # Encontra o vértice em um índie específico
    def vertex_at(self, index:int)->V:
        return self._vertices[index];
    
    #Encontra um índice de um vértice no grafo
    def index_of(self, vertix:V)->int:
        return self._vertices.index(V);
    
    #Encontra os vértices aos quais um vértice com determinado índice está conectado
    def neightbors_for_index(self, index:int)->List[V]:
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]));



g1 = Graph(['mikael', 'paulo', 'pedro']);
print(g1._vertices);
ed = Edge(0,1);
ed2 = Edge(0,2);

g1.add_edge(ed);
g1.add_edge(ed2);

print(g1._edges);
print(g1.neightbors_for_index(0));