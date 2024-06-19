# Талышева ИУ7-45Б лаба_0 выч_алг
#from sympy import diff
import math

# читает с проверкой целое неотрицательное число с клавиатуры (возвращает число + 1)
def read_int(str):
    print(str, end = '')
    flag = True
    while flag:
        try:
            n = int(input()) + 1
            if (n <= 0):
                print("Число должно быть неотрицательным! Повторите попытку: ")
            else:
                flag = False
        except:
            print("Ошибка ввода! Повторите попытку ввода целого неотрицательного числа: ", end = "")
    return n

# читает с проверкой вещественное число с клавиатуры
def read_float(str):
    print(str, end = '')
    flag = True
    while flag:
        try:
            n = float(input())
            flag = False
        except:
            print("Ошибка ввода! Повторите попытку ввода вещественного числа: ", end = "")
    return n

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

# считывает всё что нужно для задачи
def input_all():
    # вводится степнь уравнения
    n = read_int("Введите степень уравнения: ")
    count_diff = read_int("Введите известное количество производных: ")
    count_points = math.ceil(n / count_diff)
    #print(count_points)
    arr = [[0] * n for _ in range(n)]
    yrr = [0] * n
    for i in range(count_points):
        diff_arr = [1] * n
        xi = read_float("Введите x" + str(i + 1) + " : ")
        for j in range(count_diff):
            for k in range(j, n):
                #print(i, j, k)
                if (j + i * count_diff) < n:
                    arr[j + i * count_diff][k] = xi ** (k - j) * diff_arr[k]
                #print(k, j, arr[j + i * count_diff][k])
                #print_matrix(arr)
            #print("ДО:", diff_arr)
            diff_arr = [diff_arr[w] * (w - j) for w in range(n)]
            #print("После:", diff_arr)
        #print_matrix(arr)
        #print_array(yrr)
        yrr[i * count_diff] = read_float("Введите y" + str(i + 1) + " : ")
        for j in range(1, count_diff):
            if (j + i * count_diff) < n:
                yrr[j + i * count_diff] = read_float("Введите производную №" + str(j) + " : ")
    return n, arr, yrr

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

n, arr, yrr = input_all()
##n = 2
##arr = [[1, 2, 4], [0, 1, 4], [0, 0, 2]]
##yrr = [13, 11, 4]
#print_matrix(arr)
#print_array(yrr)
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
    print_res(res_a)
