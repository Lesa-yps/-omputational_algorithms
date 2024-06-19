# ввести x y из файла
def read_file(n):
    arr = list()
    flag = True
    while flag:
        filename = input("Введите название файла c x, y: ")
        try:
            # Открытие файла для чтения
            with open(filename, 'r') as file:
                # Чтение содержимого файла построчно
                for line in file:
                    # Обработка строк файла
                    if (line != '\n'):
                        arr.append(tuple(map(float, line.strip().split())))
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
def read_data(min_points_in_file):
    arr = read_file(min_points_in_file)
    x = read_float("Введите значение аргумента x, для которого выполняется интерполяция: ")
    return arr, x