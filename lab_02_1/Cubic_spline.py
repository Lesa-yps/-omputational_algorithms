from Newton import  find_Newton_coefs

# константы
MIN_COUNT_POINT = 4
POLYNOM_DEGREE = 3
Y_PART = 1
X_PART = 0

# находит вторую производную полинома Ньютона третьей степени в точке
def find_P_diff(new_arr):
    res_coefs = find_Newton_coefs(new_arr)
    b = res_coefs[1]
    c = res_coefs[2]
    x = new_arr[0][X_PART]
    return 2 * b + (6 * x - 2 * (new_arr[0][X_PART] + new_arr[1][X_PART] + new_arr[2][X_PART])) * c

# определяет граничные условия
def bound_cond(arr_start, cond):
    c_start = 0
    c_end = 0
    if cond == 2 or cond == 3:
        c_start = find_P_diff(arr_start[:(POLYNOM_DEGREE + 1)])
        if cond == 3:
            c_end = find_P_diff(arr_start[(- (POLYNOM_DEGREE + 1)):][::-1])
    return c_start, c_end

# вычисляет коффициент A сплайна
def calc_coef_A(arr_y):
    A = arr_y[:-1]
    return A

# вычисляет коффициент C сплайна
def calc_coef_C(arr_x, arr_y, cond):
    n = len(arr_x)
    C = [0] * (n - 1)
    # прямая прогонка
    kci = [0, 0]
    eta = [0, 0]
    for i in range(2, n):
        hi = arr_x[i] - arr_x[i - 1]
        hi_1 = arr_x[i - 1] - arr_x[i - 2]
        fi = - 3 * ((arr_y[i] - arr_y[i - 1]) / hi - (arr_y[i - 1] - arr_y[i - 2]) / hi_1)
        di = hi
        ai = hi_1
        bi = - 2 * (hi_1 + hi)
        kci_i = di / (bi - ai * kci[i - 1])
        eta_i = (fi + ai * eta[i - 1]) / (bi - ai * kci[i - 1])
        kci += [kci_i]
        eta += [eta_i]
    C[0], C[-1] = bound_cond([(arr_x[i], arr_y[i]) for i in range(n)], cond)
    # обратная прогонка
    for i in range(n - 2, 1, -1):
        C[i - 1] = kci[i] * C[i] + eta[i]
    return C

# вычисляет коффициент B сплайна
def calc_coef_B(arr_x, arr_y, C):
    B = list()
    for i in range(1, len(arr_x) - 1):
        hi = arr_x[i] - arr_x[i - 1]
        B += [(arr_y[i] - arr_y[i - 1]) / hi - (1/3) * hi  * (C[i] + 2 * C[i - 1])]
    hn = arr_x[-1] - arr_x[-2]
    B += [(arr_y[-1] - arr_y[-2]) / hn - (2/3) * hn * C[-1]]
    return B

# вычисляет коффициент D сплайна
def calc_coef_D(arr_x, arr_y, C):
    D = list()
    for i in range(1, len(arr_x) - 1):
        hi = arr_x[i] - arr_x[i - 1]
        D += [(C[i] - C[i - 1]) / (3 * hi)]
    hn = arr_x[-1] - arr_x[-2]
    D += [-C[-1] / (3 * hn)]
    return D

# вычисляет коффициенты сплайна
def calc_spline_coefs(arr_x, arr_y, cond):
    A = calc_coef_A(arr_y)
    C = calc_coef_C(arr_x, arr_y, cond)
    B = calc_coef_B(arr_x, arr_y, C)
    D = calc_coef_D(arr_x, arr_y, C)
    return A, B, C, D

# ищет в каком промежутке находится х
def find_ind_x(arr, x):
    ind = 1
    while (ind < len(arr) and x > arr[ind]):
        ind += 1
    return ind - 1

# вычисляет полином по найденным коэффициентам
def calc_polyn(arr_x, x, ind, coefs):
    A, B, C, D = coefs
    hi = x - arr_x[ind]
    yx = A[ind] + B[ind] * hi + C[ind] * hi**2 + D[ind] * hi**3
    return yx

# метод кубических сплайнов
def Cubic_spline_metod(arr_start, x, cond):
    arr_x = [i[X_PART] for i in arr_start]
    arr_y = [i[Y_PART] for i in arr_start]
    coefs = calc_spline_coefs(arr_x, arr_y, cond)
    ind = find_ind_x(arr_x, x)
    yx = calc_polyn(arr_x, x, ind, coefs)
    return yx