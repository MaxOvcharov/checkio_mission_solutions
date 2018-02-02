# coding: utf-8
"""
Вам даны 2 строки и надо найти индекс второго вхождения второй строки в первую.

Разберем самый первый пример, когда необходимо найти второе вхождение "s" в
слове "sims". Если бы нам надо было найти ее первое вхождение, то тут все
просто с помощью функции index или find мы можем узнать, что "s" это самый
первый символ в слове "sims" а значит индек первого вхождения 0.

Но нам необходимо найти вторую "s", а она 4ая по счету, значит индекс
второго входжения (и ответ за вопрс) 3.

*********************** TASK *******************************
Input: Две строки (String).

Output: Int or None
"""


def second_index_my(text: str, symbol: str):
    """
        returns the second index of a symbol in a given text
    """
    # your code here
    res = text.find(symbol, text.find(symbol)+1)
    return res if res != -1 else None


if __name__ == '__main__':
    print('Example:')
    print(second_index_my("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index_my("sims", "s") == 3, "First"
    assert second_index_my("find the river", "e") == 12, "Second"
    assert second_index_my("hi", " ") is None, "Third"
    assert second_index_my("hi mayor", " ") is None, "Fourth"
    assert second_index_my("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')
