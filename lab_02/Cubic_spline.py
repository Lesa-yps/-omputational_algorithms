from Inverse_mat import Inverse_mat_metod

Y_PART = 1
X_PART = 0

# составит матрицу коэффициентов сплайнов
def make_mat_coef(arr, cond):
    n = len(arr)
    matrix = list()
    arr_res = list()
    b_in_mat_start = 0
    d_in_mat_start = n
    c_in_mat_start = 2 * n
    a = [i[Y_PART] for i in arr]
    h = [(arr[i][X_PART] - arr[i - 1][X_PART]) for i in range(1, n)] # длина интервала
    for i in range(1, n):
        # уравнение чтоб кривая проходила через обе границы
        arr_res.append(arr[i][Y_PART] - a[i - 1])
        mat_new = [0] * 3 * n
        mat_new[b_in_mat_start + (i - 1)] = h[i - 1]
        mat_new[c_in_mat_start + (i - 1)] = h[i - 1] ** 2
        mat_new[d_in_mat_start + (i - 1)] = h[i - 1] ** 3
        matrix.append(mat_new)
        if (i < n):
            # уравнение чтоб первые производные на стыках совпали
            arr_res.append(0)
            mat_new = [0] * 3 * n
            mat_new[b_in_mat_start + (i - 1)] = 1
            mat_new[b_in_mat_start + i] = -1
            mat_new[c_in_mat_start + (i - 1)] = 2 * h[i - 1]
            mat_new[d_in_mat_start + (i - 1)] = 3 * h[i - 1] ** 2
            matrix.append(mat_new)
            # уравнение чтоб вторые производные на стыках совпали
            arr_res.append(0)
            mat_new = [0] * 3 * n
            mat_new[c_in_mat_start + i] = -1
            mat_new[c_in_mat_start + (i - 1)] = 1
            mat_new[d_in_mat_start + (i - 1)] = 3 * h[i - 1]
            matrix.append(mat_new)
    # C0 = 0
    arr_res.append(0)
    mat_new = [0] * 3 * n
    mat_new[c_in_mat_start + 0] = -1
    matrix.append(mat_new)
    # 2 * C(n-1) + 6 * D(n-1) * H(n - 1) = 0
    arr_res.append(0)
    mat_new = [0] * 3 * n
    mat_new[c_in_mat_start + (n - 1)] = 1
    mat_new[d_in_mat_start + (n - 1)] = 3 * h[-1]
    matrix.append(mat_new)
    return matrix, arr_res

# ищет в каком промежутке находится х
def find_ind_x(arr, x):
    ind = 0
    while (ind < len(arr) and x >= arr[ind][X_PART]):
        ind += 1
    return ind

# ищет по коэффициентам сплайнов у для х
def find_yx_coef(arr_coef, ind, x, arr_start):
    n = len(arr_start)
    b_in_mat_start = 0
    d_in_mat_start = n
    c_in_mat_start = 2 * n
    a_ind = arr_start[ind][Y_PART]
    b_ind = arr_coef[b_in_mat_start + ind]
    c_ind = arr_coef[c_in_mat_start + ind]
    d_ind = arr_coef[d_in_mat_start + ind]
    x_ind = arr_start[ind][X_PART]
    yx = a_ind + b_ind * (x - x_ind) + c_ind * (x - x_ind)**2 + d_ind * (x - x_ind)**3
    return yx

# метод кубических сплайнов
def Cubic_spline_metod(arr_start, x, cond):
    matrix, arr_res = make_mat_coef(arr_start, cond)
    arr_coef = Inverse_mat_metod(matrix, arr_res)
    ind = find_ind_x(arr_start, x)
    yx = find_yx_coef(arr_coef, ind, x, arr_start)
    return yx