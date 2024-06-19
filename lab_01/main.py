# Талышева ИУ7-45Б лаба_1 выч_алг

# ввести x y y' y'' из файла, cтепень n для аппроксимирующего полинома Ньютона и количество узлов
#для аппроксимирующего полинома Эрмита, значение аргумента x, для которого выполняется интерполяция.
def read_file(n):
    arr = list()
    flag = True
    while flag:
        filename = input("Введите название файла c x, y, y', y'': ")
        try:
            # Открытие файла для чтения
            with open(filename, 'r') as file:
                # Чтение содержимого файла построчно
                first_str = False
                for line in file:
                    #print("!", line, "!")
                    # Обработка строк файла (первая пропускается)
                    if first_str:
                        arr.append(tuple(map(float, line.strip().split())))
                    first_str = True
                if len(arr) < n:
                    print(f"Файл '{filename}' не содержит достаточного количества данных('{n}').")
                else:
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
    n = read_int("Введите cтепень n для аппроксимирующего полинома Ньютона: ")
    arr = read_file(n)
    count = read_int("Введите количество узлов для аппроксимирующего полинома Эрмита: ")
    x = read_float("Введите значение аргумента x, для которого выполняется интерполяция: ")
    return arr, n, count, x

def div_diff(arr, res_coefs):
    n = len(arr)
    if n == 1:
        return arr[0][2]  # Базовый случай: разделенная разность равна значению функции
    if n == 2:
        if arr[0][0] == arr[1][0]:  # Проверка, что x_i равен x_j
            return arr[0][2]  # Возвращаем значение производной функции в x_i
        return (arr[0][1] - arr[1][1]) / (arr[0][0] - arr[1][0])  # Возвращаем обычную разделенную разность
    new_arr_0 = [i for i in arr[:-1]]
    new_arr_1 = [i for i in arr[1:]]
    # Вычисляем разделенные разности для двух "массивов" без первого и последнего элемента соответственно
    div_diff_0 = div_diff(new_arr_0, res_coefs)
    div_diff_1 = div_diff(new_arr_1, res_coefs)
    # Добавляем в список коэффициентов
    if (new_arr_0[0][len(new_arr_0[0]) - 1] == True):
        res_coefs.append(div_diff_0)
    # Возвращаем разделенную разность для текущего узла
    if (arr[0][:-1] == arr[-1][:-1]):
        return arr[0][len(arr)]
    return (div_diff_0 - div_diff_1) / (arr[0][0] - arr[-1][0])

def sort_list(arr, ind):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1):
            if arr[j][ind] > arr[j + 1][ind]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr

def add_TF_list(arr):
    if (len(arr) > 0):
        arr[0] = arr[0] + (True,)
    for i in range(1, len(arr)):
        arr[i] = arr[i] + (False,)
    return arr

def choose_points(arr, n, x):
    if n == 0:
        return []
    new_arr = []
    i = 0
    while i < len(arr) and arr[i][0] < x:
        i += 1
    if (i >= len(arr)):
        new_arr = [i for i in arr[-n:]]
    else:
        new_arr = [arr[i]]
        i_left = i - 1
        i_right = i + 1
        k = 1
        while k < n:
            #print(k, n, i_left, i_right, i, arr, new_arr)
            if i_left >= 0:
                new_arr = [arr[i_left]] + new_arr
                k += 1
                i_left -= 1
            if i_right < len(arr) and k < n:
                new_arr += [arr[i_right]]
                k += 1
                i_right += 1
    return new_arr

def repeat_points(arr, n, count_rep):
    i = 0
    k = 0
    new_arr = list()
    while i < n and k < len(arr):
        #print(new_arr, arr[k])
        new_arr.append(arr[k])
        i += 1
        if i % count_rep == 0:
            k += 1
    return new_arr
                
def Newton_metod(arr, n, x):
    res_coefs = []  # Список для хранения коэффициентов
    arr = sort_list(arr, 0)
    new_arr = choose_points(arr, n, x)
    new_arr = add_TF_list(new_arr)
    result = div_diff(new_arr, res_coefs)
    res_coefs += [result]
    yx = new_arr[0][1]
    #print(new_arr)
    coef_x = 1
    for i in range(len(res_coefs)):
        coef_x *= x - new_arr[i][0]
        yx += res_coefs[i] * coef_x
    return yx

def Ermit_metod(arr, n, count, x):
    res_coefs = []  # Список для хранения коэффициентов
    arr = sort_list(arr, 0)
    new_arr = choose_points(arr, count, x)
    new_arr = repeat_points(new_arr, n, len(new_arr[0]) - 1)
    new_arr = add_TF_list(new_arr)
    result = div_diff(new_arr, res_coefs)
    res_coefs += [result]
    yx = new_arr[0][1]
    #print(new_arr)
    coef_x = 1
    for i in range(len(res_coefs)):
        coef_x *= x - new_arr[i][0]
        yx += res_coefs[i] * coef_x
    return yx

# Пример использования
##arr = [(-8, 7), (-1, 4), (0, 1), (0.25, 0.924), (0.5, 0.707), (0.75, 0.383), (1, 0)]
##res = Newton_metod(arr, 5, len(arr), 0.6)
##print(res)

def main():
    #print("main")
    # чтение всех данных
    arr, n, count, x = read_data()
    # применить метод
    Newton_yx = Newton_metod(arr, n, x)
    Ermit_yx = Ermit_metod(arr, n, count, x)
    # вывести значения y(x) для заданного значения аргумента
    print("\nРезультат метода Ньютона: y(x) =", Newton_yx)
    print("Результат метода Эрмита:  y(x) =", Ermit_yx)
    

if __name__ == "__main__":
    main()