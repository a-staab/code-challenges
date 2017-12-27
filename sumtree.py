"""
Check if a given binary tree is SumTree - GeeksforGeeks

Write a function that returns True if the given binary tree is a SumTree or
False if it is not. A SumTree is a binary tree where the value of each node is
equal to the sum of the nodes present in its left and right subtrees. An empty
tree is a SumTree, and the sum of an empty tree is considered to be 0. A leaf
node is also considered a SumTree.

Example:

        26
       /  \
      10   3
     /  \   \
    4    6   3

>>> leaf_1 = binaryTreeNode(4)
>>> leaf_2 = binaryTreeNode(6)
>>> leaf_3 = binaryTreeNode(3)
>>> left_child = binaryTreeNode(10, leaf_1, leaf_2)
>>> right_child = binaryTreeNode(3, leaf_3)
>>> root = binaryTreeNode(26, left_child, right_child)
>>> sumTree(root)
True

>>> sumTree(leaf_1)
True

>>> sumTree(left_child)
True

>>> subtree_a = binaryTreeNode(5)
>>> subtree_b = binaryTreeNode(5)
>>> root_a_b = binaryTreeNode(13, subtree_a, subtree_b)
>>> sumTree(root_a_b)
False

"""


class binaryTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def sumTree(node):
    if not node.left and not node.right:
        return True

    nodes_sum = get_sum(node.right) + get_sum(node.left)
    valid_subtrees = sumTree(node.right) and sumTree(node.left)

    return valid_subtrees and (nodes_sum == node.data)


def get_sum(node):
    """
    Given the root node of a binary tree, return the sum of the values for all
    nodes in the tree.
    """

    if not node:
        return 0
    return sum(node.data, get_sum(node.left), get_sum(node.right))
