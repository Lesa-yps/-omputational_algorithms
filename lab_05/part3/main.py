# Талышева ИУ7-45Б лаба_5 выч_алг
from calc_func import diff_f, Fx
from Kramer import Kramer_method
from math import sqrt

# находит длину вектора неизвестной размерности
def len_vec(vec1):
    S = 0
    for i in range(len(vec1)):
        S += vec1[i]**2
    return sqrt(S)

def calc_yacob(x_near, x_start, x_fin):
    xk = x_near[1:-1]
    n = len(xk)
    # посчитали Якобиан
    W = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            W[i][j] = diff_f(i + 1, j + 1, x_near, x_start, x_fin)
    # решим слау
    neg_Fx = [-i for i in Fx(x_near, x_start, x_fin)]
    dx = Kramer_method(W, neg_Fx)
    #print(dx, W, neg_Fx)
    return dx

def Newton_method(max_iter, eps, x_near, x_start, x_fin):
    xk = x_near[1:-1]
    n = len(xk)
    for k in range(max_iter + 1):
        dx = calc_yacob(x_near, x_start, x_fin)
        xk_old = xk.copy()  # Создаем копию xk_old
        for i in range(n):
            xk[i] = xk_old[i] + dx[i]  # Вычитаем соответствующие элементы из xk_old
            x_near[i + 1] = xk[i]
        S = len_vec(dx)
        if S < eps:
            return x_near
    print("Максимальное количество итераций превышено. Точность не достигнута.")
    return x_near

# задаёт начальное приближение по формуле y = 2 * x + 1
def make_near(x_start, x_fin, n):
    h = (x_fin - x_start) / (n - 1)
    y_near = []
    x_arr = []
    for i in range(n):
        x = x_start + h * i
        y_near.append(2 * x + 1)
        x_arr.append(x)
    return y_near, x_arr

def draw_graph(x_arr, y_arr):
    print(x_arr, "\n", y_arr)

def main():
    max_iter = 100
    eps = 0.0001
    n = 6
    x_start, x_fin = 0, 1
    y_near, x_arr = make_near(x_start, x_fin, n)
    y_arr = Newton_method(max_iter, eps, y_near, x_start, x_fin)
    draw_graph(x_arr, y_arr)

if __name__ == "__main__":
    main()