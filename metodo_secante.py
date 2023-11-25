from typing import Callable


def metodo_secante(f: Callable[[float], float], x0: float, x1: float, err: float):
    if abs(f(x0) - f(x1)) < 1e-10:
        # Si f0 y f1 son iguales o muy cercanos, ajusta x1 ligeramente para evitar divisiones por cero
        x1 += 1e-10
    if abs(x1 - x0) < err:
        return x1
    print([x0, x1])
    prox_x: float = x1 - ((f(x1) * (x0 - x1)) / (f(x0) - f(x1)))
    return metodo_secante(f, x1, prox_x, err)
