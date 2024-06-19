# Талышева ИУ7-45Б лаба_2 выч_алг
from input import read_data
from Newton import Newton_metod
from Cubic_spline import Cubic_spline_metod

# константы
MIN_COUNT_POINT = 1
POLYNOM_DEGREE = 3

def sort_list(arr, ind):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1):
            if arr[j][ind] > arr[j + 1][ind]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr

def main():
    # чтение всех данных
    arr, x = read_data(MIN_COUNT_POINT)
    arr = sort_list(arr, 0)
    # применить метод
    Newton_yx = Newton_metod(arr, POLYNOM_DEGREE, x)
    Cubic_spline_yx_1 = Cubic_spline_metod(arr, x, 1)
    # вывести значения y(x) для заданного значения аргумента
    print("\nРезультат метода Ньютона: y(x) =", Newton_yx)
    print("\nРезультат метода кубического сплайна (№1): y(x) =", Cubic_spline_yx_1)
    

if __name__ == "__main__":
    main()