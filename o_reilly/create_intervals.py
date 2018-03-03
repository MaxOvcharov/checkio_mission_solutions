# coding: utf-8
"""
Из множества(set) целых чисел(int) вам нужно создать
  список(list) замкнутых интервалов в виде кортежей(tuple)
  таких, чтобы интервалы охватывали все значения, найденные в множестве.

Замкнутый интервал включает в себя конечные точки! Интервал 1..5 ,
  например, включает каждое значение x , которое удовлетворяет
  условию: 1 <= x <= 5.

Значения могут быть в одном интервале только если разность между
  значением и следующим меньшим значением в наборе равно единице,
  иначе начинается новый интервал.

Отдельное значение, которое не вписывается в существующие правила
  формирования интервалов, становится начальной и конечной точкой
  нового интервала.
*********************** TASK *******************************
Input: множество(set) целых чисел(int).

Output: список кортежей двух целых чисел(A list of tuples of two ints),
  обозначающими концы промежутка. Массив должен быть отсортирован
  по начальной точке каждого интервала.
"""


def create_intervals_my(data):
    """
        Create a list of intervals out of set of ints.
    """

    cur, priv, res, tmp = 0, 0, [], []
    for cur in sorted(data):
        if priv != 0 and cur - priv == 1:
            priv = cur
            tmp.append(cur)
        elif priv == 0:
            priv = cur
            tmp.append(cur)
        elif priv > cur:
            res.append(tmp)
            tmp = []
        else:
            res.append(tmp)
            priv, tmp = cur, []
            tmp.append(cur)

    res.append(tmp)
    return [(i[0], i[-1]) for i in res if i]


# best solution
def create_intervals(data):
    c = []
    while len(data) != 0:
        a = min(data)
        data = data-{a}
        b = a+1
        while b in data:
            data = data-{b}
            b += 1
        c.append((a, b-1))
    return c


if __name__ == '__main__':
    #  These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')
