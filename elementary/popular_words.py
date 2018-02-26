# coding: utf-8
"""
Ваша задача в этой миссии определить популярность
  определенных слов в тексте.
На вход вашей функции передается 2 аргумента.
  Текст и массив слов, популярность которых необходимо определить.
При решении этой задачи обратите внимание на следующие моменты
Текст может быть многострочным и со знаками препинания
Слова необходимо искать во всеx регистрах. Т.е. если необходимо
  найти слово "one", значит для него будут подходить слова:
  "one", "One", "oNe", "ONE" и.т.д.
Искомые слова всегда указаны в нижнем регистре
Если слово не найдено ни разу, то его необходимо вернуть в
  словаре со значением 0 (ноль)
*********************** TASK *******************************
Input: Текст и массив искомых слов.

Output: Словарь, в котором ключами являются искомые слова и
  значениями то, сколько раз они встречаются в исходном тексте.
"""
import collections
import re


# best solution
def popular_words_my(text, words):
    text = text.lower()
    return {word: text.count(word) for word in words}


def popular_words(text, words):
    res = collections.defaultdict(lambda: 0)
    for i in re.findall("([\w']+)", text):
        res[i.lower()] += 1
    return {w: res[w] for w in words}


if __name__ == '__main__':
    print("Example:")
    print(popular_words_my('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words_my('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']) == {
        'i': 4,
        'was': 3,
        'three': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")