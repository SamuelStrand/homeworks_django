# Task 1

import datetime


def get_week_number(year, month, day):
    date = datetime.date(year, month, day)
    week_number = date.isocalendar()[1]
    return week_number


# Ввод даты
year = int(input("Введите год: "))
month = int(input("Введите месяц: "))
day = int(input("Введите день: "))

# Получение номера недели
week_number = get_week_number(year, month, day)
print("Номер недели:", week_number)


# Task 2

def find_first_monday(year, week):
    # Находим первый день заданной недели
    first_day = datetime.datetime.strptime(f'{year}-W{week}-1', '%Y-W%W-%w')

    # Если первый день - понедельник, возвращаем его
    if first_day.weekday() == 0:
        return first_day

    # Иначе находим первый понедельник в следующей неделе
    monday = first_day + datetime.timedelta(days=(7 - first_day.weekday()))
    return monday


# Ввод года и номера недели
year = int(input("Введите год: "))
week = int(input("Введите номер недели: "))

# Нахождение даты первого понедельника
first_monday = find_first_monday(year, week)
print("Первый понедельник данной недели:", first_monday)


# Task 3
def find_sundays(year):
    sundays = []

    # Итерируемся по всем месяцам в году
    for month in range(1, 13):
        # Создаем первый день месяца
        first_day = datetime.date(year, month, 1)

        # Итерируемся по дням месяца
        for day in range(1, 32):
            try:
                # Создаем объект даты
                date = datetime.date(year, month, day)

                # Проверяем, является ли день воскресеньем
                if date.weekday() == 6:
                    sundays.append(date)

            except ValueError:
                # Если возникает ValueError, значит день выходит за пределы месяца
                break

    return sundays


# Ввод года
year = int(input("Введите год: "))

# Поиск всех воскресений
sundays = find_sundays(year)

# Вывод всех воскресений
print("Все воскресенья в", year, "году:")
for sunday in sundays:
    print(sunday)


# Task 4
def addYears(date, years):
    try:
        # Добавляем годы к дате
        new_date = date.replace(year=date.year + years)
    except ValueError:
        # Если возникает ValueError, значит дата выходит за пределы допустимого диапазона
        # В этом случае мы переносим дату на конец предыдущего месяца (28 февраля в обычном случае, 29 февраля в високосный год)
        new_date = date + datetime.timedelta(days=(365 * years + years // 4))

    return new_date


# Пример использования
print(addYears(datetime.date(2015, 1, 1), -1))
print(addYears(datetime.date(2015, 1, 1), 0))
print(addYears(datetime.date(2015, 1, 1), 2))
print(addYears(datetime.date(2000, 2, 29), 1))

# Task 6
# Получение текущего времени по Гринвичу
gmt_time = datetime.datetime.utcnow()
gmt_time_str = gmt_time.strftime("%Y-%m-%d %H:%M:%S")
print("Время по Гринвичу (UTC):", gmt_time_str)

# Получение текущего местного времени
local_time = datetime.datetime.now()
local_time_str = local_time.strftime("%Y-%m-%d %H:%M:%S")
print("Местное время:", local_time_str)


# Task 7
def calculate_days_between_dates(date1, date2):
    # Разница между датами
    delta = date2 - date1

    # Извлечение количества дней
    days = delta.days

    return days


# Ввод дат
date1_str = input("Введите первую дату в формате ГГГГ-ММ-ДД: ")
date2_str = input("Введите вторую дату в формате ГГГГ-ММ-ДД: ")

# Преобразование строковых значений в объекты datetime.date
date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d").date()
date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d").date()

# Вычисление количества дней между датами
days_between = calculate_days_between_dates(date1, date2)

# Вывод результата
print("Количество дней между", date1_str, "и", date2_str, ":", days_between)


# Task 8
def convert_timedelta_to_days_hours_minutes_seconds(timedelta):
    # Извлечение полных дней
    days = timedelta.days

    # Извлечение оставшихся секунд
    seconds = timedelta.seconds

    # Вычисление часов, минут и секунд
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return days, hours, minutes, seconds


# Ввод двух дат
date1_str = input("Введите первую дату и время в формате ГГГГ-ММ-ДД ЧЧ:ММ:СС: ")
date2_str = input("Введите вторую дату и время в формате ГГГГ-ММ-ДД ЧЧ:ММ:СС: ")

# Преобразование строковых значений в объекты datetime
date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")

# Вычисление разности дат
timedelta = date2 - date1

# Преобразование разности дат в дни, часы, минуты и секунды
days, hours, minutes, seconds = convert_timedelta_to_days_hours_minutes_seconds(timedelta)

# Вывод результата
print("Разница между", date1_str, "и", date2_str, ":")
print("Дни:", days)
print("Часы:", hours)
print("Минуты:", minutes)
print("Секунды:", seconds)

# Task 9

import calendar


def create_html_calendar(year, month):
    # Получение календаря в виде строки HTML
    calendar_str = calendar.HTMLCalendar().formatmonth(year, month)

    # Формирование HTML-кода для календаря
    html_calendar = f"""
    <html>
    <head>
        <title>Календарь {calendar.month_name[month]} {year}</title>
        <style>
            table {{
                border-collapse: collapse;
            }}
            td, th {{
                border: 1px solid black;
                padding: 5px;
            }}
        </style>
    </head>
    <body>
        <h2>{calendar.month_name[month]} {year}</h2>
        {calendar_str}
    </body>
    </html>
    """

    return html_calendar


# Ввод года и месяца
year = int(input("Введите год: "))
month = int(input("Введите номер месяца (1-12): "))

# Создание HTML-календаря
html_calendar = create_html_calendar(year, month)

# Запись HTML-кода в файл
file_name = f"calendar_{year}_{month}.html"
with open(file_name, "w") as file:
    file.write(html_calendar)

print(f"HTML-календарь сохранен в файле: {file_name}")

# Task 11

import re


def extract_domains(email_list):
    domain_list = []

    # Паттерн для поиска домена в e-mail адресе
    pattern = r"@(\w+\.\w+)"

    # Итерируемся по каждому e-mail адресу в списке
    for email in email_list:
        # Ищем домен в e-mail адресе с помощью регулярного выражения
        match = re.search(pattern, email)

        # Если найден домен, добавляем его в список
        if match:
            domain = match.group(1)
            domain_list.append(domain)

    return domain_list


# Ввод списка e-mail адресов
email_list = [
    "user1@example.com",
    "user2@test.com",
    "user3@gmail.com",
    "user4@domain.com"
]

# Извлечение доменов из списка e-mail адресов
domains = extract_domains(email_list)

# Вывод результатов
print("Домены из списка e-mail адресов:")
for domain in domains:
    print(domain)


# Task 12
def extract_vowel_words(text):
    # Паттерн для поиска слов, начинающихся на гласную букву
    pattern = r"\b[aeiouAEIOU]\w+\b"

    # Извлечение слов, начинающихся на гласную букву, с помощью регулярного выражения
    vowel_words = re.findall(pattern, text)

    return vowel_words


# Ввод текста
text = input("Введите текст: ")

# Извлечение слов, начинающихся на гласную букву
words = extract_vowel_words(text)

# Вывод результатов
print("Слова, начинающиеся на гласную букву:")
for word in words:
    print(word)


# Task 13

def split_string(string, delimiters):
    # Создание регулярного выражения с использованием переданных разделителей
    pattern = '|'.join(map(re.escape, delimiters))

    # Разбиение строки с помощью регулярного выражения
    splitted = re.split(pattern, string)

    return splitted


# Ввод строки
string = input("Введите строку: ")

# Ввод разделителей
delimiters = input("Введите разделители через пробел: ").split()

# Разбиение строки по разделителям
result = split_string(string, delimiters)

# Вывод результатов
print("Результат разбиения:")
for part in result:
    print(part)
