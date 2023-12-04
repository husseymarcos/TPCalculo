def euler_mejorado(f, x0, y0, h, n):
    x = []
    y = []
    x.append(x0)
    y.append(y0)

    for i in range(1, n):
        t_i = (i - 1) * h
        x_i = x[i - 1]
        y_pred = y[i - 1] + h * f(x_i, y[i - 1], t_i)
        y_corr = y[i - 1] + (h / 2) * (f(x_i, y[i - 1], t_i) + f(x_i + h, y_pred, t_i + h))
        x.append(x_i + h)
        y.append(y_corr)

    return [x, y]
