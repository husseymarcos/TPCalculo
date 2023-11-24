import math
import matplotlib.pyplot as plt
from typing import Callable, List, Tuple

# PVI: m⋅x′′(t) + c⋅x′(t) + k⋅x(t) = F(t)

# Datos del problema
m = 9500  # Masa en kg (9.5 toneladas)
K = 350e3  # Constante del resorte en N/m (350 N/mm)
Fm = 1650  # Fuerza máxima en N
P = 1.0351603978423491  # Período en segundos

# Runge-Kutta de segundo orden. Recibe una ecuación diferencial, unas condiciones iniciales y un valor de h.
# 'initial_conds' es una lista de tuplas, donde cada tupla es un par ordenado (x; y)
def euler_mejorado(diff_eq: Callable[[float, float, float], float], initial_conds: List[Tuple[float, float]], h: float) -> List[Tuple[float, float]]:
    solutions = [initial_conds[0]]  # Inicializa la lista de soluciones

    # Inicializa las variables de ciclo y tiempo
    current_time: float = 0

    # Bucle que verifica que se hagan 500 cálculos por período.
    while current_time < P:
        conds = solutions[-1] # Las condiciones iniciales de la iteracion actual (xi+1; yi+1) es la solucion de la iteracion previa (xi; yi)
        f1 = h * diff_eq(conds[1], conds[0], current_time)
        f2 = h * diff_eq(conds[1] + f1, conds[0] + h, current_time + h)
        yf = conds[0] + (1 / 2 * (f1 + f2))
        current_time += h # Incremento la variable que controla el bucle.
        solutions.append((conds[0] + h, yf))

    return solutions # Retorno una lista con las iteraciones.

# Función para la ecuación diferencial con la fuerza cíclica
def diff_eq(x, v, t):
    return (-456.341 * v/m) - (K * x / m) + Fm/m * math.cos(2 * math.pi * t / P)

if __name__ == '__main__':
    desired_points_per_cycle = 500
    # Calculo un valor de 'h' tal que haya 500 puntos por ciclo.
    h = P / desired_points_per_cycle

    # Simulación del sistema con el valor del coeficiente de amortiguamiento obtenido
    result = euler_mejorado(diff_eq, [(0, 0)], h)

    # Extracción de los resultados para graficar
    time_points = [point[0] for point in result]
    displacement_points = [point[1] for point in result]

    # Gráfico de la respuesta del sistema
    plt.plot(time_points, displacement_points, label=f'Coeficiente de amortiguamiento: {4778225.582:.3f}')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Desplazamiento')
    plt.legend()
    plt.show()
