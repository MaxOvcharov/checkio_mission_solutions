"""
Шахматы известны по всему миру, и практически всем людям знакомы
их основные правила игры. В игре используется набор фигур,
которые могут ходить по игровому полю различными способами,
что обеспечивает огромное количество различных игровых комбинаций
(к примеру, количество возможных шахматных партий оценивается
Шенноном в 10^118). В этой задаче мы будем исследовать правила игры пешками.

Шахматы - это стратегическая игра двух игроков, которая разыгрывается
на игровой доске с клетками, расположенными в восьми рядах (называемых
горизонталями и обозначаемых цифрами от 1 до 8) и в восьми колонках
(называемых вертикалями и обозначаемых буквами от a до h). Каждая клетка
доски идентифицируется уникальной парой координат, состоящей из буквы и
цифры (например, "a1", "h8", "d6"). В этой задаче мы будем иметь дело
только с пешками. Пешка может бить пешку противника, которая находится
перед ней в соседней клетке по диагонали справа или слева, переходя в эту
клетку. У белых пешек клетки перед ними имеют номер горизонтали на единицу больше.

Сама по себе пешка является слабой фигурой, но мы можем использовать до восьми
пешек для построения оборонительной стены. Стратегия оборонительной стены
основывается на защите друг друга. Пешка защищена, если её клетка находится по
ударом другой своей пешки. На игровом поле находятся только белые пешки.
Вы должны разработать код, позволяющий определить сколько пешек защищены в этой позиции.

*********************** TASK *******************************
Предусловия: 0 < pawns ≤ 8

Входные данные: Координаты расставленных пешек в виде набора строк.

Выходные данные: Количество защищенных пешек в виде целого числа.
"""


def safe_pawns_my(pawns):
    x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    safe_pawns_counter = 0
    for pawn in pawns:
        x_pawn, y_pawn = pawn
        x_ind = x.index(x_pawn)
        safeguards = set()
        if int(y_pawn) <= 1: continue
        if x_pawn != 'a' and x_pawn != 'h':
            safeguards.update({
                ''.join([x[x_ind - 1], str(int(y_pawn) - 1)]),
                ''.join([x[x_ind + 1], str(int(y_pawn) - 1)])
            })
        else:
            if x_pawn != 'a':
                safeguards.add(''.join([x[x_ind - 1], str(int(y_pawn) - 1)]))
            else:
                safeguards.add(''.join([x[x_ind + 1], str(int(y_pawn) - 1)]))

        if not pawns.isdisjoint(safeguards):
            safe_pawns_counter += 1
        safeguards.clear()
    return safe_pawns_counter


def safe_pawns_best_solution(pawns):
    return sum([1 for elem in pawns if chr(ord(elem[0]) + 1) + str(int(elem[1]) - 1) in pawns or chr(ord(elem[0]) - 1) + str(int(elem[1]) - 1) in pawns])


if __name__ == '__main__':
    #  These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns_my({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns_my({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    assert safe_pawns_my({"a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"}) == 7
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")