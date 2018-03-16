# coding: utf-8
"""
В задании "Как найти друзей" ("How to find friends") ,
  было бы удобно работать, используя специальную структуру данных.
В этом задании мы разработаем структуру данных, которую будем
  применять для хранения и обработки социальной сети.
Класс "Friends" должен содержать данные о людях (их имена) и о
  связях между ними. Имена представлены в виде текстовых строк,
  чувствительных к регистру. Связи не имеют направлений, то есть,
  если существует связь "sofia" с "nikola", это справедливо и
  в обратную сторону.

*********************** TASK *******************************
Предусловие: Все данные корректны.

Input: Операторы и выражения с классом Friends.

Output: Поведение объекта, как описано выше.
"""


class FriendsMySolution:
    """
    Возвращает новый объект, экземпляр класса Friends.
      Параметр "connections" имеет тип "итерируемый объект", содержащий
      множества (set) с двумя элементами в каждом. Каждая связь содержит
      два имени в виде текстовых строк. Связи могут повторяться в параметре
      инициализации, но в объекте хранятся только уникальные пары. Каждая
      связь имеет только два состояния - присутствует или не присутствует.
    >>> Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"})
    >>> Friends([{"1", "2"}, {"3", "1"}])
    """
    def __init__(self, connections):
        self.connections = list(connections)

    def add(self, connection):
        """
        Добавляет связь в объект. Параметр "connection" является множеством (set) из
          двух имен (строк). Возвращает True, если заданная связь новая и не присутствует
          в объекте. Возвращает False, если заданная связь уже существует в объекте.
        >>> f = Friends([{"1", "2"}, {"3", "1"}])
        >>> f.add({"1", "3"})
        False
        >>> f.add({"4", "5"})
        True
        """
        add_res = False
        if connection not in self.connections:
            self.connections.append(connection)
            add_res = True

        return add_res

    def remove(self, connection):
        """
        Удаляет связь из объекта. Параметр "connection" является множеством (set) из
          двух имен (строк). Возвращает True, если заданная связь существует в объекте.
          Возвращает False, если заданная связь не присутствует в объекте.
        >>> f = Friends([{"1", "2"}, {"3", "1"}])
        >>> f.remove({"1", "3"})
        True
        >>> f.remove({"4", "5"})
        False
        """
        remove_res = False
        if connection in self.connections:
            self.connections.remove(connection)
            remove_res = True

        return remove_res

    def names(self):
        """
        Возвращает множество (set) имён. Множество содержит имена,
          которые имеют хотя бы одну связь.
        >>> f = Friends(({"a", "b"}, {"b", "c"}, {"c", "d"})
        >>> f.names()
        {"a", "b", "c", "d"}
        >>> f.remove({"d", "c"})
        True
        >>> f.names()
        {"a", "b", "c"}
        """
        con_len = len(self.connections)
        return {name for i in range(con_len) for name in self.connections[i]}

    def connected(self, name):
        """
        Возвращает множество (set) имён, которые связаны с именем,
          заданным параметром "name". Если "name" не присутствует в
          объекте, возвращается пустое множество (set).
        >>> f = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"})
        >>> f.connected("a")
        {"b", "c"}
        >>> f.connected("d")
        set()
        >>> f.remove({"c", "a"})
        True
        >>> f.connected("c")
        set()
        """
        x = set()
        for names in self.connections:
            if name in names:
                for i in names:
                    if i not in x and i != name:
                        x.add(i)
        return x


# best solution
class Friends(set):
    def __init__(self, pairs=set()):
        super().__init__(map(frozenset, pairs))

    def add(self, pair):
        if pair in self: return False
        super().add(frozenset(pair))
        return True

    def remove(self, pair):
        if pair not in self: return False
        super().remove(pair)
        return True

    def names(self):
        return set().union(*self)

    def connected(self, name):
        return Friends(filter({name}.issubset, self)).names() - {name}


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"