# coding: utf-8
"""
"Fizz buzz" это игра со словами, с помощью которой
 мы будем учить наших роботов делению. Давайте обучим компьютер.

Вы должны написать функцию, которая принимает положительное
целое число и возвращает:

"Fizz Buzz", если число делится на 3 и 5;

"Fizz", если число делится на 3;

"Buzz", если число делится на 5;

Число, как строку для остальных случаев.

*********************** TASK *******************************
Предусловия: 0 < number ≤ 1000

Входные данные: Число, как целочисленное (int).

Выходные данные: Ответ, как строка (str).
"""


def checkio(number):
    if (number > 0) and (number <= 1000):
        if (number % 3) == 0 and (number % 5) == 0:
            return "Fizz Buzz"
        elif number % 3 == 0:
            return "Fizz"
        elif number % 5 == 0:
            return "Buzz"
    return str(number)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
