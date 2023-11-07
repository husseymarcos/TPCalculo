from typing import Callable
import math


def metodo_secante(f: Callable[[float], float], x0: float, x1: float, err: float):
    if abs(x1 - x0) < err: return x1
    print([x0, x1])
    prox_x = x1 - ((f(x1) * (x0 - x1)) / (f(x0) - f(x1)))
    return metodo_secante(f, x1, prox_x, err)


if __name__ == '__main__':
    print(metodo_secante(lambda x: x - math.exp(-x) + x - 3, 1, 0.53788284, 0.001))
