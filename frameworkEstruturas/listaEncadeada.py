from __future__ import annotations


class Node:
    def __init__(self, conteudo) -> None:
        self.data = conteudo
        self.prox = None


class ListaEncadeada:
    def __init__(self) -> None:
        self.cabeca = None

    @property
    def inicializaLista(self):
        self.cabeca = Node('CABEÇA')

    def __str__(self) -> str:
        atual: Node = self.cabeca
        elementos: str = ''
        while(atual):
            elementos += f'{atual.data} -> '
            atual = atual.prox
        return f'{elementos} NULL'

    def adicionar(self, elemento, node):
        newNode: Node = Node(elemento)
        newNode.prox = node.prox
        node.prox = newNode


if __name__ == '__main__':
    myLink = ListaEncadeada()

    myLink.inicializaLista

    myLink.adicionar(10, myLink.cabeca)

    print(myLink)
