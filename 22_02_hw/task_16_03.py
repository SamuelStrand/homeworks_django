# Task 1

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(2))


# Task 2

def is_power_of_two(number):
    if number == 0:
        return False
    while number != 1:
        if number % 2 != 0:
            return False
        number = number // 2
    return True


print(is_power_of_two(8))

# Task 3

import math


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def calculate():
    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Факториал")
        print("6. Число Фибоначчи")
        print("7. Синус")
        print("8. Косинус")
        print("9. Тангенс")
        print("10. Возведение в степень")
        print("0. Выход")

        choice = int(input("Введите номер операции: "))

        if choice == 0:
            break

        if 1 <= choice <= 4:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))

            if choice == 1:
                result = num1 + num2
                print("Результат: ", result)
            elif choice == 2:
                result = num1 - num2
                print("Результат: ", result)
            elif choice == 3:
                result = num1 * num2
                print("Результат: ", result)
            elif choice == 4:
                result = num1 / num2
                print("Результат: ", result)

        elif choice == 5:
            num = int(input("Введите число для вычисления факториала: "))
            result = factorial(num)
            print("Результат: ", result)

        elif choice == 6:
            num = int(input("Введите номер числа Фибоначчи: "))
            result = fibonacci(num)
            print("Результат: ", result)

        elif 7 <= choice <= 9:
            angle = float(input("Введите угол в градусах: "))
            radians = math.radians(angle)

            if choice == 7:
                result = math.sin(radians)
                print("Результат: ", result)
            elif choice == 8:
                result = math.cos(radians)
                print("Результат: ", result)
            elif choice == 9:
                result = math.tan(radians)
                print("Результат: ", result)

        elif choice == 10:
            num = float(input("Введите число: "))
            power = float(input("Введите степень: "))
            result = math.pow(num, power)
            print("Результат: ", result)

        print()


calculate()

# Task 4

# Инициализация пустой доски
board = [' ' for _ in range(9)]

# Функция для отображения доски
def display_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Функция для проверки выигрышных комбинаций
def check_win(player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # горизонтальные линии
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # вертикальные линии
        [0, 4, 8], [2, 4, 6]  # диагональные линии
    ]
    for combination in win_combinations:
        if all(board[i] == player for i in combination):
            return True
    return False

# Функция для игры
def play_game():
    print("********** Игра Крестики-нолики для двух игроков **********")
    display_board()

    current_player = 'X'
    while True:
        position = int(input("Куда поставим " + current_player + "? "))

        if board[position - 1] != ' ':
            print("Недопустимый ход. Попробуйте снова.")
            continue

        board[position - 1] = current_player
        display_board()

        if check_win(current_player):
            print(current_player, "выиграл!")
            break

        if ' ' not in board:
            print("Ничья!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

# Запуск игры
play_game()
