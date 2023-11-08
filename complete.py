import math
from typing import List, Tuple, Callable

# Datos del problema
m = 9500  # Masa en kg (9.5 toneladas)
K = 350e3  # Constante del resorte en N/m (350 N/mm)
Fm = 1650  # Fuerza máxima en N
xadm = 3.4 / 1000  # Desplazamiento admisible en metros (3.4 mm)
P = 1.0351603978423491  # Periodo en segundos
initial_conditions: List[Tuple[float, float]] = [(0, 0)]  # Pares de valores (x;y)

# Paso de cálculo mínimo para tener al menos 500 puntos por ciclo
desired_points_per_cycle = 500
total_cycles = 2 * math.pi / P
total_points = int(desired_points_per_cycle * total_cycles)
h = P / total_points  # Ajuste el paso de cálculo


def euler_mejorado(diff_eq: Callable[[float, float, float], float], initial_conds: List[Tuple[float, float]], h: float,
                   c: float) -> List[Tuple[float, float]]:
    solutions = [initial_conds[0]]  # Inicializa la lista de soluciones

    # Inicializa las variables de ciclo y tiempo
    current_time = 0

    # Bucle exterior: realiza la integración para un ciclo
    while current_time < P:
        conds = solutions[-1]
        f1 = h * diff_eq(conds[0], conds[1], c)
        f2 = h * diff_eq(conds[0] + h, conds[1] + f1, c)
        yf = conds[1] + (1 / 2 * (f1 + f2))
        current_time += h
        solutions.append((conds[0] + h, yf))

    return solutions


def f(c):
    return euler_mejorado(ec_dif, initial_conditions, h, c)[-1][1]


def ec_dif(v, x, c):
    return -(c / m) * v - (K / m) * x + (Fm / m)


# Método de la secante para encontrar el coeficiente de amortiguación
def secante_con_validacion(g, x0, x1, err):
    g0 = g(x0)
    g1 = g(x1)

    while abs(g1 - g0) > err:
        x2 = x1 - g1 * (x1 - x0) / (g1 - g0)
        x0, x1 = x1, x2
        g0, g1 = g1, g(x2)

    return x1


if __name__ == '__main__':
    # Valores iniciales para X0 y X1
    X0 = 0.01  # Valor arbitrario
    X1 = 0.02  # Valor arbitrario

    # Tolerancia para el método de la secante
    tolerancia = 1e-3

    # Calcula el coeficiente de amortiguación "c" que evita vibraciones excesivas
    coeficiente_amortiguamiento = secante_con_validacion(f, X0, X1, tolerancia)
    print(f"El coeficiente de amortiguamiento que evita vibraciones excesivas es: {coeficiente_amortiguamiento:.3f}")
