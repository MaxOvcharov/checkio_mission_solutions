# coding: utf-8
"""
Стефану нужна помощь для строительства круглой посадочной
  площадки с использованием ледяных блоков. Прежде чем начать,
  ему нужно знать сколько квадратных блоков ему понадобится.

Каждый квадратный блок имеет размер 1x1 метр. Подсчитайте,
  сколько нужно целых блоков и сколько колотых для круга радиусом
  N метров. Центр круга находится в пересечении 4 блоков.
  Для примера: для круга радиусом 2 метра требуется 4 целых и
  12 колотых блока.
*********************** ЗАДАНИЕ *******************************
Предусловия: 0 < radius ≤ 4

Ввод: Радиус круга, как число (int, float)

Вывод: Количество блоков, как список (list) двух чисел - [целые, колотые].
"""
from math import sqrt
from itertools import product


def checkio(radius):
    solid = partial = 0
    for x, y in product(range(int(radius)+1), range(int(radius)+1)):
        if sqrt((x+1)**2 + (y+1)**2) < radius:
            solid += 1
        elif sqrt(x**2 + y**2) < radius:
            partial += 1

    return [4*solid, 4*partial]


#  These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(2) == [4, 12], "N=2"
    assert checkio(3) == [16, 20], "N=3"
    assert checkio(2.1) == [4, 20], "N=2.1"
    assert checkio(2.5) == [12, 20], "N=2.5"
