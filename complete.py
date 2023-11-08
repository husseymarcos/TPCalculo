import math

# Datos del problema
m = 9500  # Masa en kg (9.5 toneladas)
K = 350e3  # Constante del resorte en N/m (350 N/mm)
Fm = 1650  # Fuerza máxima en N
xadm = 3.4 / 1000  # Desplazamiento admisible en metros (3.4 mm)
P = 1.0351603978423491  # Periodo en segundos

# Paso de cálculo mínimo para tener al menos 500 puntos por ciclo
desired_points_per_cycle = 500
total_cycles = 2 * math.pi / P
total_points = int(desired_points_per_cycle * total_cycles)
h = P / total_points  # Ajuste el paso de cálculo


# Función para calcular la amplitud deseada en función de "c"
def calcular_amplitud_deseada(c):
    initial_conditions = [(xadm, 0)]  # Condición inicial (desplazamiento y velocidad)

    # Método de Euler mejorado para resolver la ecuación diferencial
    def euler_mejorado(diff_eq, initial_conds, h):
        solutions = [initial_conds[0]]  # Inicializa la lista de soluciones
        current_cycles = 0
        current_time = 0

        while current_cycles < total_cycles:
            initial_conditions = solutions[-1]

            while current_time < P:
                conds = initial_conditions
                x_incremented = conds[0] + h
                f1 = h * diff_eq(conds[0], conds[1])
                f2 = h * diff_eq(x_incremented, conds[1] + f1)
                yf = conds[1] + (1 / 2 * (f1 + f2))
                solutions.append((x_incremented, yf))
                initial_conditions = (x_incremented, yf)
                current_time += h

            current_cycles += 1
            current_time = 0

        return solutions

    # Función para la ecuación diferencial
    def diff_eq(x, v):
        return -(c / m) * v - (K / m) * x + (Fm / m)

    # Resuelve la ecuación diferencial con Euler mejorado y devuelve la última amplitud
    solution = euler_mejorado(diff_eq, initial_conditions, h)
    return solution[-1][0]


# Método de la secante para encontrar el coeficiente de amortiguación
def secante_con_validacion(f, x0, x1, err):
    f0 = f(x0)
    f1 = f(x1)

    while abs(f1 - f0) > err:
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        x0, x1 = x1, x2
        f0, f1 = f1, f(x2)

    return x1


if __name__ == '__main__':
    # Valores iniciales para X0 y X1
    X0 = 2.0  # Valor arbitrario
    X1 = 4.0  # Valor arbitrario

    # Tolerancia para el método de la secante
    tolerancia = 1e-3

    # Calcula el coeficiente de amortiguación "c" que evita vibraciones excesivas
    coeficiente_amortiguamiento = secante_con_validacion(calcular_amplitud_deseada, X0, X1, tolerancia)
    print(f"El coeficiente de amortiguamiento que evita vibraciones excesivas es: {coeficiente_amortiguamiento:.3f}")
