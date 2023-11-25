from typing import Callable, List, Tuple
import matplotlib.pyplot as plt
import numpy as np


def diff_eq(y, t):
    return -2 * y


def analytical_solution(t):
    return np.exp(-2 * t)


def euler_mejorado(diff_eq: Callable[[float, float], float], initial_conds: List[Tuple[float, float]], h: float) -> List[Tuple[float, float]]:
    solution = []

    for y0, t0 in initial_conds:
        # Inicializar variables
        t = t0
        y = y0

        # Almacenar las condiciones iniciales en la solución
        solution.append((t, y))

        # Iterar hasta alcanzar el punto final
        while t < 10:  # Puedes ajustar el límite superior según tus necesidades
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
    # Datos del problema
    initial_conditions = [(1.0, 0.0)]  # Condiciones iniciales para y(t) = 1.0 en t = 0.0
    h = 0.01  # Tamaño del paso
    P = 10  # Periodo arbitrario

    # Obtener soluciones con el método de Euler mejorado
    numerical_solution = euler_mejorado(diff_eq, initial_conditions, h)

    # Obtener soluciones analíticas
    t_values = np.arange(0, P, h)

    # Redefinir la función analítica para usar el nuevo rango de tiempo
    analytical_values = [analytical_solution(t) for t in t_values]

    # Graficar las soluciones
    plt.plot([y[1] for y in numerical_solution], label='Numerical Solution')
    plt.plot(analytical_values, label='Analytical Solution', linestyle='--')
    plt.xlabel('Time')
    plt.ylabel('y(t)')
    plt.legend()
    plt.show()

