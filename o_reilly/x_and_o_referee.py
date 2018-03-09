# coding: utf-8
"""
Крестики и Нолики - это игра для двух игроков (Х и О),
  которые расставляют эти знаки на 3х3 поле. Игрок,
  который сумел разместить три своих знака в любой г
  оризонтали, вертикали или диагонали -- выигрывает.

Но сейчас мы не будем играть в эту игру. Вы будете судить
  игру, и оценивать результат. Вам дан результат игры, и
  вы должны решить, кто победил или что это ничья. Ваша
  функция должна вернуть "X" если победил Х-игрок и "О"
  если победил О-игрок. В случае ничьи, результат должен быть "D".
Результаты игры представлены, как список (list) строк,
где "X" и "O" - это отметки игроков и "." - это пустая клетка.
*********************** TASK *******************************
Предусловия:
В играх может быть только один победитель или ничья.
len(game_result) == 3
all(len(row) == 3 for row in game_result)

Input: Результат игры, как список (list) строк (str, unicode).

Output: "X", "O" или "D", как строка (str).

"""


def checkio(net):
    cash = [str(net[0][0] + net[0][1] + net[0][2]),
            str(net[1][0] + net[1][1] + net[1][2]),
            str(net[2][0] + net[2][1] + net[2][2]),
            str(net[0][0] + net[0][1] + net[0][2]),
            str(net[0][1] + net[1][1] + net[2][1]),
            str(net[0][2] + net[1][2] + net[2][2]),
            str(net[0][0] + net[1][1] + net[1][1]),
            str(net[0][2] + net[1][1] + net[2][0])]
    for i in cash:
        if i == "XXX":
            return "X"
        elif i == "OOO":
            return "O"

    return "D"


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
    assert checkio([
        u"O.X",
        u"XX.",
        u"XOO"]) == "X", "Xs wins again"
