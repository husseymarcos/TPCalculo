def Euler(f, x0, y0, b, n):
    h = (b-x0)/n
    for i in range(n):
        y1 = y0 + h*f(x0,y0)
        x0 = x0+h
        y0 = y1
    return [x0, y0]