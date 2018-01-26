# coding: utf-8
"""
Панграмма (Греческий:παν γράμμα, pan gramma, "каждая буква")
  или предложение состоящее из разных букв алфавита, используя
  каждую букву по крайней мере один раз. Возможно, вы знакомы с
  хорошо известными панграммами "Эй, жлоб! Где туз? Прячь юных
  съёмщиц в шкаф" или "Любя, съешь щипцы, — вздохнёт мэр, — кайф жгуч".

Для этого задания, вы будете использовать латинский алфавит (A-Z).
  У вас есть текст с латинскими буквами и знаками препинания.
  Вы должны проверить является ли предложение панграммой или нет.
  Регистр не имеет значения.

*********************** TASK *******************************
Предусловия:

all(ch in (string.punctuation + string.ascii_letters + " ") for ch in text)
0 < len(text)

Входные данные: Текст как строка.

Выходные данные: Является предложение панграммой или нет как логическое.
"""
from string import ascii_lowercase


def check_pangram_my1(text):
    out = text.lower()
    return all(i in out for i in ascii_lowercase)


def check_pangram_my2(text):
    return set(ascii_lowercase).issubset(set(text.lower()))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram_my2("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram_my2("ABCDEF"), "ABC"
    assert check_pangram_my2("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
