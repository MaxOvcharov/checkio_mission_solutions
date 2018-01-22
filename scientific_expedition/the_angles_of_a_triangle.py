# coding: utf-8
"""
Даны длины сторон треугольника и необходимо найти углы
треугольника. Если невозможно сформировать треугольник из
данных сторон (или для вырожденного треугольника), тогда
результатом должны быть все нули.

Результат должен быть представлен, как список (list) целых чисел
в возрастающем порядке. Углы должны быть записаны в градусах и
округляются до целого числа (стандартное округление).

*********************** TASK *******************************
Предусловия:
0 < a,b,c ≤ 1000

Входные данные: Длины сторон треугольник, как целые числа (int).

Выходные данные: Углы данного треугольника в градусах, как
сортированный список (list) целых чисел (int).

"""
from math import acos, pi


def checkio(a, b, c):
    if a == b == c:
        return [60, 60, 60]
    elif (a < b+c) and (b < a+c) and (c < a+b):
        out = [round((acos((float(b ** 2 + c ** 2 - a ** 2)) / (float(2 * b * c)))) / (pi / 180)),
               round((acos((float(a ** 2 + c ** 2 - b ** 2)) / (float(2 * a * c)))) / (pi / 180)),
               round((acos((float(a ** 2 + b ** 2 - c ** 2)) / (float(2 * a * b)))) / (pi / 180))]
        return sorted(map(int, out))
    else:
        return [0, 0, 0]


#  These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
