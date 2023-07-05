from PyQt6 import QtCore, QtGui, QtWidgets
from calculator_ui import Ui_Calculator

class Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Calculator()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.addition)
        self.ui.pushButton_2.clicked.connect(self.subtraction)
        self.ui.pushButton_3.clicked.connect(self.multiplication)
        self.ui.pushButton_4.clicked.connect(self.division)

    def addition(self):
        num1 = int(self.ui.lineEdit.text())
        num2 = int(self.ui.lineEdit_2.text())
        result = num1 + num2
        self.ui.label.setText(str(result))

    def subtraction(self):
        num1 = int(self.ui.lineEdit.text())
        num2 = int(self.ui.lineEdit_2.text())
        result = num1 - num2
        self.ui.label.setText(str(result))

    def multiplication(self):
        num1 = int(self.ui.lineEdit.text())
        num2 = int(self.ui.lineEdit_2.text())
        result = num1 * num2
        self.ui.label.setText(str(result))

    def division(self):
        num1 = int(self.ui.lineEdit.text())
        num2 = int(self.ui.lineEdit_2.text())
        result = num1 / num2
        self.ui.label.setText(str(result))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())



# Task 1
def caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                # Зашифровка прописной буквы
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                # Зашифровка строчной буквы
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # Оставляем символы, не являющиеся буквами, без изменений
            encrypted_char = char

        encrypted_text += encrypted_char

    return encrypted_text

# Ввод сдвига шифрования
shift = int(input("Введите сдвиг шифрования: "))

# Ввод текста для шифрования
text = input("Введите текст для шифрования: ")

# Шифрование текста
encrypted_text = caesar_cipher(text, shift)

# Вывод зашифрованного текста
print("Зашифрованный текст:", encrypted_text)



# Task 2
def count_fruit(fruits, fruit):
    count = 0

    for f in fruits:
        if f.lower() == fruit.lower():
            count += 1

    return count

# Кортеж с фруктами
fruits = ("apple", "banana", "orange", "apple", "kiwi", "banana", "apple", "pear")

# Ввод названия фрукта
fruit = input("Введите название фрукта: ")

# Подсчет количества вхождений фрукта
fruit_count = count_fruit(fruits, fruit)

# Вывод результата
print("Количество вхождений фрукта:", fruit_count)



# Task 3
def count_fruit_occurrences(fruits, fruit):
    exact_match_count = 0
    partial_match_count = 0

    for f in fruits:
        if f.lower() == fruit.lower():
            exact_match_count += 1
        elif fruit.lower() in f.lower():
            partial_match_count += 1

    return exact_match_count, partial_match_count

# Кортеж с фруктами
fruits = ("apple", "banana", "orange", "apple", "kiwi", "banana", "apple", "pear", "bananamango", "mango", "strawberry-banana")

# Ввод названия фрукта
fruit = input("Введите название фрукта: ")

# Подсчет количества вхождений фрукта и частичных совпадений
exact_match_count, partial_match_count = count_fruit_occurrences(fruits, fruit)

# Вывод результата
print("Количество точных совпадений:", exact_match_count)
print("Количество частичных совпадений:", partial_match_count)


# Task 4
def replace_manufacturer(manufacturers, old_manufacturer, new_manufacturer):
    replaced_manufacturers = []

    for manufacturer in manufacturers:
        if manufacturer == old_manufacturer:
            replaced_manufacturers.append(new_manufacturer)
        else:
            replaced_manufacturers.append(manufacturer)

    return tuple(replaced_manufacturers)

# Кортеж с названиями производителей автомобилей
manufacturers = ("Ford", "Chevrolet", "Toyota", "Ford", "Honda", "Ford", "Nissan")

# Ввод названия производителя для замены
old_manufacturer = input("Введите название производителя, который нужно заменить: ")

# Ввод слова для замены
new_manufacturer = input("Введите слово для замены: ")

# Замена элементов в кортеже
replaced_manufacturers = replace_manufacturer(manufacturers, old_manufacturer, new_manufacturer)

# Вывод обновленного кортежа
print("Обновленный кортеж:", replaced_manufacturers)

# Task 5
def superset(set1, set2):
    if set1 == set2:
        print("Множества равны")
    elif set1.issuperset(set2):
        print(f"Объект {set1} является чистым супермножеством")
    else:
        print("Супермножество не обнаружено")

# Пример использования функции
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4}
superset(set1, set2)

set3 = {1, 2, 3}
set4 = {1, 2, 3}
superset(set3, set4)

set5 = {1, 2}
set6 = {3, 4}
superset(set5, set6)

# Task 6

def add_word(dictionary, word, translation):
    if word in dictionary:
        print("Слово уже существует в словаре.")
    else:
        dictionary[word] = translation
        print("Слово успешно добавлено в словарь.")

def delete_word(dictionary, word):
    if word in dictionary:
        del dictionary[word]
        print("Слово успешно удалено из словаря.")
    else:
        print("Слово не найдено в словаре.")

def search_word(dictionary, word):
    if word in dictionary:
        translation = dictionary[word]
        print(f"{word} - {translation}")
    else:
        print("Слово не найдено в словаре.")

def replace_translation(dictionary, word, new_translation):
    if word in dictionary:
        dictionary[word] = new_translation
        print("Перевод успешно заменен.")
    else:
        print("Слово не найдено в словаре.")

# Создание пустого словаря
dictionary = {}

# Основной цикл программы
while True:
    print("\n--- Англо-французский словарь ---")
    print("1. Добавить слово")
    print("2. Удалить слово")
    print("3. Поиск слова")
    print("4. Замена перевода")
    print("0. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        word = input("Введите слово на английском: ")
        translation = input("Введите перевод на французский: ")
        add_word(dictionary, word, translation)
    elif choice == "2":
        word = input("Введите слово на английском: ")
        delete_word(dictionary, word)
    elif choice == "3":
        word = input("Введите слово на английском: ")
        search_word(dictionary, word)
    elif choice == "4":
        word = input("Введите слово на английском: ")
        new_translation = input("Введите новый перевод на французский: ")
        replace_translation(dictionary, word, new_translation)
    elif choice == "0":
        break
    else:
        print("Некорректный ввод. Попробуйте снова.")

# Task 7
def set_gen(numbers):
    number_counts = {}
    result_set = set()

    for number in numbers:
        if number in number_counts:
            number_counts[number] += 1
        else:
            number_counts[number] = 1

    for number in numbers:
        count = number_counts[number]
        if count > 1:
            result_set.add(str(number) * count)
        else:
            result_set.add(number)

    return result_set

# Пример использования функции
numbers = [1, 2, 3, 4, 4, 4, 5, 5, 6, 7, 7, 7, 7]
result = set_gen(numbers)

# Вывод результата
print(result)


# Task 8

def biggest_dict(**kwargs):
    my_dict = {'first_one': 'we can do it'}
    my_dict.update(kwargs)
    return my_dict

# Пример использования функции
result = biggest_dict(k1=22, k2=31, k3=11, k4=91, name='Елена', age=31, weight=61, eyes_color='grey')

# Вывод результата
print(result)


# Task 9

def modify_dict(dictionary):
    keys = list(dictionary.keys())
    first_key = keys[0]
    last_key = keys[-1]

    # Меняем местами первый и последний элементы
    dictionary[first_key], dictionary[last_key] = dictionary[last_key], dictionary[first_key]

    # Удаляем второй элемент
    del dictionary[keys[1]]

    # Добавляем новый ключ и значение в конец
    dictionary['new_key'] = 'new_value'

# Создание словаря
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5'}

# Вывод исходного словаря
print("Исходный словарь:")
print(my_dict)

# Модификация словаря
modify_dict(my_dict)

# Вывод модифицированного словаря
print("Модифицированный словарь:")
print(my_dict)


# Task 10

import json

def add_data(dictionary, country, capital):
    if country in dictionary:
        print("Данные для этой страны уже существуют.")
    else:
        dictionary[country] = capital
        print("Данные успешно добавлены.")

def delete_data(dictionary, country):
    if country in dictionary:
        del dictionary[country]
        print("Данные успешно удалены.")
    else:
        print("Данные для этой страны не найдены.")

def search_data(dictionary, country):
    if country in dictionary:
        capital = dictionary[country]
        print(f"Столица страны {country}: {capital}")
    else:
        print("Данные для этой страны не найдены.")

def edit_data(dictionary, country, new_capital):
    if country in dictionary:
        dictionary[country] = new_capital
        print("Данные успешно отредактированы.")
    else:
        print("Данные для этой страны не найдены.")

def save_data(dictionary, filename):
    with open(filename, 'w') as file:
        json.dump(dictionary, file)
    print("Данные успешно сохранены.")

def load_data(filename):
    with open(filename, 'r') as file:
        dictionary = json.load(file)
    print("Данные успешно загружены.")
    return dictionary

# Создание пустого словаря
data_dict = {}

# Основной цикл программы
while True:
    print("\n--- Словарь стран и столиц ---")
    print("1. Добавить данные")
    print("2. Удалить данные")
    print("3. Поиск данных")
    print("4. Редактировать данные")
    print("5. Сохранить данные")
    print("6. Загрузить данные")
    print("0. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        country = input("Введите название страны: ")
        capital = input("Введите название столицы: ")
        add_data(data_dict, country, capital)
    elif choice == "2":
        country = input("Введите название страны: ")
        delete_data(data_dict, country)
    elif choice == "3":
        country = input("Введите название страны: ")
        search_data(data_dict, country)
    elif choice == "4":
        country = input("Введите название страны: ")
        new_capital = input("Введите новое название столицы: ")
        edit_data(data_dict, country, new_capital)
    elif choice == "5":
        filename = input("Введите имя файла для сохранения: ")
        save_data(data_dict, filename)
    elif choice == "6":
        filename = input("Введите имя файла для загрузки: ")
        data_dict = load_data(filename)
    elif choice == "0":
        break
    else:
        print("Некорректный ввод. Попробуйте снова.")
