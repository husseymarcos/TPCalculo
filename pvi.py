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
def euler_mejorado(diff_eq: Callable[[float, float], float], initial_conds: List[Tuple[float, float]], h: float,
                   P: float) -> List[Tuple[float, float]]:
    solutions = [initial_conds[0]]  # Inicializa la lista de soluciones
    current_time: float = 0

    while current_time <= P:
        conds = solutions[-1]  # Condiciones iniciales de la iteración actual (xi+1, yi+1) es la solución de la iteración previa (
        # xi, yi)

        # Calcular k1 y k2 usando la ecuación diferencial
        k1 = h * diff_eq(conds[0], conds[1])
        k2 = h * diff_eq(conds[0] + h, conds[1] + k1)

        # Calcular el siguiente valor de la solución usando el método de Euler mejorado
        yf = conds[1] + (1 / 2 * (k1 + k2))

        # Incrementar el tiempo
        current_time += h

        # Agregar la solución a la lista
        solutions.append((conds[0] + h, yf))

    return solutions


if __name__ == '__main__':

    # Verifico el valor del coeficiente de amortiguamiento obtenido.
    result = euler_mejorado(lambda t, v: (-122748.180 * v / m) - (K * (v*t) / m) + (Fm / m) * math.cos(2 * math.pi / P) * t, [(0, 0)], h, P)
    print("Valor de la ecuación diferencial evaluada en el 'c' hallado = ", result[-1][1], "m")
