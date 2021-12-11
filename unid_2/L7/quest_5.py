#!python3.8
from random import randrange


def escolha() -> int:
    '''
    Função Viciada
    SAIDA: Int 0 com 60% de probabilidade ou inteiro 1 com 40% de probabilidade.
    '''
    value = randrange(1, 11)

    if(value <= 6):
        return 0
    else:
        return 1


def escolhaJusta() -> int:
    '''
    ENTRADA: Dada uma função viciada.
    Escolha justa retornara uma probabilidade de 50% para ambos os casos de 
    escolha.
    SAIDA: 0 ou 1 Representando os casos da escolha.
    '''
    val1: int = escolha()
    val2: int = escolha()
    if(val1 == 0 and val2 == 1):
        return 0
    if(val1 == 1 and val2 == 0):
        return 1
    return escolhaJusta()


print(escolhaJusta())
