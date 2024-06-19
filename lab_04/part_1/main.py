# Талышева ИУ7-45Б лаба_4 выч_алг
from table import make_table, print_table, change_weight
from res_graph import print_res_graph

def main():
    # генерация таблицы
    table = make_table()
    # меню
    act_choose = -1
    while act_choose != 0:
        print("Меню:\n\
    0 - выход из программы\n\
    1 - вывести сгенерированную таблицу\n\
    2 - вывести результирующий график\n\
    3 - изменить вес точки\n\
    Введите выбранное действие: ", end = '')
        try:
            act_choose = int(input())
        except ValueError:
            act_choose = -1
            print("Ошибка ввода выбранного действия! Повторите попытку!")
            continue
        if act_choose == 1:
            print_table(table)
        elif act_choose == 2:
            print_res_graph(table)
        elif act_choose == 3:
            change_weight(table)
        elif act_choose == 0:
            print("Программа завершена ^-^")
        else:
            print("Ошибка! Номер действия должен быть в интервале 0-3! Повторите попытку!")
    

if __name__ == "__main__":
    main()