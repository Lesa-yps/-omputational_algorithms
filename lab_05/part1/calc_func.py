# функция дополняет метод Ньютона,
# вычисляя функцию и частные производные в точке

# помогает считать производные
def diff_f(numf, numx, vector):
    x, y, z = vector
    if numf == 1:
        if (numx == 1):
            return 2*x
        if (numx == 2):
            return 2*y
        return 2*z
    if numf == 2:
        if (numx == 1):
            return 4*x
        if (numx == 2):
            return 2*y
        return -4
    if (numx == 1):
        return 6*x
    if (numx == 2):
        return -4
    return 2*z

# считает значение функции в точке
def Fx(vector):
    x, y, z = vector
    f1 = x**2 + y**2 + z**2 - 1
    f2 = 2 * x**2 + y**2 -4 * z
    f3 = 3 * x**2 - 4 * y + z**2
    return [f1, f2, f3]
