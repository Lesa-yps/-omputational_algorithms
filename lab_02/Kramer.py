# выводит матрицу на экран
def print_matrix(mat):
    print("Матрица:")
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end = ' ')
        print()
    if len(mat) == 0 or len(mat[0]) == 0:
        print("Матрица пуста.")
    print()

# выводит массив на экран
def print_array(arr):
    print("Массив:")
    for i in range(len(arr)):
        print(arr[i])
    if len(arr) == 0:
        print("Массив пуст.")
    print()

# выводит результат в красивом виде на экран
def print_res(arr):
    n = len(arr)
    new_arr = arr[::-1]
    res_str = ""
    if n - 1 < 0:
        print("Результат:\n P0(x) =", end = " ")
    else:
        print("Результат:\n P" + str(n - 1) + "(x) =", end = " ")
    for i in range(n):
        plus = "+ "
        if res_str == "" or new_arr[i] < 0:
            plus = ""
        x_part = " * x^" + str(n - i - 1) if i < (n - 1) else ""
        if (new_arr[i] != 0):
            res_str += plus + "{:.2f}".format(new_arr[i]) + x_part + " "
    if n == 0:
        res_str += "0"
    print(res_str)

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

# вычисляет методом Крамера i-тый неизвестный элемент
def calc_ai(arr, yrr, ind, def_main):
    arr_new = [row[:] for row in arr]
    for i in range(len(arr_new)):
        arr_new[i][ind] = yrr[i]
    def_ai = calc_def(arr_new)
    #print_matrix(arr_new)
    #print(def_ai / def_main)
    return def_ai / def_main

##n = 2
##arr = [[1, 2, 4], [0, 1, 4], [0, 0, 2]]
##yrr = [13, 11, 4]
def Kramer_metod(arr, yrr):
    def_main = calc_def(arr)
    #print(def_main)
    if (def_main == 0):
        print("Система уравнений не имеет единственного решения, так как определитель матрицы равен 0.\n\
    Возможно, система имеет бесконечно много решений или не имеет решений вовсе.")
    else:
        res_a = list()
        for i in range(len(arr[0])):
            ai = calc_ai(arr, yrr, i, def_main)
            res_a.append(ai)
        return res_a