# coding: utf-8
"""
Подручные дроны Софии - это не какие-то тупые,
  бесчувственные железяки. Более того - они умеют дружить.
  На самом деле, они уже даже делают свою социальную сеть,
  только для дронов! София вытащила оттуда данные о всех
  связях между дронами и теперь хочет изучить эти
  взаимосвязи подробнее.
Дан массив прямых связей между дронами - кто с кем дружит.
  Каждая такая связь представлена, как строка с двумя именами
  разделеными дефисом. Для примера: "dr101-mr99" означает что
  dr101 и mr99 дружат между собой. Кроме этого даны два имени.
  Попробуйте определить, связаны ли они через других дронов,
  вне зависимости от глубины этих связей. Для примера: Если у
  двух дронов есть общий друг или или друзья, у которых есть
  общий друг и так далее.
Давайте рассмотрим примеры:
  scout2 и scout3 оба дружат с scout1, так что они связаны.
  super и scout2 связаны между собой через sscout, scout4 и scout1.
  Но вот dr101 и sscout никак не взаимосвязаны друг с другом.

*********************** TASK *******************************
Предусловие: len(network) ≤ 45
если "name1-name2" в network, то "name2-name1" не в network
3 ≤ len(drone_name) ≤ 6
first_name и second_name всегда в network.

Input: Три аргумента: информация о друзьях, как кортеж (tuple)
  строк (str); первое имя, как строка (str); второе имя,
  как строка (str).

Output: Связаны ли указанные дроны между собой, как
  булево значение (bool).
"""


def check_connection(network, first, second):
    friend_groups, fiends = [], {first, second}

    for friends in network:
        f1, f2 = friends.split("-")
        new_group, input_index = False, None
        for i, friend_group in enumerate(friend_groups):
            if f1 in friend_group and f2 not in friend_group:
                if input_index is not None:
                    friend_groups[input_index].add(f2)
                    input_index = None
                else:
                    friend_group.add(f2)
                    input_index = i

                new_group = False
            elif f1 not in friend_group and f2 in friend_group:
                if input_index is not None:
                    friend_groups[input_index].add(f1)
                    input_index = None
                else:
                    friend_group.add(f1)
                    input_index = i

                new_group = False
            elif f1 not in friend_group and f2 not in friend_group:
                new_group = True

        if new_group or not friend_groups:
            friend_groups.append({f1, f2})
    return any(friend_group.issuperset(fiends) for friend_group in friend_groups)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."

    # assert check_connection(
    #     ("nikola-robin", "batman-nwing", "mr99-batman", "mr99-robin",
    #      "dr101-out00", "out00-nwing",), "dr101", "mr99") == True
