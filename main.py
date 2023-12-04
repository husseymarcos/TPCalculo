from metodo_secante import metodo_secante as ms
from pvi import euler_mejorado

# Datos del problema
m = 9500  # Masa en kg (9.5 toneladas)
K = 350e3  # Constante del resorte en N/m (350 N/mm)
Fm = 1650  # Fuerza máxima en N
xadm = 3.4 / 1000  # Desplazamiento admisible en metros (3.4 mm)
P = 10351603978423491.  # Periodo en segundos
tolerancia = 1e-3  # Tolerancia para el método de la secante
initial_conditions = [(0, 0)]  # Pares de valores (x;y)
num_puntos_por_ciclo = 500

h = P / num_puntos_por_ciclo


# La ecuación diferencial resulta en una f(x, v).
def fuerza(c):
    def F(t):
        # Término adicional para el golpe cíclico una vez por periodo
        if t % P == 0:
            return Fm
        else:
            return 0

    def ecuacion(x, v, t):
        # Devuelve la aceleracion x''
        ec_movimiento = - (c * v / m) - (K * x / m)

        # Término adicional para el golpe cíclico
        ec_golpe = F(t) / m

        return ec_movimiento + ec_golpe

    return ecuacion


# Función para calcular la amplitud deseada en función de "c"
def f(c):
    solution = euler_mejorado(fuerza(c), 0, 0, h, int(num_puntos_por_ciclo))
    sol = solution[1][-1]
    return sol


# Función a usar con el método de la secante.
g = lambda c: abs(f(c) - xadm)

if __name__ == '__main__':
    try:
        # Valores iniciales para X0 y X1
        X0 = 0.1
        X1 = 0.2

        # Calcula el coeficiente de amortiguamiento "c" que evita vibraciones excesivas
        coeficiente_amortiguamiento = ms(g, X0, X1, tolerancia)

        print(
            f"El valor del coeficiente de amortiguamiento que evita vibraciones excesivas es: {coeficiente_amortiguamiento:.3f} kg/s")

        # Utiliza el coeficiente de amortiguamiento en la función f(c)
        amplitud_deseada = f(coeficiente_amortiguamiento)
        print(f"La amplitud deseada con el coeficiente de amortiguamiento obtenido es: {amplitud_deseada:.4f}")

    except Exception as e:
        print(f"Se produjo un error: {e}")
