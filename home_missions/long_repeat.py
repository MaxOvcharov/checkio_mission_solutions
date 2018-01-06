"""
This mission is the first one of the series.

Here you should find the length of the longest substring
that consists of the same letter. For example,
line "aaabbcaaaa" contains four substrings with the
same letters "aaa", "bb","c" and "aaaa".

The last substring is the longest one which makes it an answer.

*********************** TASK *******************************
Input: String.

Output: Int.
"""
from itertools import groupby


def long_repeat_my(line):
    """
        length the longest substring that consists of the same char
    """
    previous, current, tmp_set = 0, 0, set()
    for char in line:
        if char in tmp_set:
            current += 1
        elif len(tmp_set) == 0:
            tmp_set.add(char)
            current = 1
        else:
            tmp_set.clear()
            previous = previous if previous > current else current
            current = 1
            tmp_set.add(char)

    return previous if previous > current else current


def long_repeat_best_solution(line):
    """
        length the longest substring that consists of the same char
    """
    return max((sum(1 for _ in g) for k, g in groupby(line)), default=0)


if __name__ == '__main__':
    #  These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat_my('sdsffffse') == 4, "First"
    assert long_repeat_my('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat_my('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
