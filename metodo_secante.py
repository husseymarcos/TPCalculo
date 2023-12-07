from typing import Callable


def metodo_secante(f: Callable[[float], float], x0: float, x1: float, err: float):
    """
        Método de la secante para encontrar la raíz de una función.

        Parameters:
            - f: La función cuya raíz se está buscando.
            - x0: Primer valor de la aproximación inicial.
            - x1: Segundo valor de la aproximación inicial.
            - err: Tolerancia para la convergencia.

        Returns:
            - La aproximación de la raíz.
        """
    x_next = x1
    x_prev = x0

    while abs((x_next - x_prev)) > err:
        # Calcular el siguiente valor de x usando el método de la secante
        x_temp = x_next - f(x_next) * (x_next - x_prev) / (f(x_next) - f(x_prev))

        # Actualizar los valores de x para la siguiente iteración
        x_prev = x_next
        x_next = x_temp
    return x_next


def prueba_funcion(x: float) -> float:
    return x ** 2 - 4


if __name__ == "__main__":
    # Valores iniciales para x0 y x1
    x0 = 1
    x1 = 3

    # Tolerancia para la convergencia
    tolerancia = 1e-5

    # Aplicar el método de la secante
    raiz_aproximada = metodo_secante(prueba_funcion, x0, x1, tolerancia)

    # Imprimir el resultado
    print(f"Aproximación de la raíz: {raiz_aproximada}")
