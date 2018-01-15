# coding: utf-8
"""
Роботы решили покопаться в себе и может быть даже улучшить что-нибудь.
В этой задаче Вам нужно написать свою реализацию встроенных функций
(версии для py3) min и max. Некоторые встроенные функции
заблокированы здесь: import, eval, exec, globals. Не забудьте,
что в этой задаче вам нужно реализовать две функции, а не одну как обычно.

max(iterable, *[, key]) or min(iterable, *[, key])
max(arg1, arg2, *args[, key]) or min(arg1, arg2, *args[, key])

Возвращает наибольший (наименьший) элемент в итерируемом (iterable)
или наибольшее (наименьшее) из двух и более аргументов.

Если дан только один позиционный аргумент, то он должен быть итерируемым. В этом
случае функция возвращает наибольший (наименьший) элемент из данного итерируемого.

Если даны два или более позиционных аргумента, то возвращен будет
наибольший (наименьший) из данных аргументов.

Необязательный ключевой аргумент key определяет функцию одного аргумента,
которая используется для извлечения ключа для сравнения из каждого элемента
массива (для примера, key=str.lower).

Если массив содержит несколько максимальных (минимальных) значений,
то функция возвращает первый по порядку в массиве.

*********************** ЗАДАНИЕ *******************************

Предусловия: Все тесты корректны, согласно описания функции и не должны порождать исключения.

Ввод: Один позиционный аргумент, как итерируемое или два или
более позиционных аргументов. Необязательный ключевой аргумент, как функция.

Вывод: Наибольший элемент для "max" функции и наименьший для "min" функции.
"""


def get_first_from_sorted(args, key, reverse):
    if len(args) == 1:
        args = iter(args[0])
    return sorted(args, key=key, reverse=reverse)[0]


def min(*args, **kwargs):
    key = kwargs.get("key", None)
    return get_first_from_sorted(args, key, False)


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    return get_first_from_sorted(args, key, True)


if __name__ == '__main__':
    #  These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")