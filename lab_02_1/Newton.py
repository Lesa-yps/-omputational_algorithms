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

# Находит список для хранения коэффициентов
def find_Newton_coefs(new_arr):
    res_coefs = []
    new_arr = add_TF_list(new_arr)
    result = div_diff(new_arr, res_coefs)
    res_coefs += [result]
    return res_coefs

def Newton_metod(arr, n, x):
    new_arr = choose_points(arr, n, x)
    res_coefs = find_Newton_coefs(new_arr)
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