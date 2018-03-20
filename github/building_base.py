# coding: utf-8
"""
Сингулярность всё-таки наступила, и мы обязаны построить
  идеальный робо-город для наших повелителей. В этом
  сияющем робополисе все здания будут прямоугольными, а
  все улицы идти в направлениях "север-юг" и "восток-запад",
  образуя восхитительную решётку. Прежде чем начать
  строительство, мы должны создать класс, представляющий
  совершенное здание.
Так как все здания в городе прямоугольные, и их стены параллельны
  улицам, мы можем определить любое здание, используя только пару
  координат юго-западного угла, длину стен, идущих с запада на
  восток, длину стен, идущих с севера на юг, а также высоту здания.
  Эти значения выражены как положительные числа в обычных единицах
  измерения. Начало координат расположено в юго-западном углу города,
  следовательно, северные стороны зданий имеют значения координат
  больше, чем южные. Для решения этой задачи нам потребуется
  разработать несколько методов. Описание класса смотрите далее.

*********************** ЗАДАНИЕ *******************************

Предусловия: Предусловие: Все данные корректны.

Ввод: операторы и выражения, использующие класс Building.

Вывод: поведение экземпляра как описано выше.
"""
from itertools import product


class BuildingMy:
    """
    Возвращает новый экземпляр класса Building (класса здания)
      с юго-западным углом расположенным в точке с
      координатами [south, west], длиной стен, идущих по направлению
      "восток-запад" - width_WE, длиной стен, идущих по направлению
      "север-юг" - width_NS, и высотой height. Параметр height
      является положительным числом со значением по умолчанию равным 10.
    >>> Building(10, 10, 1, 2, 2)
    Building(10, 10, 1, 2, 2)
    >>> Building(0, 0, 10.5, 2.546)
    Building(0, 0, 10.5, 2.546, 10)
    """
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height

    # method that return coordinates
    def corners(self):
        """
        Возвращает словарь (dictionary) с координатами углов здания.
          Словарь имеет следующие ключи: "north-west", "north-east",
          "south-west", "south-east". Значениями являются списки
          (list) или кортежи (tuples) с двумя числовыми значениями.
        >>> Building(1, 2, 2, 2).corners()
        {"north-west": [3, 2], "north-east": [3, 4], "so
        """
        d = {'north-west': [self.south + self.width_NS, self.west],
             'north-east': [self.south + self.width_NS, self.west + self.width_WE],
             'south-west': [self.south, self.west],
             'south-east': [self.south, self.west + self.width_WE]}
        return d

    # method that return area of building
    def area(self):
        """
        Возвращает площадь основания здания.
        >>> Building(1, 2.5, 4.2, 1.25).area()
        5.25
        """
        return self.width_NS * self.width_WE

    # method that return volume of building
    def volume(self):
        """
        Возвращает объем здания.
        >>> Building(1, 2.5, 4.2, 1.25, 101).volume()
        530.25
        """
        return self.width_NS * self.width_WE * self.height

    # method that return string
    def __str__(self):
        """
        Это представление объекта Building в виде текстовой строки.
          Метод используется в функциях print или str (преобразование
          в строку). Возвращает строку следующего вида:
          "Building({south}, {west}, {width_we}, {width_ns}, {height})"
        >>> str(Building(0, 0, 10.5, 2.546))
        "Building(0, 0, 10.5, 2.546, 10)"
        """
        return "Building(%s, %s, %s, %s, %s)" % (self.south, self.west, self.width_WE,
                                                 self.width_NS, self.height)


# best solution
class Building:
    def __init__(self, south, west, width, depth, height=10):
        self.south, self.west = south, west
        self.width, self.depth, self.height = width, depth, height
        self.north, self.east = south + depth, west + width

    def corners(self):
        pairs = product(('south', 'north'), ('west', 'east'))
        return {'-'.join(p): [getattr(self, d) for d in p] for p in pairs}

    def area(self):
        return self.width * self.depth

    def volume(self):
        return self.width * self.depth * self.height

    def __repr__(self):
        txt = 'Building({0.south}, {0.west}, {0.width}, {0.depth}, {0.height})'
        return txt.format(self)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())


    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"

