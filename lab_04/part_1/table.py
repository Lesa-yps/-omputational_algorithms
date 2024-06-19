from random import random # рандомное вещественное число в диапазоне 0.0 - 1.0

SIZE_TABLE = 8
DEF_WEIGHT = 1
MAX_XY = 10

# генерация рандомной таблицы
def make_table():
    table = list()
    x = random() * MAX_XY
    for i in range(SIZE_TABLE):
        table.append([x + i, random() * MAX_XY, random() * DEF_WEIGHT])
    return table

# вывод сгенерированной таблицы
def print_table(table):
    n = len(table)
    print("\nСгенерированная таблица:\n")
    print("  {:}    |      {:}     |      {:}    |     {:} \n".format('№', 'X', 'Y', 'P') + 40 * "-")
    for i in range(n):
        print("  {:-3d}  |   {:-5.2f}   |   {:-4.2f}   |   {:-5.2f}   ".format(i + 1, table[i][0], table[i][1], table[i][2]))

# функция изменяет вес точки (выбранной пользователем по номеру)
def change_weight(table):
    n = len(table)
    # ввод номера точки
    point_num = -1
    while point_num <= 0:
        try:
            point_num = int(input("Введите номер точки, для которой нужно изменить вес (1 - {:}): ".format(n)))
        except ValueError:
            point_num = -1
            print("Ошибка ввода номера точки! Повторите попытку!")
        else:
            if point_num <= 0 or point_num > n:
                print("Ошибка ввода номера точки (он должен быть положительным и меньше или равен {:})! Повторите попытку!".format(n))
    # ввод нового веса точки
    point_weight = -1
    while point_weight <= 0:
        try:
            point_weight = int(input("Введите новый вес точки (> 0): "))
        except ValueError:
            point_weight = -1
            print("Ошибка ввода веса точки! Повторите попытку!")
        else:
            if point_weight <= 0:
                print("Ошибка ввода веса точки (он должен быть положительным)! Повторите попытку!")
    # изменение веса выбранной точки
    table[point_num - 1][2] = point_weight