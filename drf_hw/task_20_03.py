# Task 1

def calculate_minimum_payment(prices):
    # Сортировка списка стоимостей товаров в порядке убывания
    sorted_prices = sorted(prices, reverse=True)

    # Вычисление суммы двух наиболее дорогих товаров
    total_payment = sum(sorted_prices[:2])

    # Вычисление суммы остальных товаров, которые Вася получит бесплатно
    free_payment = sum(sorted_prices[2:])

    # Вычисление общей суммы денег, которую Вася должен взять с собой
    minimum_payment = total_payment + free_payment

    return minimum_payment

# Ввод данных
N = int(input("Введите количество товаров: "))
prices = list(map(int, input("Введите стоимости товаров через пробел: ").split()))

# Вычисление минимальной суммы денег, которую нужно взять с собой
minimum_payment = calculate_minimum_payment(prices)

# Вывод результата
print("Минимальная сумма денег: ", minimum_payment)

# Task 2
def find_closest_numbers(numbers):
    # Сортировка списка чисел
    sorted_numbers = sorted(numbers)

    # Инициализация переменных для хранения ближайших чисел
    closest_num1 = sorted_numbers[0]
    closest_num2 = sorted_numbers[1]
    min_diff = abs(sorted_numbers[1] - sorted_numbers[0])

    # Проход по отсортированному списку и поиск двух чисел с наименьшей разностью
    for i in range(1, len(sorted_numbers) - 1):
        diff = abs(sorted_numbers[i+1] - sorted_numbers[i])
        if diff < min_diff:
            min_diff = diff
            closest_num1 = sorted_numbers[i]
            closest_num2 = sorted_numbers[i+1]

    return closest_num1, closest_num2

# Ввод списка чисел
numbers = list(map(int, input("Введите список чисел через пробел: ").split()))

# Поиск двух ближайших чисел
closest_num1, closest_num2 = find_closest_numbers(numbers)

# Вывод результатов
print("Два ближайших числа:", closest_num1, closest_num2)


# Task 3
def align_strings(strings):
    # Нахождение длины самой длинной строки
    max_length = max(len(s) for s in strings)

    # Вывод строк с выравниванием
    for s in strings:
        print('*' * (max_length - len(s)) + s)

# Ввод количества строк
M = int(input("Введите количество строк: "))

# Создание списка для хранения строк
strings = []

# Ввод строк и добавление их в список
for _ in range(M):
    s = input("Введите строку: ")
    strings.append(s)

# Выравнивание строк и вывод результатов
align_strings(strings)


# Task 4
def balance_array(arr):
    # Вычисление суммы положительных и отрицательных элементов
    positive_sum = sum(num for num in arr if num > 0)
    negative_sum = sum(num for num in arr if num < 0)

    # Вычисление разницы между суммами
    diff = abs(positive_sum) - abs(negative_sum)

    # Добавление элемента diff к исходному массиву
    arr.append(diff)

    return arr

# Ввод исходного массива
arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

# Балансировка массива
balanced_arr = balance_array(arr)

# Вывод результатов
print("Исходный массив:", arr)
print("Балансированный массив:", balanced_arr)

