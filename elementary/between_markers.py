# coding: utf-8
"""
Вам дана строка и два маркера (начальный и конечный).

Вам необходимо найти текст, заключенный между двумя
  этими маркерами. Но есть несколько важных условий:

Начальный и конечный маркеры всегда разные:

Если нет начального маркера, то началом считать начало строки;

Если нет конечного маркера, то концом считать конец строки;

Если нет ни конечно ни начального маркеров, то просто вернуть всю строку;

Если конечный маркер стоит перед начального, то вернуть пустую строку.

*********************** TASK *******************************
Предусловия: не может быть более одного маркера одного типа

Input: Три аргумента. Все строки. Второй и третий аргументы это
начальный и конечный маркеры.

Output: Строка.
"""


# My solution faster
def between_markers_my(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    begin_len, start_i, end_i = len(begin), text.find(begin), text.find(end)
    if start_i == end_i == -1:
        res = text
    elif start_i == -1:
        res = text[:end_i]
    elif end_i == -1:
        res = text[start_i + begin_len:]
    elif start_i > end_i:
        res = ""
    else:
        res = text[start_i + begin_len:end_i]
    return res


def between_markers_best_solution(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    return text[text.find(begin) + len(begin) if text.find(begin) >= 0 else 0:
                text.find(end) if text.find(end) >= 0 else len(text)]


if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert between_markers_my('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers_my("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers_my('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers_my('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers_my('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers_my('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
