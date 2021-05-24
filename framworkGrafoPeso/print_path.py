from vertex import Vertex


#Dado dois vértices de um grafo, será mostrado o caminho mínimo caso exista
def print_path(s: Vertex, v: Vertex) -> None:
    if (v == s):
        print(s)
    elif (v.parent == None):  #Se for None
        print('Não existe caminho de {} para {}'.format(s.label, v.label))
    else:
        print_path(s, v.parent)
        print(v)