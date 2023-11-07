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


def euler_mejorado(diff_eq: Callable[[float, float], float], initial_conds: List[Tuple[float, float]], h: float,
                   timesteps: int) -> List[Tuple[float, float]]:
    iteration = 0
    solutions = [initial_conds[iteration]]
    cycles_per_period = 6.069769787  # Número de ciclos deseados por período
    P = 1.0351603978423491  # Período en segundos

    # Calcula el número de ciclos en el período deseado
    total_cycles = cycles_per_period * P

    # Calcula el paso de tiempo necesario para al menos 500 puntos por ciclo
    h = P / (total_cycles * 500)

    timesteps = int(total_cycles * 500)  # Ajusta el número de pasos para alcanzar el tiempo deseado

    while iteration < timesteps:
        conds = initial_conds[iteration]
        x_incremented = conds[0] + h
        f1 = h * diff_eq(conds[0], conds[1])
        f2 = h * diff_eq(x_incremented, conds[1] + f1)
        yf = conds[1] + (1 / 2 * (f1 + f2))
        solutions.append((x_incremented, yf))
        initial_conds.append((x_incremented, yf))
        iteration += 1
    return solutions
