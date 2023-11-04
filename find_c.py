import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize

# Paso 1: Definir la ecuación diferencial
def system(t, y, c):
    # y[0] es la posición x, y[1] es la velocidad dx/dt
    x, v = y
    k = 350  # Rigidez (N/m)
    m = 9500  # Masa (kg)
    Fm = 1650  # Fuerza máxima (N)
    P = 1.0351603978423491  # Periodo (s)
    
    # Define la carga cíclica F(t) aquí (puede ser una función de t)
    F_t = Fm * np.sin(2 * np.pi * t / P)

    dxdt = v
    dvdt = (F_t - k * x - c * v) / m

    return [dxdt, dvdt]

# Paso 2: Resolución de la ecuación diferencial
t_span = (0, 10)  # Rango de tiempo
initial_conditions = [0, 0]  # Condición inicial [x0, v0]

# Definir una función que calcule el desplazamiento en función de c
def displacement(c):
    sol = solve_ivp(system, t_span, initial_conditions, args=(c,), t_eval=np.linspace(*t_span, 1000))
    return sol.y[0][-1]

# Paso 3: Encontrar el valor de c
xadm = 0.0034  # Desplazamiento admisible (3.4 mm en metros)
c_initial_guess = 0.1  # Adivinanza inicial para c

result = minimize(lambda c: (displacement(c) - xadm) ** 2, c_initial_guess, method='Nelder-Mead', tol=1e-6)

# Paso 4: Resultado
optimal_c = result.x[0]
print(f"El coeficiente de amortiguamiento óptimo es: {optimal_c:.3f}")
