"""Given already-sorted lists, `a` and `b`, return sorted list of both.

You may not use sorted() or .sort().

Check edge cases of empty lists:

    >>> sort_ab([], [])
    []

    >>> sort_ab([1, 2, 3], [])
    [1, 2, 3]

    >>> sort_ab([], [1, 2, 3])
    [1, 2, 3]

Check:

    >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
    [1, 2, 3, 5, 6, 7, 8, 10]

    >>> sort_ab([1, 3, 5], [1, 7, 8])
    [1, 3, 5, 7, 8]

    >>> sort_ab([1, 2, 3], [1, 2, 10])
    [1, 2, 3, 10]

"""


def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    """

    new_list = []
    i = 0
    j = 0

    if len(b) > len(a):
        a, b = b, a

    if b == []:
        new_list = a
        return new_list

    while i < len(a):
        if a[i] < b[j]:
            new_list.append(a[i])
            i += 1
        elif a[i] == b[j]:
            new_list.append(a[i])
            b.pop(j)
            i += 1
        else:
            new_list.append(b[j])
            b.pop(j)
    if b != []:
        new_list.extend(b)

    return new_list


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE A MERGE CHAMPION!!\n"
