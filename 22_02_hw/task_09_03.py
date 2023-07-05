# Task 1

def find_missing_card(N, remaining_cards):
    total_sum = sum(range(1, N + 1))  # Сумма всех номеров карточек от 1 до N
    remaining_sum = sum(remaining_cards)  # Сумма номеров оставшихся карточек
    missing_card = total_sum - remaining_sum  # Номер потерянной карточки
    return missing_card


# Ввод данных
N = int(input("Введите число N: "))
remaining_cards = []
for _ in range(N - 1):
    card = int(input("Введите номер оставшейся карточки: "))
    remaining_cards.append(card)

# Поиск потерянной карточки
missing_card = find_missing_card(N, remaining_cards)
print("Номер потерянной карточки:", missing_card)


# Task 2

def print_squares(N):
    i = 1
    while i ** 2 <= N:
        print(i ** 2)
        i += 1


# Ввод числа N
N = int(input("Введите число N: "))

# Печать квадратов натуральных чисел
print("Квадраты натуральных чисел, не превосходящие", N, ":")
print_squares(N)
