import matplotlib.pyplot as plt  # Импортируем библиотеку для построения графиков
from copy import deepcopy  # Импортируем функцию deepcopy для создания глубоких копий объектов

from color import set_color, base_color, red, purple  # Импортируем цветовые константы из другого файла
from table import SIZE_TABLE  # Импортируем константу SIZE_TABLE из другого файла

EPS = 0.01  # Задаем значение малого положительного эпсилона

def init_matrix(size):
    # Функция для инициализации матрицы заданного размера
    matrix = []  # Создаем пустой список для матрицы
    for _ in range(size + 1):  # Проходим по каждой строке матрицы
        row = []  # Создаем пустую строку
        for _ in range(size + 2):  # Проходим по каждому элементу строки
            row.append(0)  # Заполняем строку нулями

        matrix.append(row)  # Добавляем строку в матрицу

    return matrix  # Возвращаем инициализированную матрицу

def make_slae_matrix(table, n):
    # Функция для создания матрицы СЛАУ
    size = len(table)  # Получаем количество точек из таблицы
    matrix = init_matrix(n)  # Инициализируем матрицу размером n

    for i in range(n + 1):  # Проходим по каждой строке матрицы
        for j in range(n + 1):  # Проходим по каждому столбцу матрицы

            matrix[i][j] = 0.0  # Инициализируем элемент матрицы нулем
            matrix[i][n + 1] = 0.0  # Инициализируем элемент матрицы нулем

            for k in range(size):  # Проходим по каждой точке в таблице
                weight = table[k][2]  # Получаем вес точки
                x = table[k][0]  # Получаем координату x точки
                y = table[k][1]  # Получаем координату y точки

                matrix[i][j] += weight * pow(x, (i + j))  # Вычисляем элемент матрицы
                matrix[i][n + 1] += weight * y * pow(x, i)  # Вычисляем элемент матрицы

    return matrix  # Возвращаем матрицу СЛАУ

def solve_matrix_gauss(matrix):
    # Функция для решения СЛАУ методом Гаусса
    size = len(matrix)  # Получаем размер матрицы

    for i in range(size):  # Проходим по каждой строке матрицы
        for j in range(i + 1, size):  # Проходим по каждой строке ниже текущей
            if (i == j):  # Если индексы равны
                continue  # Пропускаем итерацию

            k = matrix[j][i] / matrix[i][i]  # Вычисляем коэффициент k

            for q in range(i, size + 1):  # Проходим по всем элементам строки
                matrix[j][q] -= k * matrix[i][q]  # Выполняем вычитание для получения нулевого элемента

    result = [0 for i in range(size)]  # Создаем список для результатов

    for i in range(size - 1, -1, -1):  # Проходим по строкам матрицы снизу вверх
        for j in range(size - 1, i, -1):  # Проходим по столбцам справа налево
            matrix[i][size] -= result[j] * matrix[i][j]  # Вычитаем из правой части решения

        result[i] = matrix[i][size] / matrix[i][i]  # Вычисляем значение переменной

    return result  # Возвращаем результаты решения

def find_graph_dots(table, n):
    # Функция для нахождения точек графика полинома
    matrix = make_slae_matrix(table, n)  # Создаем матрицу СЛАУ
    result = solve_matrix_gauss(matrix)  # Решаем СЛАУ методом Гаусса

    x_arr, y_arr = [], []  # Инициализируем списки для координат точек
    k = table[0][0] - EPS  # Устанавливаем начальное значение x

    size = len(table)  # Получаем количество точек из таблицы
    while (k <= table[size - 1][0] + EPS):  # Пока не достигнут последний x
        y = 0  # Обнуляем y
        for j in range(0, n + 1):  # Проходим по степеням полинома
            y += result[j] * pow(k, j)  # Вычисляем значение y

        x_arr.append(k)  # Добавляем x в список
        y_arr.append(y)  # Добавляем y в список

        k += EPS  # Увеличиваем x на эпсилон

    return x_arr, y_arr  # Возвращаем списки координат точек

def table_changed(table):
    # Функция для проверки изменения таблицы
    for i in table:  # Проходим по каждой точке в таблице
        if i[2] != 1:  # Если вес точки не равен 1
            return True  # Возвращаем True
    
    return False  # Возвращаем False, если все веса равны 1

def get_base_table(table):
    # Функция для получения таблицы с равными весами
    base_table = deepcopy(table)  # Создаем глубокую копию таблицы
    size = len(base_table)  # Получаем размер таблицы

    for i in range(size):  # Проходим по каждой точке в таблице
        base_table[i][2] = 1  # Устанавливаем вес точки равным 1
    
    return base_table  # Возвращаем таблицу с равными весами

def plot_graphs(table, n, type_graph, type_dots):
    # Функция для построения графиков
    for i in range(1, n + 1):  # Проходим по степеням полинома
        if (i > 2 and i < n):  # Если степень полинома больше 2 и меньше n
            continue  # Пропускаем итерацию

        x_arr, y_arr = find_graph_dots(table, i)  # Получаем координаты точек графика
        plt.plot(x_arr, y_arr, type_graph, label = "%s\nn = %d" %(type_dots, i))  # Строим график для текущей степени

def solve_task(table):
    # Функция для решения задачи
    try:
        n = int(input("\n%s%sВведите степень аппроксимирующего полинома: %s%s"
            %(set_color, purple, set_color, base_color)))  # Получаем степень полинома от пользователя
    except:
        print("\n%s%sОшибка: некорректно введенна степень полинома!%s%s"
            %(set_color, red, set_color, base_color)))  # Выводим сообщение об ошибке, если ввод некорректен
        return table  # Возвращаем исходную таблицу

    if n >= SIZE_TABLE or n <= 0:  # Проверяем корректность введенной степени полинома
        print("\n%s%sОшибка: некорректно введенна степень полинома!%s%s"
            %(set_color, red, set_color, base_color))  # Выводим сообщение об ошибке, если ввод некорректен
        return table  # Возвращаем исходную таблицу

    if table_changed(table):  # Проверяем, изменилась ли таблица
        base_table = get_base_table(table)  # Получаем таблицу с равными весами
        type_dots = "Diff weights"  # Устанавливаем тип точек
        type_graph = "-."  # Устанавливаем тип графика

        plot_graphs(base_table, n, "-", "Equal weights")  # Строим графики для таблицы с равными весами
    else:
        type_dots = "Equal weights"  # Устанавливаем тип точек
        type_graph = "-"  # Устанавливаем тип графика

    plot_graphs(table, n, type_graph, type_dots)  # Строим графики для исходной таблицы

    x_arr = [i[0] for i in table]  # Получаем координаты x из таблицы
    y_arr = [i[1] for i in table]  # Получаем координаты y из таблицы

    plt.plot(x_arr, y_arr, 'o', label = "dots")  # Строим график точек

    plt.legend()  # Выводим легенду графика
    plt.grid()  # Включаем сетку на графике
    plt.xlabel("Axis X")  # Устанавливаем подпись для оси X
    plt.ylabel("Axis Y")  # Устанавливаем подпись для оси Y
    plt.show()  # Отображаем график

    return table  # Возвращаем исходную таблицу
