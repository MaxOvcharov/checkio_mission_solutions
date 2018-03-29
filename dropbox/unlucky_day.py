# coding: utf-8
"""
Friday 13th or Black Friday is considered as unlucky day.
  Calculate how many unlucky days are in the given year.
Find the number of Friday 13th in the given year.
*********************** ЗАДАНИЕ *******************************
Precondition: 1000 < |year| < 3000

Input: Year as an integer.

Output: Number of Black Fridays in the year as an integer.
"""

from datetime import date, timedelta


def checkio_my(year):
    d = date(year, 1, 1)  # January 1st
    d += timedelta(days=4 - d.weekday())  # First Friday
    counter = 0
    while d.year == year or counter == 0:
        if d.day == 13:
            counter += 1

        d += timedelta(days=7)
    return counter


def checkio(year):
    friday13_count = 0
    months = range(1, 13)
    for month in months:
        if date(year, month, 13).weekday() == 4:
            friday13_count += 1
    return friday13_count


if __name__ == '__main__':
    #  These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(2015) == 3, "First - 2015"
    assert checkio(1986) == 1, "Second - 1986"
    assert checkio(1634) == 2, "Third - 1634"
