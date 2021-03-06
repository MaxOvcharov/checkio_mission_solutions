# coding: utf-8
"""
Нашему Робо-Трио необходимо тренироваться для будущих приключений
  и охоты за сокровищами (золотые контакты нужны всем). Стефан
  построил специальную упрощенную модель пирамиды. И теперь наши
  роботы будут тренироваться в забегах за золотом на скорость.
  Они начинают с вершины пирамиды и собирают золото в каждой
  комнате, через которую проходят. В каждой комнате они выбирают
  влево или вправо и спускаются на следующий уровень. Чтобы
  оценивать результаты, Стефану нужно знать, а сколько максимум
  можно собрать за один забег.

Представьте кортеж (tuple) кортежей в котором первый массив имеет
  одно число и следующие на одно число больше чем предыдущий.
  Такой кортеж кортежей будет выглядеть как треугольник. Вам
  нужно написать функцию, которая поможет Стефану найти
  максимальную сумму золота на самом выгодном маршруте с вершины
  пирамиды до ее основания. Все маршруты прохода по пирамиде из
  шагов вниз и влево/вправо.

Примечание:
Попробуйте думать о шаге вниз-влево, как о движении
  в следующий ряд не изменяя индекс в ряду и о шаге вниз/вправо
  -- с увеличением индекса в ряду на единицу. Будьте осторожны
  если вы хотите решать задачу рекурсией. получится медленное решение.
*********************** ЗАДАНИЕ *******************************
Предусловия:
0 < len(pyramid) ≤ 20
all(all(0 < x < 10 for x in row) for row in pyramid)

Ввод: Пирамида, как кортеж (tuple) кортежей. Каждый кортеж
  содержит целочисленное (int).

Вывод: Максимально количество золота за один забег,
  как целочисленное (int).
"""


def get_cost(costs, i, j):
    """ returns 0 if you get out of pyramid """
    if j < 0 or i < 0:
        return 0
    try:
        return costs[i][j]
    except IndexError:
        return 0


def count_gold_my(pyramid):
    """
    Return max possible sum in a path from top to bottom
    """

    costs = []  # max costs of i,j-position
    for i in range(0, len(pyramid)):
        costs.append([])
        for j in range(0, len(pyramid[i])):
            if i == j == 0:
                costs[i].append(pyramid[i][j])
            else:
                cij = pyramid[i][j] + max(get_cost(costs, i - 1, j - 1), get_cost(costs, i - 1, j))
                costs[i].append(cij)

    return max(costs[-1])


# best solution
def count_gold(pyramid):
    pyramid_list = [list(row) for row in pyramid]
    for i in range(len(pyramid_list) - 2, -1, -1):
        for j in range(i + 1):
            pyramid_list[i][j] += max(pyramid_list[i + 1][j], pyramid_list[i + 1][j + 1])

    return pyramid_list[0][0]


if __name__ == '__main__':
    #  These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"
