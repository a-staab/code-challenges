"""Make a binary tree from an array.

Adapted from Cracking the Coding Interview, 6th Ed.

Given a list of sorted numbers, make a binary search tree.

Returns the root node of a new BST that is valid and balanced.

For example, for [1,2,3], this produces this tree:

   2
  / \
 1   3

    >>> tree3 = make_bst([1, 2, 3])
    >>> tree3.data
    2
    >>> tree3.left.data
    1
    >>> tree3.left.left is None
    True
    >>> tree3.left.right is None
    True
    >>> tree3.right.data
    3
    >>> tree3.right.left is None
    True
    >>> tree3.right.right is None
    True

For [1..7], this produces this perfectly-balanced tree:

        4
     /-----\
    2      6
   / \    / \
  1   3  5   7

    >>> tree7 = make_bst([1, 2, 3, 4, 5, 6, 7])
    >>> tree7.data
    4
    >>> tree7.left.data
    2
    >>> tree7.left.left.data
    1
    >>> tree7.left.right.data
    3
    >>> tree7.right.data
    6
    >>> tree7.right.left.data
    5
    >>> tree7.right.right.data
    7

When we can't make things perfectly balanced (like below), this
fills left-hand nodes before right-hand nodes.

Using a less-perfectly-even lists; e.g. [1..4]:

    3
   / \
  2   4
 /
1

    >>> tree4 = make_bst([1, 2, 3, 4])
    >>> tree4.data
    3
    >>> tree4.left.data
    2
    >>> tree4.left.left.data
    1
    >>> tree4.left.right is None
    True
    >>> tree4.right.data
    4
    >>> tree4.right.left is None
    True
    >>> tree4.right.right is None
    True

And [1..5]:

     3
    / \
   2   5
  /   /
 1   4

    >>> tree5 = make_bst([1, 2, 3, 4, 5])
    >>> tree5.data
    3
    >>> tree5.left.data
    2
    >>> tree5.left.left.data
    1
    >>> tree5.right.data
    5
    >>> tree5.right.left.data
    4

And [1..6]:

      4
   /-----\
  2       6
 / \     /
1   3   5

    >>> tree6 = make_bst([1, 2, 3, 4, 5, 6])
    >>> tree6.data
    4
    >>> tree6.left.data
    2
    >>> tree6.left.left.data
    1
    >>> tree6.left.right.data
    3
    >>> tree6.right.data
    6
    >>> tree6.right.left.data
    5

By Joel Burton <joel@hackbrightacademy.com>
"""


class BinaryNode(object):
    """Node in a binary tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def make_bst(nums):
    """Given a list of sorted numbers, make a binary search tree.

    Returns the root node of a new BST that is valid and balanced.
    """

    if not nums:
        return None

    # Halve the lists to find root node

    # Because of offset from zero-indexing, halves will be equal or left half
    # will have the odd node, as it should

    root_index = len(nums) / 2

    node = BinaryNode(nums[root_index])

    # Recurse on left and right lists, in order

    node.left = make_bst(nums[0:root_index])
    node.right = make_bst(nums[(root_index + 1):len(nums)])

    return node

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n**** ALL TESTS PASSED. YOU'RE A TREE-MASTER!\n"
