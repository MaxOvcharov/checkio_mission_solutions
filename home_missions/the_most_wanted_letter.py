# coding: utf-8
"""
Дан текст, который содержит различные английские буквы и знаки препинания.
Вам необходимо найти самую частую букву в тексте. Результатом должна быть
буква в нижнем регистре.

При поиске самой частой буквы, регистр не имеет значения, так что при
подсчете считайте, что "A" == "a". Убедитесь, что вы не считайте знаки
препинания, цифры и пробелы, а только буквы.

Если в тексте две и больше буквы с одинаковой частотой, тогда результатом
будет буква, которая идет первой в алфавите. Для примера, "one"
содержит "o", "n", "e" по одному разу, так что мы выбираем "e".

*********************** TASK *******************************

Предусловия:
text содержит только ASCII символы.
0 < len(text) ≤ 105

Вх. данные: Текст для анализа, как строка.

Вых. данные: Наиболее частая буква, как строка.
"""
import string


def checkio_my(text):
    a = list(text.lower())
    a.sort()
    count = [0, 0]
    for i in a:
        if i.isalpha():
            temp = a.count(i)
            if temp > count[0]:
                count[0] = temp
                count[1] = i
    return count[1]


def checkio_best_solution(text):
    """
    We iterate through latyn alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from they.
    """
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)


if __name__ == '__main__':
    #  These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio_my(u"Hello World!") == "l", "Hello test"
    assert checkio_my(u"How do you do?") == "o", "O is most wanted"
    assert checkio_my(u"One") == "e", "All letter only once."
    assert checkio_my(u"Oops!") == "o", "Don't forget about lower case."
    assert checkio_my(u"AAaooo!!!!") == "a", "Only letters."
    assert checkio_my(u"abe") == "a", "The First."
    print("Start the long test")
    assert checkio_my(u"a" * 9000 + u"b" * 1000) == "a", "Long."
    print("The local tests are done.")
