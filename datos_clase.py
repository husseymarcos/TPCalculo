import numpy as np
from matplotlib import pyplot as plt

from metodo_secante import metodo_secante as ms

# Datos del problema
m = 10000  # Masa en kg (9.5 toneladas)
K = 600e3  # Constante del resorte en N/m (350 N/mm)
Fm = 1200  # Fuerza máxima en N
xadm = 1.5 / 1000  # Desplazamiento admisible en metros (3.4 mm)
P = 0.8111  # Periodo en segundos
tolerancia = 1e-3  # Tolerancia para el método de la secante
num_puntos_por_ciclo = 500
h1 = P / num_puntos_por_ciclo


def ec_dif(c):
    def ecuacion(x, v, t):
        # Número total de ciclos
        num_ciclos = 10

        # Duración de cada ciclo
        duracion_ciclo = P

        # Determinar el número de ciclo actual
        num_ciclo_actual = int(t / duracion_ciclo)

        # Verificar si estamos dentro del golpe cíclico en el ciclo actual
        if 0 <= t % duracion_ciclo < 0.1 * P:
            golpe_ciclico = Fm
        else:
            golpe_ciclico = 0

        # Aplicar el golpe cíclico solo durante los primeros 10 ciclos
        if num_ciclo_actual < num_ciclos:
            return (golpe_ciclico / m) - (c * v / m) - (K * x / m)
        else:
            # Sin golpe cíclico después de los primeros 10 ciclos
            return - (c * v / m) - (K * x / m)

    return ecuacion


def Euler(f, x0, y0, h, n):
    x = []  # desplazamientos
    v = []  # velocidad
    t = []

    x.append(x0)
    v.append(y0)
    t.append(0)

    for i in range(1, n):
        t_actual = t[-1] + h
        v.append(v[-1] + h * f(x[-1], v[-1], t_actual))
        x.append(x[-1] + v[-1] * h)
        t.append(t_actual)

    return t, x


# Función para calcular la amplitud deseada en función de "c"
def f(c):
    tiempos, solution = Euler(ec_dif(c), 0, 0, h1, num_puntos_por_ciclo * 10)
    xmax = max(solution)
    return xmax


# Función a usar con el método de la secante.
g = lambda c: f(c) - xadm

if __name__ == '__main__':
    try:
        # Valores iniciales para X0 y X1
        X0 = 20
        X1 = 30

        # Calcula el coeficiente de amortiguamiento "c" que evita vibraciones excesivas
        coeficiente_amortiguamiento = ms(g, X0, X1, tolerancia)

        print(
            f"El valor del coeficiente de amortiguamiento que evita vibraciones excesivas es: {coeficiente_amortiguamiento:.3f} kg/s")

        # Utiliza el coeficiente de amortiguamiento en la función f(c)
        amplitud_deseada = f(coeficiente_amortiguamiento)
        print(f"La amplitud deseada con el coeficiente de amortiguamiento obtenido es: {amplitud_deseada:.4f}")

        # Verifica para c = 30
        c = 30
        solucion_c_30 = Euler(ec_dif(c), 0, 0, h1, num_puntos_por_ciclo * 10)
        xmax_c_30 = max(solucion_c_30[1])
        g_c_30 = g(c)

        print()
        print(f"Para c = 30:")
        print(f"xmax calculado: {xmax_c_30:.5f}")
        print(f"g(c) calculado: {g_c_30:.5f}")

    except Exception as e:
        print(f"Se produjo un error: {e}")
