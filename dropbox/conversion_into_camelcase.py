# coding: utf-8
"""
Ваша задача - написать функцию, которая преобразовывает
  текст (название другой функции) из формата, принятого
  в Python (my_function_name) в CamelCase, принятый в
  JavaScript (MyFunctionName), где первая буква каждого
  слова - большая/заглавная.
*********************** ЗАДАНИЕ *******************************
Предусловия:
0 < len(string) <= 100
Во входящих данных не будет чисел или пустых строк

Ввод: Название функции как строка

Вывод: То же самое название, но в CamelCase
"""


def to_camel_case(name):
    return "".join(word.capitalize() for word in name.split('_'))


if __name__ == '__main__':
    print("Example:")
    print(to_camel_case('name'))

    #  These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
