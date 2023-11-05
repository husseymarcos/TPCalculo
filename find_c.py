import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize

# Datos del problema
m = 9500  # Masa en kg (9.5 toneladas)
c_initial_guess = np.array([0.1])  # Valor inicial del coeficiente de amortiguamiento (ajústalo según sea necesario)
k = 350e3  # Constante del resorte en N/m (350 N/mm)
Fm = 1650  # Fuerza máxima en N
xadm = 3.4 / 1000  # Desplazamiento admisible en metros (3.4 mm)
P = 1.0351603978423491  # Periodo en segundos


# Paso 1: Definir la ecuación diferencial
def system(t, y, c):
    x, v = y
    F_t = Fm * np.sin(2 * np.pi * t / P)

    dxdt = v
    dvdt = (F_t - k * x - c * v) / m

    return [dxdt, dvdt]


# Paso 2: Definir la función para calcular el desplazamiento
def displacement_difference(c):
    sol = solve_ivp(system, t_span, initial_conditions, args=(c,), t_eval=np.linspace(*t_span, 1000))
    x_calculated = sol.y[0]
    return x_calculated[-1] - xadm  # Diferencia con el desplazamiento deseado


# Paso 3: Resolución de la ecuación diferencial
t_span = (0, 10)  # Rango de tiempo
initial_conditions = [0, 0]  # Condición inicial [x0, v0]

# Paso 4: Encontrar el valor óptimo de c
result = minimize(displacement_difference, c_initial_guess, method='Nelder-Mead', tol=1e-6)

# Paso 5: Resultado
optimal_c = result.x[0]
print(f"El coeficiente de amortiguamiento óptimo es: {optimal_c:.3f}")
