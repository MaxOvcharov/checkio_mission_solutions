# coding: utf-8
"""
An anagram is a type of word play, the result of rearranging
the letters of a word or phrase to produce a new word or phrase,
using all the original letters exactly once. Two words are
anagrams to each other if we can get one from another by
rearranging the letters.

Anagrams are case-insensitive and
don't take account whitespaces. For example: "Gram Ring Mop"
and "Programming" are anagrams. But "Hello" and "Ole Oh" are not.

You are given two words or phrase. Try to verify are they anagrams or not.

*********************** TASK *******************************
Precondition: 0 < |first_word| < 100;
0 < |second_word| < 100;
Words contain only ASCII latin letters and whitespaces.

Input: Two arguments as strings.

Output: Are they anagrams or not as boolean (True or False)

"""


def verify_anagrams(first_word, second_word):
    f = list(first_word.lower())
    s = list(second_word.lower())
    word = f if len(f) > len(s) else s
    for i in word:
        if i == " ":
            continue
        elif i not in s or f.count(i) != s.count(i):
            return False
    return True


def verify_anagrams_best_solution(a, b):
    return sorted(a.lower().replace(' ', '')) == sorted(b.lower().replace(' ', ''))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams(u"a", u"z"), bool), "Boolean!"
    assert verify_anagrams(u"Programming", u"Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams(u"Hello", u"Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams(u"Kyoto", u"Tokyo") == True, "The global warming crisis of 3002"
