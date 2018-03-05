# coding: utf-8
"""
Медиана - это числовое значение, которое делит сортированый
  массив чисел на большую и меньшую половины. В сортированом
  массиве с нечетным числом элементов медиана - это число в
  середине массива. Для массива с четным числом элементов,
  где нет одного элемента точно посередине, медиана - это
  среднее значение двух чисел, находящихся в середине массива.

В этой задаче дан непустой массив натуральных чисел.

Вам необходимо найти медиану данного массива.
*********************** TASK *******************************
Предусловия:
1 < len(data) ≤ 1000
all(0 ≤ x < 10 ** 6 for x in data)

Input: Массив как список (list) чисел (int).

Output: Медиана как число (int, float).
"""


def quick_sort(alist):

    quick_sort_helper(alist, 0, len(alist)-1)


def quick_sort_helper(alist, first, last):
    if first < last:

        splitpoint = partition(alist, first, last)

        quick_sort_helper(alist, first, splitpoint-1)
        quick_sort_helper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]
    leftmark, rightmark = first + 1, last

    done = False
    while not done:

        while leftmark <= rightmark and \
                alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and \
                rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark


def checkio_my(data):
    data.sort()
    if len(data) % 2 == 0:
        return (data[len(data) // 2] + data[(len(data) // 2) - 1]) / 2.0
    else:
        return data[len(data)//2]


# best solution
def checkio(data):
    data.sort()
    half = len(data) // 2
    return (data[half] + data[~half]) / 2


#  These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("The local tests are done.")
