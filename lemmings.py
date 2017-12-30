"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3
"""


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""

    # Assuming cafes is sorted.

    max_so_far = 0

    # Get max distance from outermost holes to outermost cafes
    if cafes[0] > max_so_far:
        max_so_far = cafes[0]
    if ((num_holes - 1) - cafes[-1]) > max_so_far:
        max_so_far = ((num_holes - 1) - cafes[-1])

    # Compare to maximum distance from hole that is between two cafes
    for i in range(len(cafes) - 1):
        if (cafes[(i + 1)] - cafes[i])/2 > max_so_far:
            max_so_far = (cafes[(i + 1)] - cafes[i])/2

    return max_so_far

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; GREAT JOB!\n"
