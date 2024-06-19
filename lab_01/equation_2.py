import main

EPS = 0.001

# прочитать из файла функции f и g
def read_file(filename):
    arr = list()
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
        file.close()
    return arr

def what_n(arr_f, arr_g):
    arr_n = dict()
    for i in range(len(arr_g)):
        n = 2
        Newton_yx_old = main.Newton_metod(arr_f, 1, arr_g[i][0])
        Newton_yx_new = main.Newton_metod(arr_f, 2, arr_g[i][0])
        while (abs(Newton_yx_old - Newton_yx_new) >= EPS and n <= 7):
            n += 1
            Newton_yx_old = Newton_yx_new
            Newton_yx_new = main.Newton_metod(arr_f, n, arr_g[i][0])
        if not (n > 7):
            if n in arr_n:
                arr_n[n] += 1
            else:
                arr_n[n] = 1
    # Находим ключ с наибольшим значением в словаре
    real_n = max(arr_n, key = arr_n.get)
    return real_n
        

# проинтерполировать f к иксам g
def fx_to_gx(arr_f, arr_g):
    new_arr_f = []
    n = what_n(arr_f, arr_g)
    for i in range(len(arr_g)):
        Newton_yx = main.Newton_metod(arr_f, n, arr_g[i][0])
        new_arr_f.append((arr_g[i][0], Newton_yx))
    return new_arr_f, n

def equation_2():
    # прочитать из файла функции f и g
    arr_f = read_file("func_1.txt")
    arr_g = read_file("func_2.txt")
    # проинтерполировать f к иксам g
    arr_f, n = fx_to_gx(arr_f, arr_g)
    # создать массив (f(x) - g(x), x)
    arr = []
    for i in range(len(arr_f)):
        arr.append((arr_f[i][1] - arr_g[i][1], arr_f[i][0]))
    # найти x(0) и вывести
    Newton_xy = main.Newton_metod(arr, n, 0)
    print("\nРезультат (корень): x(0) =", Newton_xy)

if __name__ == "__main__":
    equation_2()