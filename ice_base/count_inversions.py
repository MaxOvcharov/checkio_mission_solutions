# coding: utf-8
"""
В комьютерной науке и дискретной математике, инверсия
  - это пара позиций последовательности, где элементы
  на этих позициях выпадают из естественного порядка.
  Таким образом, если мы используем порядок по возрастанию
  для группы чисел, то инверсия получается, когда более
  крупные цифры стоят перед меньшим значением в последовательности.

Проверим такой пример последовательности: (1, 2, 5, 3, 4, 7, 6)
  и мы можем видеть здесь три инверсии - 5 и 3; - 5 и 4; - 7 и 6.

Вам дана последовательность уникальных чисел и вы должны
  подсчитать число инверсий в этой последовательности.

*********************** TASK *******************************
Предусловия:
2 < len(sequence) < 200
len(sequence) == len(set(sequence))
all(-100 < x < 100 for x in sequence)

Входные данные: Последовательность как кортеж целых чисел.

Выходные данные: Количество инверсий.
"""


# Best solutions
def count_inversion_my1(sequence):
    count, slen = 0, len(sequence)
    for i in range(slen):
        for j in range(i+1, slen):
            if sequence[i] > sequence[j]:
                count += 1
    return count


def count_inversion_my2(sequence):
    slen = len(sequence)
    return sum(1 for i in range(slen) for j in range(i+1, slen) if sequence[i] > sequence[j])


if __name__ == '__main__':
    #  These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion_my1((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion_my1((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion_my1((99, -99)) == 1, "Two numbers"
    assert count_inversion_my1((5, 3, 2, 1, 0)) == 10, "Reversed"
