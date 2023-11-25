from metodo_secante import metodo_secante as ms
from pvi import euler_mejorado
import numpy as np

# Datos del problema
m = 9500  # Masa en kg (9.5 toneladas)
K = 350e3  # Constante del resorte en N/m (350 N/mm)
Fm = 1650  # Fuerza máxima en N
xadm = 3.4 / 1000  # Desplazamiento admisible en metros (3.4 mm)
P = 1.0351603978423491  # Periodo en segundos
tolerancia = 1e-3  # Tolerancia para el método de la secante
h = P / 500  # Quiero 500 puntos por ciclo.
initial_conditions = [(0, 0)]  # Pares de valores (x;y)


# Ecuacion diferencial con la fuerza cíclica
def ec_dif(c):
    return lambda v, x: -(c / m) * v - (K / m) * x + (Fm / m) * np.cos(2 * np.pi / P)


# Función para calcular la amplitud deseada en función de "c"
def f(c):
    diff_eq_c = ec_dif(c)
    solution = euler_mejorado(diff_eq_c, initial_conditions, h)
    return solution[-1][1]  # Devuelve el valor en y de la última iteración del método.


# Función a usar con el método de la secante.
g = lambda c: f(c) - xadm

if __name__ == '__main__':
    try:
        # Valores iniciales para X0 y X1
        X0 = 0.1
        X1 = 0.2

        # Calcula el coeficiente de amortiguamiento "c" que evita vibraciones excesivas
        coeficiente_amortiguamiento = ms(g, X0, X1, tolerancia)

        print(f"El valor del coeficiente de amortiguamiento que evita vibraciones excesivas es: {coeficiente_amortiguamiento:.3f}")

        # Utiliza el coeficiente de amortiguamiento en la función f(c)
        amplitud_deseada = f(coeficiente_amortiguamiento)
        print(f"La amplitud deseada con el coeficiente de amortiguamiento obtenido es: {amplitud_deseada:.4f}")

    except Exception as e:
        print(f"Se produjo un error: {e}")