from math import sqrt, sin, cos

# помогает считать производные
def diff_f(numf, numx, vector):
    x, y = vector
    if numf == 1:
        if (numx == 1):
            return cos(x - 0.5)
        return -1
    if (numx == 1):
        return 2
    return -sin(y)

# считает значение функции в точке
def Fx(vector):
    x, y = vector
    f1 = sin(x - 0.5) - y - 1.5
    f2 = 2 * x - cos(y) - 0.6
    return [f1, f2]

# находит длину вектора неизвестной размерности
def len_vec(vec1):
    S = 0
    for i in range(len(vec1)):
        S += vec1[i]**2
    return sqrt(S)
