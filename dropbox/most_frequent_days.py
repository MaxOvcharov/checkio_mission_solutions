# coding: utf-8
"""
What is your favourite day of the week? Check if it's
  the most frequent day of the week in the year.
You are given a year as integer (e. g. 2001). You should
  return the most frequent day(s) of the week in that year.
  The result has to be a list of days sorted by the order of
  days in week (e. g. ['Monday', 'Tuesday']). Week starts
  with Monday.
*********************** ЗАДАНИЕ *******************************
Preconditions: Year is between 1 and 9999. Week starts
  with Monday.

Input: Year as an int.

Output: The list of most frequent days sorted by the
  order of days in week (from Monday to Sunday).
"""
from datetime import datetime, date, timedelta
import calendar
from collections import Counter


def most_frequent_days_my(year):
    """
        List of most frequent days of the week in the given year
    """
    start_date = date(year, 1, 1)
    end_date = date(year, 12, 31)
    all_days = (start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1))
    weekdays = (calendar.day_name[d.weekday()] for d in all_days)
    weekdays_sorted = Counter(weekdays).most_common(7)
    highest = weekdays_sorted[0][1]
    weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    max_weekdays = (weekday for weekday, count in weekdays_sorted if count == highest)

    return sorted(max_weekdays, key=weekdays.index)


DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


# best solution
def most_frequent_days(year):
    """
        List of most frequent days of the week in the given year
    """
    temp = list()
    n = 1
    tmp = datetime(year, 1, n).timetuple()[6]

    while tmp != 0:
        temp.append(tmp)
        n += 1
        tmp = datetime(year, 1, n).timetuple()[6]

    n = 31
    tmp = datetime(year, 12, n).timetuple()[6]

    while tmp != 6:
        # if tmp not in temp:
        temp.append(tmp)
        n -= 1
        tmp = datetime(year, 12, n).timetuple()[6]

    if len(temp) > 7:
        temp = list(set([x for x in temp if temp.count(x) == 2]))

    return [DAYS[x] for x in sorted(temp)]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_days(2399) == ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"
