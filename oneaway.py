"""Given two strings, are they, at most, one edit away?

    >>> one_away("make", "make")
    True

    >>> one_away("make", "fake")
    True

    >>> one_away("task", "take")
    False

    >>> one_away("ask" ,"asks")
    True

    >>> one_away("asks", "ask")
    True

    >>> one_away("act", "tact")
    True

    >>> one_away("fat", "fact")
    True

    >>> one_away("yes", "no")
    False

    >>> one_away("dessert", "desert")
    True

    >>> one_away("paint", "painting")
    False

"""


def one_away(w1, w2):
    """Given two strings, are they, at most, one edit away?"""

    j = 0
    fail_count = 0
    if len(w2) > len(w1):
        w1, w2 = w2, w1
    if len(w1) - len(w2) > 1:
        return False
    for i in range(len(w1)):
        if w1[i] != w2[j]:
            fail_count += 1
            if fail_count > 1:
                return False
            if len(w1) == len(w2):
                j += 1
        else:
            j += 1
            if j >= len(w2):
                return True
    return True


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; NICE JOB! ***\n"
