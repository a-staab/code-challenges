"""Does a string have balanced parentheses?

For example::

   >>> has_balanced_parens("()")
   True

   >>> has_balanced_parens("(Oh Noes!)(")
   False

   >>> has_balanced_parens("((There's a bonus open paren here.)")
   False

   >>> has_balanced_parens(")")
   False

   >>> has_balanced_parens("(")
   False

   >>> has_balanced_parens("(This has (too many closes.) ) )")
   False

If you receive a string with no parentheses, consider it balanced::

   >>> has_balanced_parens("Hey...there are no parens here!")
   True
"""

# Solution 1

# def has_balanced_parens(phrase):
#     """Does a string have balanced parentheses?"""

#     stack = []

#     for char in phrase:
#         if char == ')':
#             if stack:
#                 stack.pop()
#             else:
#                 return False
#         elif char == '(':
#             stack.append('(')

#     return not stack

# Solution 2 - Similar logic, optimal space complexity


def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?"""

    open_parens = 0

    for char in phrase:
        if char == ')':
            if open_parens:
                open_parens -= 1
            else:
                return False
        elif char == '(':
            open_parens += 1

    return open_parens == 0


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY PARENS!\n"
