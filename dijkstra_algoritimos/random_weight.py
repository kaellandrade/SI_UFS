from __future__ import annotations
from random import randrange


"""
Recebe um intervalo [A,B] e retorna um valor entre [A,B]
"""
def random_weight(a: int, b: int) -> int:
    return randrange(a, b + 1)
