import prettytable as pt

N = 6  # Количество точек

# Функция для форматирования вывода чисел
def formatOut(num):
    return f"{num:.5f}"

# Функция для односторонней разностной производной
def leftDiffDer(yValue, step, index):
    if index > 0:
        return formatOut((yValue[index] - yValue[index - 1]) / step)
    else:
        return '*'  # Помечаем, если нет значения

# Функция для центральной разностной производной
def centerDiffDer(yValue, step, index):
    if index > 0 and index < N - 1:
        return formatOut((yValue[index + 1] - yValue[index - 1]) / (2 * step))
    else:
        return '*'  # Помечаем, если нет значения

# Функция для второй формулы Рунге
def secondRunge(yValue, step, index):
    if not (1 < index < N - 2):
        return '*'  # Помечаем, если нет значения

    f1 = (yValue[index + 1] - yValue[index - 1]) / (2 * step)
    f2 = (yValue[index + 2] - yValue[index - 2]) / (4 * step)

    return formatOut(f1 + (f1 - f2) / 3)

# Функция для введения выравнивающих переменных
def aligVars(yValue, xValue, index):
    if index > N - 2:
        return '*'  # Помечаем, если нет значения

    d = (np.log(yValue[index + 1] / yValue[index])) / (np.log(xValue[index + 1] / xValue[index]))

    return formatOut(d * yValue[index] / xValue[index])

# Функция для вычисления второй разностной производной
def secondDiffDer(yValue, step, index):
    if index > 0 and index < N - 1:
        return formatOut((yValue[index - 1] - 2 * yValue[index] + yValue[index + 1]) / step ** 2)
    else:
        return '*'  # Помечаем, если нет значения

xArr = [1, 2, 3, 4, 5, 6]  # Значения X
yArr = [0.571, 0.889, 1.091, 1.231, 1.333, 1.412]  # Значения Y

step = (xArr[-1] - xArr[0]) / (len(xArr) - 1)  # Вычисляем шаг

methods = [leftDiffDer, centerDiffDer, 
           secondRunge, aligVars, 
           secondDiffDer]  # Список функций для вычисления разностных производных

# Создаем таблицу с помощью библиотеки PrettyTable
table = pt.PrettyTable()
filedNames = ["X", "Y", "1", "2", "3", "4", "5"]  # Названия столбцов

# Добавляем значения X и Y в таблицу
table.add_column(filedNames[0], xArr)
table.add_column(filedNames[1], yArr)

# Для каждой функции вычисляем соответствующие разностные производные и добавляем их в таблицу
for i in range(len(methods)):
    if i == 3:
        table.add_column(filedNames[i + 2], [methods[i](yArr, xArr, j) for j in range(N)])
    else:    
        table.add_column(filedNames[i + 2], [methods[i](yArr, step, j) for j in range(N)])

# Выводим таблицу с результатами
print(table)