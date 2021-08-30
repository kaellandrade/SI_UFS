from typing import Callable
import timeit


def calcTime(func:Callable) -> float:
    start = timeit.default_timer()
    func()
    stop = timeit.default_timer()
    return stop - start
