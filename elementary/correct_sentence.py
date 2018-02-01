# coding: utf-8
"""
На вход Вашей функции будет передано одно предложение.
  Необходимо вернуть его исправленную копию так,
  чтобы оно всегда начиналось с большой буквы и
  заканчивалось точкой.

Обратите внимание на то, что не все исправления необходимы.
  Если предложение уже заканчивается на точку, то добавлять
  еще одну не нужно, это будет ошибкой

*********************** TASK *******************************
Предусловия:
В начале и конце нет пробелов, текст состоит
только из пробелов, a-z A-Z , и .

Входные аргументы: Строка (A string).

Выходные аргументы: Строка (A string).
"""


def correct_sentence_my(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    return text.capitalize() + "." if not text.endswith('.') else text.capitalize()


def correct_sentence_best_solutions(text: str) -> str:
    """Corrected sentence starting with a capital letter, ending with a dot."""
    return text.capitalize() + '.' * (not text.endswith('.'))


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence_my("greetings, friends"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence_my("greetings, friends") == "Greetings, friends."
    assert correct_sentence_my("Greetings, friends") == "Greetings, friends."
    assert correct_sentence_my("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence_my("hi") == "Hi."
    print("Coding complete? Click 'Check' to earn cool rewards!")
