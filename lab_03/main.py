# Талышева ИУ7-45Б лаба_3 выч_алг
from input import read_data
from Newton import Newton_metod
from Cubic_spline import Cubic_spline_metod, X_PART, Y_PART, Z_PART

# возвращает "мерность" списка
def get_list_dimension(arr):
    if isinstance(arr, list):
        return 1 + get_list_dimension(arr[0])
    else:
        return 0
    
# функция для многомерной интерполяции (x -> y -> z)
# param_inter = (x, y, z), degree_inter = (nx, ny, nz), arr - трехмерный массив x*y*z
def interpol_3(arr_z, param_inter, degree_inter, func1, func2):
    res_arr_z = list()
    for i_z in range(len(arr_z)):
        res_arr_y = list()
        arr_y = arr_z[i_z]
        for i_y in range(len(arr_y)):
            new_arr = [(i, arr_y[i_y][i]) for i in range(len(arr_y[i_y]))]
            res_arr_y.append((i_y, func1(new_arr, degree_inter[X_PART], param_inter[X_PART])))
        res_arr_z.append((i_z, func2(res_arr_y, degree_inter[Y_PART], param_inter[Y_PART])))
    return func1(res_arr_z, degree_inter[Z_PART], param_inter[Z_PART])

def main():
    # чтение всех данных
    arr, degree_inter, param_inter = read_data()
    # применить метод
    Newton_yx = interpol_3(arr, param_inter, degree_inter, Newton_metod, Newton_metod)
    Cubic_spline_yx_1 = interpol_3(arr, param_inter, degree_inter, Cubic_spline_metod, Cubic_spline_metod)
    combo_yx_1 = interpol_3(arr, param_inter, degree_inter, Newton_metod, Cubic_spline_metod)
    # вывести значения y(x) для заданного значения аргумента
    print("\nРезультат метода Ньютона: y(x) =", round(Newton_yx, 3))
    print("Результат метода кубического сплайна (№1): y(x) =", round(Cubic_spline_yx_1, 3))
    print("Результат смешанного метода: y(x) =", round(combo_yx_1, 3))
    

if __name__ == "__main__":
    main()