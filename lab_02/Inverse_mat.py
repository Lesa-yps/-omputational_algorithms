# вычислит определитель
def calc_def(arr):
    n = len(arr)
    # базовые случаи
    if n <= 0:
        return 0
    if n == 1:
        return arr[0][0]
    if n == 2:
        return arr[0][0] * arr[1][1] - arr[1][0] * arr[0][1]
    # для матриц размером > 2 для каждого элемента первой строки
    res = 0
    for i in range(n):
        # вычисляем минор элемента arr[0][i]
        minor = [[arr[row][col] for col in range(n) if col != i] for row in range(1, n)]
        # вычисляем определитель минора и добавляем его с учетом знака
        res += arr[0][i] * calc_def(minor) * ((-1) ** i)
    return res

#  транспонируем матрицу
def rev_mat(arr):
    n = len(arr)
    m = len(arr[0])
    arr_t = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            arr_t[j][i] = arr[i][j]
    return arr_t

# находит союзную матрицу (из алгебраических дополнений)
def union_mat(arr):
    n = len(arr)
    m = len(arr[0])
    arr_res = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            minor = [[arr[w][z] for z in range(m) if w != j] for w in range(n) if w != i]
            arr_res[i][j] = calc_def(minor) * (-1)**(i + j)
    return arr_res

# делит матрицу на число
def divide_mat(arr, divid):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = arr[i][j] / divid
    return arr

# получаем обратную матрицу
def inverse_mat(arr):
    arr_union = union_mat(arr)
    arr_union_t = rev_mat(arr_union)
    def_arr = calc_def(arr)
    inv_mat = divide_mat(arr_union_t, def_arr)
    return inv_mat

# перемножает матрицу на массив
def mul_mat_arr(inv_mat, yrr):
    arr_res = [0 for _ in range(len(inv_mat))]
    for i in range(len(inv_mat)):
        for j in range(len(inv_mat[i])):
            arr_res[i] += inv_mat[i][j] * yrr[j]
    return arr_res

# нахождение коэффициентов методом обратной матрицы
def Inverse_mat_metod(arr, yrr):
    # получаем обратную матрицу
    inv_mat = inverse_mat(arr)
    # и умножаем её на столбец свободных членов
    arr_res = mul_mat_arr(inv_mat, yrr)
    return arr_res
