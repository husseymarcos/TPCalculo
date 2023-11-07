import math
# import numpy as np
from typing import Callable, List, Tuple

# PVI: m⋅x′′(t) + c⋅x′(t) + k⋅x(t) = F(t)

# Datos del problema
m = 9500  # Masa en kg (9.5 toneladas)
K = 350e3  # Constante del resorte en N/m (350 N/mm)
Fm = 1650  # Fuerza máxima en N
xadm = 3.4 / 1000  # Desplazamiento admisible en metros (3.4 mm)
P = 1.0351603978423491  # Periodo en segundos


def euler_mejorado(diff_eq: Callable[[float, float], float], initial_conds: List[Tuple[float, float]], h: float, desired_cycles: float) -> List[Tuple[float, float]]:
    solutions = [initial_conds[0]]  # Inicializa la lista de soluciones
    P = 1.0351603978423491  # Período en segundos

    # Calcula el número total de ciclos necesarios
    total_cycles = 2 * math.pi / P

    # Inicializa las variables de ciclo y tiempo
    current_cycles = 0
    current_time = 0

    # Bucle exterior: verifica si hemos alcanzado la cantidad deseada de ciclos
    while current_cycles < total_cycles:
        # Inicializa las condiciones iniciales para este ciclo
        initial_conditions = solutions[-1]
        iteration = 0

        # Bucle interior: realiza la integración para un ciclo
        while current_time < P:
            conds = initial_conditions
            x_incremented = conds[0] + h
            f1 = h * diff_eq(conds[0], conds[1])
            f2 = h * diff_eq(x_incremented, conds[1] + f1)
            yf = conds[1] + (1 / 2 * (f1 + f2))
            solutions.append((x_incremented, yf))
            initial_conditions = (x_incremented, yf)
            current_time += h
            iteration += 1

        # Actualiza el número de ciclos completados
        current_cycles += 1
        current_time = 0

    return solutions
