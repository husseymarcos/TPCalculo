import math
from typing import Callable, List, Tuple

# Datos del problema
m = 9500  # Masa en kg (9.5 toneladas)
K = 350e3  # Constante del resorte en N/m (350 N/mm)
Fm = 1650  # Fuerza máxima en N
xadm = 3.4 / 1000  # Desplazamiento admisible en metros (3.4 mm)
P = 1.0351603978423491  # Período en segundos
desired_points_per_cycle = 500
# Calculo un valor de 'h' tal que hayan 500 puntos por ciclo.
h = P / desired_points_per_cycle


# Runge-Kutta de segundo orden. Recibe una ecuación diferencial, unas condiciones iniciales y un valor de h.
# 'initial_conds' es una lista de tuplas, donde cada tupla es un par ordenado (x; y)
def euler_mejorado(diff_eq: Callable[[float, float], float], initial_conds: List[Tuple[float, float]], h: float) -> List[Tuple[float, float]]:
    solution = []

    for y0, t0 in initial_conds:
        # Inicializar variables
        t = t0
        y = y0

        # Almacenar las condiciones iniciales en la solución
        solution.append((t, y))

        # Iterar hasta alcanzar el punto final
        while t < 100:  # Puedes ajustar el límite superior según tus necesidades
            # Calcular k1 y k2
            k1 = h * diff_eq(y, t)
            k2 = h * diff_eq(y + k1, t + h)

            # Calcular el siguiente valor de y usando la fórmula del método de Euler mejorado
            y = y + 0.5 * (k1 + k2)

            # Incrementar el tiempo
            t += h

            # Agregar el punto a la solución
            solution.append((t, y))

    return solution


if __name__ == '__main__':

    # Verifico el valor del coeficiente de amortiguamiento obtenido.
    result = euler_mejorado(lambda x, v: (-420.069 * v / m) - (K * x / m) + (Fm / m) * math.cos(2 * math.pi / P),
                            [(0, 0)], h)
    print("Valor de la ecuación diferencial evaluada en el 'c' hallado = ", result[-1][1], "m")
