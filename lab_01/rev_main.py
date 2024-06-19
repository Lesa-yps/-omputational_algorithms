import main

def reverse_xy(arr):
    for i in range(len(arr)):
        x_diff1 = float('inf')
        x_diff2 = 0
        if arr[i][2] != 0:
            x_diff1 = arr[i][2] ** (-1)
            x_diff2 = - arr[i][3] / (x_diff1 ** 3)
        arr[i] = (arr[i][1], arr[i][0], x_diff1, x_diff2)
    return arr

def rev_main():
    #print("rev_main")
    # чтение всех данных
    n = main.read_int("Введите cтепень n для аппроксимирующего полинома Ньютона: ")
    arr = main.read_file(n)
    count = main.read_int("Введите количество узлов для аппроксимирующего полинома Эрмита: ")
    # чтобы найти корни меняем x и y в массиве местами и ищем x для y = 0
    arr = reverse_xy(arr)
    y = 0
    # применить метод
    Newton_xy = main.Newton_metod(arr, n, y)
    Ermit_xy = main.Ermit_metod(arr, n, count, y)
    # вывести значения x(0)
    print("\nРезультат метода Ньютона (корень): x(0) =", Newton_xy)
    print("Результат метода Эрмита (корень):  x(0) =", Ermit_xy)
    

if __name__ == "__main__":
    rev_main()