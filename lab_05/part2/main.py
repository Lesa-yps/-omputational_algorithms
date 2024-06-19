# Талышева ИУ7-45Б лаба_5 выч_алг (done)
from math import sqrt, exp, pi

def f(t):
    return exp(-t ** 2 / 2)

def Integ(a, b):
    if a == b:
        return 0
    minus = 1
    if a > b:
        minus = -1
        a, b = b, a
    N = 10
    if (b - a) > 1:
        N *= (b - a)
    h = (b - a) / (N - 1)
    res = (f(a) + f(b)) * h/2
    for i in range(1, int(N - 1)):
        res += h * f(a + i * h)
    return res * minus
        

def Fi(x):
    return 2/sqrt(2 * pi) * Integ(0, x)

def solve_task(low, high, target, max_iter, eps):
    mid = (low + high) / 2
    if (abs(Fi(mid) - target) <= eps):
        return mid
    if low > high:
        high, low = low, high
    for i in range(max_iter):
        if Fi(mid) > target:
            high = mid
        else:
            low = mid
        mid = (low + high) / 2
        if (abs(Fi(mid) - target) <= eps):
            return mid
    print("Максимальное количество итераций превышено. Точность не достигнута.")
    return mid

def main():
    target = -0.5
    low = -15
    high = 1
    max_iter = 100
    eps = 0.0001
    x = solve_task(low, high, target, max_iter, eps)
    print("Result:", x)

if __name__ == "__main__":
    main()