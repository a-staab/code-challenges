import unittest

"""
Write a function that determines if there is a cycle in a linked list and, if
there is, removes the cycle.
"""


def remove_cycle(head):
    cycle_start = has_cycle(head)
    if cycle_start:
        current = head
        while current is not cycle_start:
            current = current.next
        current.next = None
    return head


def has_cycle(head):
        seen = set()
        current = head
        while current:
            if current.next in seen:
                return current
            seen.add(current)
            current = current.next
        return


class TestRemoveCycle(unittest.TestCase):

    def setUp(self):

        class Ll_node(object):
            def __init__(self, data, next=None):
                self.data = data
                self.next = next

        self.empty_ll = None
        self.ll_length_one = Ll_node(1)

        self.node_1 = Ll_node(1)
        self.node_2 = Ll_node(2)
        self.node_3 = Ll_node(3)
        self.node_1.next = self.node_2
        self.node_2.next = self.node_3
        self.node_3.next = self.node_2
        self.ll_with_cycle = self.node_1

        self.ll_without_cycle = Ll_node(1, Ll_node(2, Ll_node(3)))

    def get_length(self, head):
        current = head
        node_count = 0
        while current:
            node_count += 1
            current = current.next
        return node_count

    def test_has_cycle(self):
        # Check returns none for empty list
        self.assertIsNone(has_cycle(self.empty_ll))

        # Check returns none for single node
        self.assertIsNone(has_cycle(self.ll_length_one))

        # Check returns node where cycle begins for linked list with a cycle
        expected = self.node_3
        actual = has_cycle(self.ll_with_cycle)
        self.assertEqual(actual, expected)

        # Check returns none for linked list with > one node and no cycles
        self.assertIsNone(has_cycle(self.ll_without_cycle))

    def test_remove_cycle(self):

        # Check returns none for empty list
        self.assertIsNone(remove_cycle(self.empty_ll))

        # Check returns same node for linked list with single node
        expected = self.ll_length_one
        actual = remove_cycle(self.ll_length_one)
        self.assertEqual(actual, expected)

        # Check result of passing in a linked list with a cycle
        clipped_list = remove_cycle(self.ll_with_cycle)
        actual_length = self.get_length(clipped_list)
        expected_length = 3

        self.assertIsNone(has_cycle(clipped_list))
        self.assertIsNone(self.node_3.next)
        self.assertEqual(actual_length, expected_length)

        # Check result of passing in a linked list with > one node and no cycles
        expected_length = 3
        actual_length = self.get_length(remove_cycle(self.ll_without_cycle))
        self.assertEqual(actual_length, expected_length)


if __name__ == "__main__":
    unittest.main()
