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
    def F(t):

        # Encuentra el tiempo relativo dentro del ciclo actual
        t_rel = t - (int(t // P) * P)

        p_cicl = 0.1 * P

        # Término adicional para el golpe cíclico una vez por periodo
        if 0 <= t_rel < p_cicl:
            return Fm
        else:
            return 0

    def ecuacion(x, v, t):
        return F(t) / m - (c * v / m) - (K * x / m)

    return ecuacion


def Euler(f, x0, y0, h, n):
    x = []
    y = []  # y = velocidad
    x.append(x0)
    y.append(y0)

    for i in range(1, n):
        t = h * (i - 1)
        x.append(x[i - 1] + y[i - 1] * h)
        y.append(y[i - 1] + h * f(x[i - 1], y[i - 1], t))

    return [x, y]


# Función para calcular la amplitud deseada en función de "c"
def f(c):
    solution = Euler(ec_dif(c), 0, 0, h1, num_puntos_por_ciclo * 10)
    xmax = max(solution[0])
    return xmax / 10


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
        xmax_c_30 = max(solucion_c_30[0])
        g_c_30 = g(c)

        print()
        print(f"Para c = 30:")
        print(f"xmax calculado: {xmax_c_30:.5f}")
        print(f"g(c) calculado: {g_c_30:.5f}")

    except Exception as e:
        print(f"Se produjo un error: {e}")
