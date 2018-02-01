# coding: utf-8
"""
Дана строка и нужно найти ее первое слово.

При решении задачи обратите внимание на следующие моменты:

В строке могут встречатся точки и запятые
Строка может начинаться с буквы или, к примеру, с пробела или точки
В слове может быть апостроф и он является частью слова
Весь текст может быть представлен только одним словом и все

*********************** TASK *******************************
Предисловие:
текст может содержать - a-z A-Z , . '

Входные параметры: Строка.

Выходные параметры: Строка.
"""
import re

from string import punctuation


def first_word_my(text: str) -> str:
    """
        returns the first word in a given text.
    """
    p = punctuation.translate(str.maketrans("", "", "'"))
    return text.strip(punctuation + ' ').split()[0].strip(p).split('.')[0]


def first_word_best_solutions(text: str) -> str:
    return re.search("([\w']+)", text).group(1)


if __name__ == '__main__':
    print("Example:")
    print(first_word_my("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word_my("Hello world") == "Hello"
    assert first_word_my(" a word ") == "a"
    assert first_word_my("don't touch it") == "don't"
    assert first_word_my("greetings, friends") == "greetings"
    assert first_word_my("... and so on ...") == "and"
    assert first_word_my("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")