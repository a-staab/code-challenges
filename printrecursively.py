"""Print items in the list, using recursion.

For example::

   >>> print_recursively([1, 2, 3, 4, 5])
   1
   2
   3
   4
   5

"""


def print_recursively(lst):
    """Print items in the list, using recursion."""

    if not lst:
        return
    else:
        print lst[0]
    print_recursively(lst[1:])

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n***TEST PASSED!***\n"
