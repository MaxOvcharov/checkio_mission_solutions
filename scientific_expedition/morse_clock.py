# coding: utf-8
"""
Помогите Стефану создать программный модуль для перевода
  времени представленного в нормальном виде, в двоичную Морзе-форму.

Взгляните на иллюстрацию, Серые кружки значат "включено",
  а белые - "выключено". Каждая цифра в написании времени
 представлена разным количеством бинарных знаков.

Первая цифра в "часах" состоит из двух знаков, тогда как
  вторая цифра -- из четырех. Первая цифра "минут" и "секунд"
  состоят из трех знаков и вторые цифры -- из четырех.

Каждая цифра должна быть переведена в двоичный вид.

Затем замените каждую единицу (1) на тире ("-") и каждый
  ноль (0) на точку (".").

Время может быть представлено в следующем виде: "hh:mm:ss",
  "h:m:s" или "hh:m:ss" "Пропущеные" цифры - это нули.
  Для примера, "1:2:3" тоже самое, что и "01:02:03".

Окончательная морзе-форма времени должна быть написана в
следующем формате: "h h : m m : s s"

где каждая цифра - это последовательность "." и "-"

*********************** TASK *******************************
Предусловия:
В time_string всегда правильное время.

Ввод: Нормальная запись времени, представленая строкой (str).

Вывод: Переработаная морзе-форма времени, представленая строкой (str).
"""


def checkio_my(time_string):
    a = []
    for x in time_string.split(":"):
        if len(x) % 2 == 0:
            for i in x:
                a.append(int(i))
        else:
            x = x.rjust(2, '0')
            for i in x:
                a.append(int(i))

    segl = [2, 4, 3, 4, 3, 4]
    out = [(bin(a[j]).lstrip('0b')).rjust(segl[j], '0') for j in range(len(a))]
    out = [i.replace('1', '-') for i in out]
    out = [j.replace('0', '.') for j in out]
    return (out[0] + " " + out[1] + " " + ":" + " " + out[2]
            + " " + out[3] + " " + ":" + " " + out[4] + " " + out[5])


TO_MORSE = str.maketrans('01', '.-')


def to_morse(number, bits):
    """Return number in binary-Morse as a string with the given number of bits."""
    return "{0:0{1}b}".format(number, bits).translate(TO_MORSE)


def to_code(field):
    """Return a space-delimited string of binary-Morse digits."""
    tens, ones = divmod(int(field), 10)
    return "{} {}".format(to_morse(tens, 3), to_morse(ones, 4))


def checkio_best_solution(data):
    """Return a string representing the time in a Morse code-like form."""
    return ' : '.join(map(to_code, data.split(':')))[1:]  # Strip leading.


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio_my(u"10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio_my(u"21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio_my(u"00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio_my(u"23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
