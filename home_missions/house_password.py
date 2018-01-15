# coding: utf-8
"""
Стефан и София забывают о безопасности и используют простые
пароли для всего. Помогите Николе разработать модуль для
проверки паролей на безопасность.

Пароль считается достаточно стойким, если его длина больше
или равна 10 символам, он содержит, как минимум одну цифру,
одну букву в верхнем и одну в нижнем регистре.

Пароль может содержать только латинские буквы и/или цифры.
*********************** TASK *******************************

Предусловия:
re.match("[a-zA-Z0-9]+", password)
0 < len(password) ≤ 64

Вх. данные: Пароль как строка (str, unicode).

Вых. данные: Безопасность пароля в виде булевого значения (bool)
или любого типа данных, который может быть сконвертирован и
представлен как булево значение (True или False)
"""


def checkio_my(pas):
    if len(pas) < 10:
        return False
    numbers = sum(c.isdigit() for c in pas)
    upper_str = sum(c.isupper() for c in pas)
    lower_str = sum(c.islower() for c in pas)
    return True if (upper_str > 0) and (lower_str > 0) and (numbers > 0) else False


checkio_best_solution = lambda s: not(
        len(s) < 10
        or s.isdigit()
        or s.isalpha()
        or s.islower()
        or s.isupper()
    )

if __name__ == '__main__':
    #  These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio_my(u'A1213pokl') == False, "1st example"
    assert checkio_my(u'bAse730onE4') == True, "2nd example"
    assert checkio_my(u'asasasasasasasaas') == False, "3rd example"
    assert checkio_my(u'QWERTYqwerty') == False, "4th example"
    assert checkio_my(u'123456123456') == False, "5th example"
    assert checkio_my(u'QwErTy911poqqqq') == True, "6th example"
