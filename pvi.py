def euler_mejorado(f, x0, y0, h, n):
    x = []
    y = []
    x.append(x0)
    y.append(y0)

    for i in range(1, n):
        t_i = i * h  # Variable de tiempo
        x_i = x0 + i * h
        # Predicción utilizando el método de Euler
        y_pred = y[i - 1] + h * f(t_i, x[i - 1], y[i - 1])

        # Corrección utilizando el promedio ponderado de las pendientes en dos puntos
        y_corr = y[i - 1] + (h / 2) * (f(t_i, x[i - 1], y[i - 1]) + f(t_i + h, x_i, y_pred))

        x.append(x_i)
        y.append(y_corr)

    return [x, y]