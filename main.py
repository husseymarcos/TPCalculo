from metodo_secante import metodo_secante
from pvi import euler_mejorado
from typing import List, Tuple
# Datos del problema
m = 9500  # Masa en kg (9.5 toneladas)
K = 350e3  # Constante del resorte en N/m (350 N/mm)
Fm = 1650  # Fuerza máxima en N
xadm = 3.4 / 1000  # Desplazamiento admisible en metros (3.4 mm)
P = 1.0351603978423491  # Periodo en segundos
h = 0.1
initial_conditions: List[Tuple[float, float]] = [(0, 0)] # Pares de valores (x;y)

# ED: lambda v, x: -(c / m) * v - (k / m) * x + (Fm / m)

# Ecuacion para usar en la tabla. Devuelve la ecuacion diferencial con el valor de 'c' que se le da.
def ec_dif(c):
    return lambda v, x: -(c / m) * v - (K / m) * x + (Fm / m)

#
def f(c): return euler_mejorado(ec_dif(c), initial_conditions, h)

# Ecuacion para la tabla. Resta Xadm a f(c)
#g = lambda c: f(c) - xadm

if __name__ == '__main__':
    #print(euler_mejorado(ec_dif(-60789.473684210534), initial_conditions, h))
    print(euler_mejorado(ec_dif(10), initial_conditions, h))
    #print(metodo_secante(g, 10, 15, 0.001))
