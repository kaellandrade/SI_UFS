from vertex import Vertex;
from graph import Graph;

#! Inicializa um vértice com distância 0;
def initialize_single_source(G:Graph, V: Vertex) -> None:
    V.dist = 0