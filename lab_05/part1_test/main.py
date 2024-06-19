# Талышева ИУ7-45Б лаба_5 выч_алг
from calc_diff import diff_f, Fx, len_vec
from Kramer import Kramer_method

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

def solve_task(n, max_iter, eps, xk):
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
    n = 2
    max_iter = 100
    eps = 0.001
    x0 = [0.13, -1.8]
    x = solve_task(n, max_iter, eps, x0)
    print("Result:", x)

if __name__ == "__main__":
    main()