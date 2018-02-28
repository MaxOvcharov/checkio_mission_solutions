# coding: utf-8
"""
Дана таблица всех доступных продуктов на складе.
Данные представленны в виде списка диктов (a list of dicts)
Ваша миссия тут - это найти ТОП самых дорогих товаров.
Количество товаров, которые мы ищем, будет переданно в первом
  аргументе, а сами данные по товарам будут переданны вторым аргументом.
*********************** TASK *******************************
Input: Число и массив диктов (int and list of dicts).
  Каждый дикт имеет 2 ключа "name" и "price".

Output: Такой же как и второй аргумент.
"""


# best solution
def bigger_price_my(limit, data):
    """
        TOP most expensive goods
    """
    return sorted(data, key=lambda x: x["price"], reverse=True)[:limit]


if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price_my(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price_my(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price_my(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')