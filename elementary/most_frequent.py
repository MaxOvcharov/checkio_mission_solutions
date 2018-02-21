# coding: utf-8
"""
You have a sequence of strings, and you’d like to
  determine the most frequently occurring string in the sequence.

*********************** TASK *******************************
Input: a list of strings.

Output: a string.
"""


# My solution faster
def most_frequent_my(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    # your code here
    return max(data.count(n) for n in data)


def most_frequent(data):
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
