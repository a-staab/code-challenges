"""Find the most frequent num(s) in nums.

Return the set of nums that are the mode::

    >>> find_mode([1]) == {1}
    True

    >>> find_mode([1, 2, 2, 2]) == {2}
    True

If there is a tie, return all::

    >>> find_mode([1, 1, 2, 2]) == {1, 2}
    True
"""


def find_mode(nums):
    """Find the most frequent num(s) in nums."""

    frequencies = {}
    for num in nums:
        frequencies[num] = frequencies.get(num, 0) + 1

    mode = set([])
    for num, frequency in frequencies.items():
        if frequency == max(frequencies.values()):
            mode.add(num)

    return mode

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. HOORAY!\n"
