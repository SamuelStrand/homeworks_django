# Task 1
def check_expenses(s, p, m):
    total_expenses = s + p
    if total_expenses <= m:
        return "Да"
    else:
        return "Нет"

# Входные данные
s = int(input("Введите стоимость подписки на онлайн-кинотеатр: "))
p = int(input("Введите стоимость пиццы: "))
m = int(input("Введите заработок Пети: "))

# Проверка возможности покупки
result = check_expenses(s, p, m)
print(result)

# Task 2

def is_valid_move_queen(start_square, end_square):
    start_file, start_rank = start_square
    end_file, end_rank = end_square

    # Проверка, находятся ли клетки на одной диагонали, горизонтали или вертикали
    if start_file == end_file or start_rank == end_rank or abs(start_file - end_file) == abs(start_rank - end_rank):
        return True
    else:
        return False


def is_valid_move_knight(start_square, end_square):
    start_file, start_rank = start_square
    end_file, end_rank = end_square

    # Проверка возможных вариантов ходов коня
    if (abs(start_file - end_file) == 2 and abs(start_rank - end_rank) == 1) or (
            abs(start_file - end_file) == 1 and abs(start_rank - end_rank) == 2):
        return True
    else:
        return False


def parse_square(square):
    # Проверка правильности ввода клетки (например, 'a1')
    if len(square) != 2:
        raise ValueError("Неверный формат клетки. Введите букву и цифру (например, 'a1').")

    file = square[0].lower()
    rank = square[1]

    # Проверка допустимости буквы файла (от 'a' до 'h')
    if file < 'a' or file > 'h':
        raise ValueError("Неверная буква файла. Введите букву от 'a' до 'h'.")

    # Проверка допустимости номера ранга (от 1 до 8)
    if int(rank) < 1 or int(rank) > 8:
        raise ValueError("Неверный номер ранга. Введите номер от 1 до 8.")

    return file, int(rank)


def chessboard_app():
    print("********** Шахматная доска **********")
    print("Шахматный ферзь ходит по диагонали, горизонтали или вертикали.")
    print(
        "Шахматный конь ходит буквой 'Г' - на две клетки по вертикали в любом направлении и на одну клетку по горизонтали, или наоборот.")
    print()

    while True:
        try:
            start_square = input("Введите начальную клетку: ")
            end_square = input("Введите конечную клетку: ")

            start_square = parse_square(start_square)
            end_square = parse_square(end_square)

            queen_move = is_valid_move_queen(start_square, end_square)
            knight_move = is_valid_move_knight(start_square, end_square)

            print()
            if queen_move:
                print("Ферзь может попасть с первой клетки на вторую одним ходом.")
            else:
                print("Ферзь не может попасть с первой клетки на вторую одним ходом.")

            if knight_move:
                print("Конь может попасть с первой клетки на вторую одним ходом.")
            else:
                print("Конь не может попасть с первой клетки на вторую одним ходом.")

            break
        except ValueError as e:
            print("Ошибка:", str(e))
            print("Попробуйте снова.")
            print()


# Запуск приложения
chessboard_app()
