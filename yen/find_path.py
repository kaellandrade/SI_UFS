from vertex import Vertex

"""
Dado dois vértices de um grafo, será retronada uma lista
com a sequancia do caminho mais se existir, caso contrário
será retornado [];
"""


def find_path(s: Vertex, v: Vertex, path=[]) -> None:
    if (v == s):
        return [s] + path
    elif (v.parent == None): 
        return []
    else:
        return find_path(s, v.parent, [v]+path)
