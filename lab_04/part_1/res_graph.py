import matplotlib.pyplot as plt
from Kramer import Kramer_method

# находим слау (матрицу)
# akj =  Σi=0N    [φk(xi)φj(xi) ], bj =  Σi=0N[f(xi)φj(xi) ], φk(x) = xk
def find_table_slay(table, degree, all_one = False):
    n = len(table)
    # инициализируем нулевую матрицу размерности n * n (правая часть слау a)
    mat_slay = [[0 for _ in range(degree)] for i in range(degree)]
    # инициализируем нулевой массив размерности n (левая часть слау b)
    res_slay = [0 for _ in range(degree)]
    for i in range(degree + 1):
        for j in range(degree + 1):
            # Проходим по каждой точке в таблице
            for k in range(n):
                x_point = table[k][0]  # Получаем координату x точки
                y_point = table[k][1]  # Получаем координату y точки
                w_point = 1 if all_one else table[k][2]  # Получаем вес точки
                mat_slay[i][j] += w_point * pow(x_point, (i + j))
                res_slay[i] += w_point * y_point * pow(x_point, i)
    return mat_slay, res_slay

# строит график по матрице с весами и степени аппроксимирующего полинома
def build_graph(table, poly_degree, type_line = '-', all_one = False):
    # Создаем матрицу СЛАУ
    mat_slay, res_slay = find_table_slay(table, poly_degree, all_one)
    # находим коэффициенты функции, которая будет строиться (решаем СЛАУ методом Крамера)
    res_arr = Kramer_method(mat_slay, res_slay)
    # составляет массив х-ов и у-ов по найденной функции
    x_arr, y_arr = [], []
    for x in range(len(table)):
        y = 0
        for i in range(len(res_arr)):
            y += res_arr[i] * x ** i
        x_arr.append(x)
        y_arr.append(y)
    # Строим график
    label_graph = "график с весами = 1" if all_one else "график с настоящими весами"
    plt.plot(x_arr, y_arr, type_line, label = label_graph)  


def print_res_graph(table):
    n = len(table)
    # ввод степени аппроксимирующего полинома
    poly_degree = -1
    while poly_degree <= 0:
        try:
            poly_degree = int(input("Введите степень аппроксимирующего полинома: "))
        except ValueError:
            poly_degree = -1
            print("Ошибка ввода степени аппроксимирующего полинома! Повторите попытку!")
        else:
            if poly_degree <= 0 or poly_degree >= n:
                print("Ошибка ввода степени аппроксимирующего полинома (он должен быть положительным и меньше {n})! Повторите попытку!")
    # строим функцию с её весами
    build_graph(table, poly_degree)
    # строим функцию со всеми весами = 1
    build_graph(table, poly_degree, type_line = '-.', all_one = True)
    # массив всех х-ов и массив всех у-ов
    arr_x_table = [i[0] for i in table]
    arr_y_table = [i[1] for i in table]
    # строит график
    plt.plot(arr_x_table, arr_y_table, 'x', label = "result graph")
    plt.legend()
    plt.grid()
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.show()
    return table