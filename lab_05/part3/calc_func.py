# функция дополняет метод Ньютона,
# вычисляя функцию и частные производные в точке

# помогает считать производные
def diff_f(numf, numx, vector, x_start, x_fin):
    y_arr = vector
    h = (x_fin - x_start) / (len(vector) - 1)
    if numf == numx:
        return -2 / h**2 - 3 * y_arr[numx]**2
    if abs(numf - numx) == 1:
        return 1 / h**2
    return 0

# считает значение функции в точке
def Fx(vector, x_start, x_fin):
    #y_arr = [1] + vector + [3]
    y_arr = vector
    h = (x_fin - x_start) / (len(vector) - 1)
    f_arr = []
    for i in range(1, len(y_arr) - 1):
        f_arr.append((y_arr[i + 1] - 2 * y_arr[i] + y_arr[i - 1]) / h**2 - y_arr[i]**3 - (x_start + i * h)**2)
        #f_arr.append(25 * y_arr[i - 1] - (50 + y_arr[i]**2) * y_arr[i] + 25 * y_arr[i + 1] - (0.2 * i)**2)
    return f_arr
