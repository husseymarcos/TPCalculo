import math
import numpy as np

# PVI: m⋅x′′(t) + c⋅x′(t) + k⋅x(t) = F(t)

# Datos del problema
m = 9500  # Masa en kg (9.5 toneladas)
K = 350e3  # Constante del resorte en N/m (350 N/mm)
Fm = 1650  # Fuerza máxima en N
xadm = 3.4 / 1000  # Desplazamiento admisible en metros (3.4 mm)
P = 1.0351603978423491  # Periodo en segundos


# timesteps tiene que ser > 500
def euler_modificado(differential_equation, initial_condition, timesteps, h):
    solutions = [initial_condition[0]]  # Inicializa la lista de soluciones con el valor inicial
    y = initial_condition[0]  # Valor inicial
    for t in timesteps:
        f1 = differential_equation(t, y)
        f2 = differential_equation(t + h, y + h * f1)
        y = y + (h / 2) * (f1 + f2)
        solutions.append(y)
    return solutions

