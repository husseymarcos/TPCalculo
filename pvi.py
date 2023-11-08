import math
# import numpy as np
from typing import Callable, List, Tuple

# PVI: m⋅x′′(t) + c⋅x′(t) + k⋅x(t) = F(t)

# Datos del problema
m = 9500  # Masa en kg (9.5 toneladas)
K = 350e3  # Constante del resorte en N/m (350 N/mm)
Fm = 1650  # Fuerza máxima en N
xadm = 3.4 / 1000  # Desplazamiento admisible en metros (3.4 mm)
P = 1.0351603978423491  # Período en segundos

# Runge-Kutta de segundo orden. Recibe una ecuación diferencial, unas condiciones iniciales y un valor de h.
# 'initial_conds' es una lista de tuplas, donde cada tupla es un par ordenado (x; y)
def euler_mejorado(diff_eq: Callable[[float, float], float], initial_conds: List[Tuple[float, float]], h: float) -> List[Tuple[float, float]]:
    solutions = [initial_conds[0]]  # Inicializa la lista de soluciones

    # Inicializa las variables de ciclo y tiempo
    current_time: float = 0

    # Bucle que verifica que se hagan 500 cálculos por período.
    while current_time < P:
        conds = solutions[-1] # Las condiciones iniciales de la iteracion actual (xi+1; yi+1) es la solucion de la iteracion previa (xi; yi)
        f1 = h * diff_eq(conds[0], conds[1])
        f2 = h * diff_eq(conds[0] + h, conds[1] + f1)
        yf = conds[1] + (1 / 2 * (f1 + f2))
        current_time += h # Incremento la variable que controla el bucle.
        solutions.append((conds[0] + h, yf))

    return solutions # Retorno una lista con las iteraciones.


if __name__ == '__main__':
    desired_points_per_cycle = 500
    # Calculo un valor de 'h' tal que hayan 500 puntos por ciclo.
    h = P / desired_points_per_cycle

    # Verifico el valor del coeficiente de amortiguamiento obtenido.
    result = euler_mejorado(lambda v, x: (-456.3 * v/m) - (K * x / m) + Fm/m, [(0, 0)], h)
    print(result)

