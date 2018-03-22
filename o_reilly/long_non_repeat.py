# coding: utf-8
"""
Это вторая миссия, которая по своей сути схожа с первой
  миссией серии, но требует другого направления поиска.
  Здесь Вам необходимо найти первую самую длинную подстроку
  состоящую исключительно из неповторяющихся букв. Например,
  в строке "abca" мы имеем две подстроки с неповторяющимися
  буквами "abc" и "bca", но нам нужна первая подстрока,
  поэтому ответом будет "abc".

*********************** ЗАДАНИЕ *******************************
Ввод: Строка.

Вывод: Строка.
"""


def non_repeat(line):
    """
        the longest substring without repeating chars
    """
    # your code here
    return line


if __name__ == '__main__':
    #  These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    print('"Run" is good. How is "Check"?')
