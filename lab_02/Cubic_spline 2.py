from Newton import find_coefs

# константы
MIN_COUNT_POINT = 4
POLYNOM_DEGREE = 3
Y_PART = 1
X_PART = 0

# находит вторую производную полинома Ньютона третьей степени в точке
def find_P_diff(new_arr):
    res_coefs = find_coefs(new_arr)
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

# ищет в каком промежутке находится х
def find_ind_x(arr, x):
    ind = 0
    while (ind < len(arr) and x >= arr[ind][X_PART]):
        ind += 1
    if (ind == 0):
        ind += 1
    return ind

# метод кубических сплайнов
def Cubic_spline_metod(arr_start, x, cond):
    n = len(arr_start)
    h_arr = [(arr_start[i][X_PART] - arr_start[i - 1][X_PART]) for i in range(1, n)] #!!!
    sigma = [0]
    eta = [0]
    # прогонка "туда"
    for i in range(2, n - 1):
        Ai = h_arr[i - 1]
        Bi = -2 * (h_arr[i - 1] + h_arr[i])
        Di = h_arr[i]
        Fi = -3 * ((arr_start[i][Y_PART] - arr_start[i - 1][Y_PART])/h_arr[i] - (arr_start[i - 1][Y_PART] -  \
                                                                                 arr_start[i - 2][Y_PART]) / h_arr[i - 1])
        sigma.append(Di / (Bi - Ai * sigma[-1]))
        eta.append((Fi + Ai * eta[-1]) / (Bi - Ai * sigma[-2]))
    sigma.append(0)
    eta.append(0)
    # прогонка "обратно"
    c_start, c_end = bound_cond(arr_start, cond)
    c_arr = [c_end]
    for i in range(n - 3, -1, -1):
        c_arr = [sigma[i + 1] * c_arr[0] + eta[i + 1]] + c_arr
    c_arr = [c_start] + c_arr
    # находим остальные коэффициенты
    ind = find_ind_x(arr_start, x)
    x_ind = arr_start[ind][X_PART]
    c_ind = c_arr[ind]
    a_ind = arr_start[ind - 1][Y_PART]
    d_ind = - c_arr[-1] / (3 * h_arr[-1]) if (ind == n) else (c_arr[ind + 1] - c_arr[ind]) / (3 * h_arr[ind])
    if (ind == n):
        b_ind = (arr_start[-1][Y_PART] - arr_start[-2][Y_PART]) / h_arr[-1] - 2/3 * h_arr[-1] * c_arr[-1]
    else:
        b_ind = (arr_start[ind][Y_PART] - arr_start[ind - 1][Y_PART]) / h_arr[ind] - 1/3 * h_arr[ind] * (c_arr[ind + 1] + 2 * c_arr[ind])
    # высчитываем y
    yx = a_ind + b_ind * (x - x_ind) + c_ind * (x - x_ind)**2 + d_ind * (x - x_ind)**3
    print(x_ind, a_ind, b_ind, c_ind, d_ind, c_arr[ind + 1], c_arr[ind], yx)
    return yx