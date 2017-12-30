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

    counts = {}
    mode = set()

    for num in nums:
        counts[num] = counts.setdefault(num, 0) + 1

    max_count = max(counts.values())

    for num, count in counts.items():
        if count == max_count:
            mode.add(num)

    return mode


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. HOORAY!\n"
