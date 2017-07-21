"""Given list of chars, return a new copy, but with vowels replaced by '*'.

For example::

    >>> replace_vowels(['h', 'i'])
    ['h', '*']

    >>> replace_vowels([])
    []

    >>> replace_vowels(['o', 'o', 'o'])
    ['*', '*', '*']

    >>> replace_vowels(['z', 'z', 'z'])
    ['z', 'z', 'z']

Make sure to handle uppercase::

    >>> replace_vowels(["A", "b"])
    ['*', 'b']

Do not consider `y` a vowel::

    >>> replace_vowels(["y", "a", "y"])
    ['y', '*', 'y']

This should return a new list, not mutate the original::

    >>> a = ['h', 'i']
    >>> out = replace_vowels(a)

"""


def replace_vowels(chars):
    """Given list of chars, return a new copy, but with vowels replaced by '*'."""

    no_vowels = []
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    for char in chars:
        if char in vowels:
            no_vowels.append("*")
        elif char.lower() in vowels:
            no_vowels.append("*")
        else:
            no_vowels.append(char)
    return no_vowels


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"
