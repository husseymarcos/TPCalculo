from metodo_secante import secante_con_validacion, metodo_secante
from pvi import euler_mejorado
from typing import List, Tuple

# Datos del problema
m = 9500  # Masa en kg (9.5 toneladas)
K = 350e3  # Constante del resorte en N/m (350 N/mm)
Fm = 1650  # Fuerza máxima en N
xadm = 3.4 / 1000  # Desplazamiento admisible en metros (3.4 mm)
P = 1.0351603978423491  # Periodo en segundos
h = P / 500 # Quiero 500 puntos por ciclo.
initial_conditions: List[Tuple[float, float]] = [(0, 0)]  # Pares de valores (x;y)


# ED: lambda v, x: -(c / m) * v - (k / m) * x + (Fm / m)

# Ecuacion para usar en la tabla. Devuelve la ecuacion diferencial con el valor de 'c' que se le da.
def ec_dif(c):
    return lambda v, x: -(c / m) * v - (K / m) * x + (Fm / m)


# Función para calcular la amplitud deseada en función de "c"
def f(c):
    solution = euler_mejorado(ec_dif(c), initial_conditions, h)
    return solution[-1][1]  # Devuelve el valor en y de la última amplitud obtenida


def secante_con_validacion2(f, x0, x1, err):
    f0 = f(x0)
    f1 = f(x1)

    if abs(f0 - f1) < 1e-10:
        # Si f0 y f1 son iguales o muy cercanos, ajusta x1 ligeramente para evitar divisiones por cero
        x1 += 1e-10

    # Continúa con el método de la secante
    coeficiente_amortiguamiento = secante_con_validacion2(f, x0, x1, err)
    return coeficiente_amortiguamiento


if __name__ == '__main__':
    # Valores iniciales para X0 y X1
    X0 = 2.0  # Valor arbitrario
    X1 = 4.0  # Valor arbitrario

    # Tolerancia para el método de la secante
    tolerancia = 1e-3

    # Calcula el coeficiente de amortiguamiento "c" que evita vibraciones excesivas
    coeficiente_amortiguamiento = metodo_secante(f, X0, X1, tolerancia)
    print(f"El coeficiente de amortiguamiento que evita vibraciones excesivas es: {coeficiente_amortiguamiento:.3f}")
