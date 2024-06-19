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

def calc_yacob(n, xk):
    # посчитали Якобиан
    W = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            W[i][j] = diff_f(i + 1, j + 1, xk)
    # решим слау
    neg_Fx = [-i for i in Fx(xk)]
    dx = Kramer_method(W, neg_Fx)
    #print(dx, W, neg_Fx)
    return dx

def Newton_method(max_iter, eps, xk):
    n = len(xk)
    for k in range(max_iter + 1):
        dx = calc_yacob(n, xk)
        xk_old = xk.copy()  # Создаем копию xk_old
        for i in range(n):
            xk[i] = xk_old[i] + dx[i]  # Вычитаем соответствующие элементы из xk_old
        S = len_vec(dx)
        if S < eps:
            return xk
    print("Максимальное количество итераций превышено. Точность не достигнута.")
    return xk

def main():
    max_iter = 100
    eps = 0.0001
    #x0 = [0.8, 0.5, 0.35]
    x0 = [1, 1, 1]
    x = Newton_method(max_iter, eps, x0)
    print("Result:", x)

if __name__ == "__main__":
    main()