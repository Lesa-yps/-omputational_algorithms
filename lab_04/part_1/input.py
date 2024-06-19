# читает данные из файла
def read_file(file):
    arr = list()
    # Чтение содержимого файла построчно
    for line in file:
        # Обработка строк файла
        if (line != '\n'):
            arr.append(list(map(float, line.strip().split())))
    return arr

# ввести данные из файла
def work_with_file():
    flag = True
    while flag:
        filename = input("Введите название файла c x, y: ")
        try:
            # Открытие файла для чтения
            with open(filename, 'r') as file:
                # Чтение содержимого файла
                arr = read_file(file)
                flag = False
                file.close()
        except FileNotFoundError:
            print(f"Файл '{filename}' не существует.")
        except IOError:
            print(f"Ошибка при чтении файла '{filename}'.")
    return arr

# чтение всех данных
def read_data():
    arr = work_with_file()
    return arr