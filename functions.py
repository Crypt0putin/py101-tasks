"""Задания по ветвлениям, итерациям и вводу данных."""

# напиши функцию, которая принимает на вход любое
# количество чисел и сообщает, есть ли среди них чётное

def even_exist():
    user_ints = input('Введите несколько чисел через пробел')
    listing = sorted(user_ints.split(' '))
    try:
        result = [int(i) for i in listing]
        for i in result:
            if i % 2 == 0:
                print("четное число найдено!")
                break
    except (ValueError, TypeError):
        print('"' + string + '"' + ' - не является числом. Необходимы числа через пробел.')

# используй тернарный оператор, чтобы вызвать функцию
# если возраст больше 21 года, в противном случае верни
# сообщение "Мы не продаём алкоголь несовершеннолетним."

age = 17
if age > 21:
    sell_alcohol()
else:
        print('Мы не продаём алкоголь несовершеннолетним')


# напиши функцию, которая проверит, является ли строка ключевым словом в Питоне
# тебе понадобится модуль keyword, импортируй его и изучи с помощью dir()

def kwcheck(x):
    import keyword
    print(x in dir([keyword.kwlist]))

# напиши функцию, которая возвращает тип данных на русском языке:
# число, строка, булевый, None, список, кортеж, множество, словарь
# пример: get_type("что-то") возвращает "Это строка."
# пример2: get_type(42) возвращает "Это словарь."

def get_type(x):
    if isinstance(x, str):
        print('Это строка')
    elif isinstance(x, int):
        print('Это число')
    elif isinstance(x, float):
        print('Это число с плавающей точкой')
    elif isinstance(x, list):
        print('Это список')
    elif isinstance(x, tuple):
        print('Это кортежч')
    elif isinstance(x, dict):
        print('Это словарь')
    elif isinstance(x, set):
        print('Это множество')
    elif isinstance(x, set):
        print('Это множество')
    elif isinstance(x, Boolean):
        print('Это логическая переменная')
    elif isinstance(x, None):
        print('Это неопределенное значение переменной')


