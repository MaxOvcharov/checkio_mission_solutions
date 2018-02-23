# coding: utf-8
"""
Your mission here is to create a function that gets an tuple
  and returns a tuple with 3 elements - first, third and
  second to the last for the given tuple
*********************** TASK *******************************
Input: A tuple, at least 3 elements long.

Output: A tuple.
"""


def easy_unpack_my(elements):
    """
        returns a tuple with 3 elements - first, third and second to the last
    """
    try:
        res = tuple(elements[i] for i in [0, 2, -2])
    except IndexError:
        res = 0
    return res


def easy_unpack_best_solution(elements):
    return elements[0], elements[2], elements[-2]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert easy_unpack_my((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack_my((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack_my((6, 3, 7)) == (6, 7, 3)
    assert easy_unpack_my((6, 3)) == 0
    print('Done! Go Check!')
