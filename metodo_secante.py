from typing import Callable
import math


def metodo_secante(f: Callable[[float], float], x0: float, x1: float, err: float):
    if (abs(f(x1) - f(3.4/1000))) < err: return x1
    print([x0, x1])
    f0 = f(x0)
    f1 = f(x1)
    next_x = x1 - f1 * (x0 - x1) / (f0 - f1)
    return metodo_secante(f, x1, next_x, err)


