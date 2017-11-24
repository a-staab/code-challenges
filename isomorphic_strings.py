"""
Isomorphic Strings (Leetcode)

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character but a character may map to itself.

Note:
You may assume both s and t have the same length.

>>> isIsomorphic("egg", "add")
True

>>> isIsomorphic("foo", "bar")
False

>>> isIsomorphic("paper", "title")
True

>>> isIsomorphic("ab", "aa")
False

"""


def isIsomorphic(s, t):

    def make_comparator(string):

        num_mappings = {}
        comparator = ''

        for i in range(len(string)):
            if not num_mappings.get(i):
                num_mappings[string[i]] = i

        for letter in string:
            comparator += str(num_mappings[letter])

        return comparator

    return make_comparator(s) == make_comparator(t)
