import numpy as np
from matplotlib import pyplot as plt

from metodo_secante import metodo_secante as ms

# Datos del problema
m = 9500  # Masa en kg (9.5 toneladas)
K = 350e3  # Constante del resorte en N/m (350 N/mm)
Fm = 1650  # Fuerza máxima en N
xadm = 3.4 / 1000  # Desplazamiento admisible en metros (3.4 mm)
P = 1.0351603978423491  # Periodo en segundos
tolerancia = 1e-3  # Tolerancia para el método de la secante
num_puntos_por_ciclo = 500

num_ciclos = 10


h = P / num_puntos_por_ciclo


def graficar_solucion(tiempos, desplazamientos, fuerza_aplicada):

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Tiempo')
    ax1.set_ylabel('Desplazamiento', color=color)
    ax1.plot(tiempos, desplazamientos, label='Desplazamiento', color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Fuerza Aplicada', color=color)
    ax2.plot(tiempos, fuerza_aplicada, label='Fuerza Aplicada', linestyle='--', color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    # Marcar exactamente en el eje x los momentos donde se aplica y no se aplica la fuerza
    for i in range(num_ciclos):
        inicio_intervalo = i * P
        fin_intervalo = (i + 0.1) * P
        ax1.axvspan(inicio_intervalo, fin_intervalo, facecolor='yellow', alpha=0.3)

        # Marcar tiempos exactos
        ax1.axvline(x=inicio_intervalo, color='gray', linestyle='--', linewidth=0.5)
        ax1.axvline(x=fin_intervalo, color='gray', linestyle='--', linewidth=0.5)

        # Mostrar texto con los tiempos exactos
        ax1.text(inicio_intervalo, ax1.get_ylim()[1] * 0.9, f'Tiempo: {inicio_intervalo:.2f}s', rotation=90, fontsize=8)
        ax1.text(fin_intervalo, ax1.get_ylim()[1] * 0.9, f'Tiempo: {fin_intervalo:.2f}s', rotation=90, fontsize=8)

    fig.tight_layout()
    plt.title('Desplazamiento y Fuerza Aplicada en función del tiempo')
    plt.show()


def ec_dif(c):
    def ecuacion(x, v, t):
        # Duración de cada ciclo
        duracion_ciclo = P

        # Verificar si estamos dentro del golpe cíclico en el ciclo actual
        if 0 <= t % duracion_ciclo < 0.1 * P:
            golpe_ciclico = Fm
        else:
            golpe_ciclico = 0

        return (golpe_ciclico / m) - (c * v / m) - (K * x / m)

    return ecuacion


def rungekutta2(f, x0, y0, h, n):
    x = []
    y = []
    t = []
    x.append(x0)
    y.append(y0)
    t.append(0)

    for i in range(1, n + 1):
        x_i = x0 + i * h
        k1 = h * f(x0, y0, t[i-1])
        k2 = h * f(x_i, y0 + k1, t[i-1])

        x.append(x_i)
        y.append(y0 + 0.5 * (k1 + k2))
        t.append(t[i - 1] + h)

        x0 = x_i
        y0 = y[i]

    a = t[-1]
    b = x[-1]
    return [x, y, t]


# Función para calcular la amplitud deseada en función de "c"
def f(c):
    solution = rungekutta2(ec_dif(c), 0, 0, h, num_puntos_por_ciclo * 10)
    xmax = max(solution)  # Apply max to absolute values
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

    except Exception as e:
        print(f"Se produjo un error: {e}")


