# coding: utf-8
"""
You have a sequence of strings, and you’d like to
  determine the most frequently occurring string in the sequence.

*********************** TASK *******************************
Input: a list of strings.

Output: a string.
"""


def most_frequent_my(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    # your code here
    return max((data.count(n), n) for n in data)[1]


def most_frequent_best_solution(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    # your code here
    return max(data, key=lambda n: data.count(n))


if __name__ == '__main__':
    #  These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_my([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent_my(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
