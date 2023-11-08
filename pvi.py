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


def euler_mejorado(diff_eq: Callable[[float, float], float], initial_conds: List[Tuple[float, float]], h: float) -> List[Tuple[float, float]]:
    solutions = [initial_conds[0]]  # Inicializa la lista de soluciones

    # Inicializa las variables de ciclo y tiempo
    current_time = 0

    # Bucle exterior: realiza la integración para un ciclo
    while current_time < P:
        conds = solutions[-1]
        f1 = h * diff_eq(conds[0], conds[1])
        f2 = h * diff_eq(conds[0] + h, conds[1] + f1)
        yf = conds[1] + (1 / 2 * (f1 + f2))
        current_time += h
        solutions.append((conds[0] + h, yf))

    return solutions

def calcular_amplitud_deseada(c):
    # Función para calcular la amplitud deseada en función de "c"
    initial_conditions = [(xadm, 0)]  # Condición inicial (desplazamiento y velocidad)
    solution = euler_mejorado(lambda x, v: -(c / m) * v - (K / m) * x + (Fm / m), initial_conditions, h)
    return solution[-1][0]  # Devuelve la última amplitud obtenida



if __name__ == '__main__':
    # Cálculo del paso de cálculo para tener al menos 500 puntos por ciclo
    desired_points_per_cycle = 500
    total_cycles = 2 * math.pi / P
    total_points = int(desired_points_per_cycle * total_cycles)
    h = P / total_points  # Ajuste el paso de cálculo

    # Llama a la función euler_mejorado con el nuevo valor de h
    result = euler_mejorado(lambda x, y: 2*x*y + x, [(0, 0)], h)
    print(result)

