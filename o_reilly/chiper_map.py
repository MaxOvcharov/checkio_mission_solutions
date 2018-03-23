# coding: utf-8
"""
Помогите Софи написать дешифратор для паролей, которые
  Никола зашифровал с помощью шифровальной решетки.
  Шифрорешетка - это квадрат 4 на 4 с четырьмя вырезанными
  окошками. Поместите решетку на листе бумаги такого же
  размера с буквами, выписываете первые 4 символа, которые
  видно в окошках (см. рисунок). Затем поверните решетку
  на 90 градусов по часовой стрелке. Выпишите следующие
  символы и повторите поворот. В итоге процедура повторяется
  4 раза. Таким образом сложно узнать пароль без специальной
  решетки.

Напишите программу, которая поможет проводить данную процедуру.

Шифровальная решетка и зашифрованный пароль представлены,
  как массив строк
*********************** ЗАДАНИЕ *******************************
Предусловия: len(cipher_grille) == 4
len(ciphered_password) == 4
all(len(row) == 4 for row in ciphered_password)
all(len(row) == 4 for row in cipher_grille)
all(all(ch in string.ascii_lowercase for ch in row) for row in ciphered_password)
all(all(ch == "X" or ch == "." for ch in row) for row in cipher_grille)

Ввод: Шифровальная решетка и зашифрованный пароль, как список (list) строк.

Вывод: Пароль, как строка.
"""
from itertools import chain, product


def recall_password_my(cipher_grille, ciphered_password):
    rotated_0 = tuple(tuple(row) for row in cipher_grille)
    rotated_90 = tuple(zip(*reversed(rotated_0)))
    rotated_180 = tuple(zip(*reversed(rotated_90)))
    rotated_270 = tuple(zip(*reversed(rotated_180)))

    cipher_grilles = (
        cipher_grille,
        rotated_90,
        rotated_180,
        rotated_270
    )

    res = []
    for cipher_grille in cipher_grilles:
        for i, row in enumerate(cipher_grille):
            res.append([ciphered_password[i][j] for j, ch in enumerate(row) if ch == 'X'])

    return ''.join(chain(*res))


# best solution
def recall_password(cipher_grille, ciphered_password):
    s = ''
    for i in range(4):
        cipher_grille = tuple(zip(*reversed(cipher_grille)))

        for x, y in product(range(4), range(4)):
            if cipher_grille[x][y] == "X":
                s += ciphered_password[x][y]

    return s[-4:] + s[:-4]


if __name__ == '__main__':
    #  These "asserts" using only for self-checking and not necessary for auto-testing

    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'