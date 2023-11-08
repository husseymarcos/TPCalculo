import math
from typing import Callable


def secante_con_validacion(f, x0, x1, err):
    f0 = f(x0)
    f1 = f(x1)

    if abs(f0 - f1) < 1e-10:
        # Si f0 y f1 son iguales o muy cercanos, maneja esta situación adecuadamente
        print("Valores iniciales muy cercanos. Considera cambiar los valores iniciales o ajustar la tolerancia.")
        return None

    # Continúa con el método de la secante
    coeficiente_amortiguamiento = secante_con_validacion(f, x0, x1, err, 5)
    return coeficiente_amortiguamiento


def metodo_secante(f: Callable[[float], float], x0: float, x1: float, err: float):
    #if abs(x1 - x0) < err: return x1
    if (abs(f(x1) - f(3.4 / 1000))) < err: return x1
    print([x0, x1])
    prox_x = x1 - ((f(x1) * (x0 - x1)) / (f(x0) - f(x1)))
    return metodo_secante(f, x1, prox_x, err)
    #f0 = f(x0)
    #f1 = f(x1)
    #next_x = x1 - f1 * (x0 - x1) / (f0 - f1)
    #return metodo_secante(f, x1, next_x, err)


if __name__ == '__main__':
    # Ejemplo.
    #print(metodo_secante(lambda x: x - math.exp(-x) + x - 3, 1, 0.53788284, 0.001))
    print(metodo_secante(lambda x: x**2 - 4, 7, 5, 0.001))
