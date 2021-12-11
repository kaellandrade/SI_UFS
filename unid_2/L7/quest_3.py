#!python3.8
from copy import copy


class Item:
    def __init__(self, peso, valor) -> None:
        self.peso = peso
        self.valor = valor


class No:
    def __init__(self, nivel, lucro,  peso, limite) -> None:
        self.nivel = nivel
        self.lucro = lucro
        self.limite = limite
        self.peso = peso


def bound(v: No, W, matriz_itens):
    '''
    se o peso superar a capacidade da mochila, retorne 0 conforme o limite esperado
    '''
    if(v.peso >= W):
        return 0
    # inicializa o limite vinculado ao lucro pelo lucro atual
    lucro_vinculado = v.lucro

    '''
        Começa a incluir itens do índice 1 mais para o índice de item atual
    '''
    j = v.nivel + 1
    totalPeso = v.peso

    while (j < len(matriz_itens)) and ((totalPeso + matriz_itens[j][0]) <= W):
        totalPeso += matriz_itens[j][0]
        lucro_vinculado += matriz_itens[j][1]
        j += 1

    # Se k não for n, inclua o último item parcialmente para o limite superior do lucro
    if(j < len(matriz_itens)):
        lucro_vinculado += (W - totalPeso) * \
            (matriz_itens[j][1] / matriz_itens[j][0])

    return lucro_vinculado


def mochila_branch_bound(W: int, matriz_itens: list):
    # Classificando itens baseados no valor/unidade
    matriz_itens.sort(key=lambda item: item[1]/item[0], reverse=True)

    Q = []  # Fila

    u: No = No(-1, 0, 0, 0)  # No inicial

    Q.append(u)
    '''
        One by one extract an item from decision tree
        compute profit of all children of extracted item
        and keep saving maxProfit
    '''
    lucro_maximo = 0
    while(Q):
        v: No = No(None, None, None, None)
        u = Q.pop(0)
        # Se for o nó inicial
        if(u.nivel == -1):
            v.nivel = 0
        if(u.nivel == len(matriz_itens)-1):
            continue

        # Caso contrário, se não o último nó, então incremente o nível
        # e calcular o lucro dos nós filhos.

        v.nivel = u.nivel + 1

        '''
        Tomando o item do nível atual, adiciona o peso e o valor do nível atual 
        ao peso e valor do nó u
        '''
        v.peso = u.peso + matriz_itens[v.nivel][0]  # peso
        v.lucro = u.lucro + matriz_itens[v.nivel][1]  # valor
        '''
        Se o peso acumulado for menor que W e o lucro for maior que o 
        lucro anterior, atualize o maxprofit
        '''
        if(v.peso <= W and v.lucro > lucro_maximo):
            lucro_maximo = v.lucro

        '''
        Obtenha o limite superior do lucro para decidir se deve adicionar v a Q ou não.
        '''

        v.limite = bound(v, W, matriz_itens)

        '''
        Se o valor vinculado for maior do que o lucro, 
        apenas coloque na fila para uma consideração mais detalhada
        '''
        if(v.limite > lucro_maximo):
            Q.append(copy(v))

        '''
        Faça a mesma coisa, mas sem levar o item na mochila
        '''

        v.peso = u.peso
        v.lucro = u.lucro
        v.limite = bound(v, W, matriz_itens)
        if(v.limite > lucro_maximo):
            Q.append(v)
    return lucro_maximo


CAPACIDADE = 100
matriz_itens = [
    [4.5, 40],
    [7.2, 42],
    [5.5, 25],
    [3.5, 12],
    [10.1, 1],
    [5.0, 10]
]
print(mochila_branch_bound(CAPACIDADE, matriz_itens))
