import re

# константы
MIN_COUNT_POINT_SPLINE = 4

# читает данные из файла
def read_file(file):
    arr = list()
    pattern = r"\s*z=(\d+)\s*"  # Шаблон для строки вида "z=<число>" c возможными пробелами в начале и конце
    is_first_string = True
    # Чтение содержимого файла построчно
    for line in file:
        # Обработка строк файла
        if (line != '\n'):
            if re.match(pattern, line):
                arr.append(list())
                is_first_string = True
            elif is_first_string == False:
                arr[-1].append(list(map(float, line.strip().split()))[1:])
            elif is_first_string == True:
                is_first_string = False
    return arr

# проверяет количество точек и их соответствие степеням полиномов
def check_arr_n(arr, nx, ny, nz):
    rc = False
    if len(arr) == 0 or len(arr[0]) == 0 or len(arr[0][0]) == 0:
        print("Ошибка! Количество точек не может быть нулевым!")
    else:
        count_z = len(arr)
        count_y = len(arr[0])
        count_x = len(arr[0][0])
        if count_z < MIN_COUNT_POINT_SPLINE or count_y < MIN_COUNT_POINT_SPLINE or count_x < MIN_COUNT_POINT_SPLINE:
            print(f"Файл не содержит достаточного количества данных для интерполяции кубическими сплайнами ('{MIN_COUNT_POINT_SPLINE}').")
        elif count_z < (nz + 1):
            print(f"Файл не содержит достаточного количества точек z для интерполяции полиномом Ньютона '{nz}'-степени.")
        elif count_y < (ny + 1):
            print(f"Файл не содержит достаточного количества точек y для интерполяции полиномом Ньютона '{ny}'-степени.")
        elif count_x < (nx + 1):
            print(f"Файл не содержит достаточного количества точек x для интерполяции полиномом Ньютона '{nx}'-степени.")
        else:
            rc = True
    return rc

# ввести данные из файла
def work_with_file(nx, ny, nz):
    flag = True
    while flag:
        filename = input("Введите название файла c x, y: ")
        try:
            # Открытие файла для чтения
            with open(filename, 'r') as file:
                # Чтение содержимого файла
                arr = read_file(file)
                # проверяет количество точек и их соответствие степеням полиномов
                if check_arr_n(arr, nx, ny, nz):
                    flag = False
                file.close()
        except FileNotFoundError:
            print(f"Файл '{filename}' не существует.")
        except IOError:
            print(f"Ошибка при чтении файла '{filename}'.")
    return arr

# читает с проверкой целое положительное число с клавиатуры
def read_int(str):
    print(str, end = '')
    flag = True
    while flag:
        try:
            n = int(input())
            if (n <= 0):
                print("Число должно быть положительным! Повторите попытку: ", end = "")
            else:
                flag = False
        except:
            print("Ошибка ввода! Повторите попытку ввода целого положительного числа: ", end = "")
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

# чтение всех данных
def read_data():
    nx = read_int("Введите степень аппроксимирующего полинома - nx: ")
    ny = read_int("Введите степень аппроксимирующего полинома - ny: ")
    nz = read_int("Введите степень аппроксимирующего полинома - nz: ")
    arr = work_with_file(nx, ny, nz)
    x = read_float("Введите значение аргумента x, для которого выполняется интерполяция: ")
    y = read_float("Введите значение аргумента y, для которого выполняется интерполяция: ")
    z = read_float("Введите значение аргумента z, для которого выполняется интерполяция: ")
    return arr, (nx, ny, nz), (x, y, z)