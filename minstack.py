"""
Design a stack that supports push, pop, peek, and retrieving the minimum element
in constant time.
"""


class MinStack(object):

    def __init__(self):
        self.nums = []
        self.minimum = []

    def __repr__(self):
        return "MinStack with elements %s and min = %s" % (
            self.nums, self.get_min())

    def push(self, num):
        self.nums.append(num)
        if not self.minimum or num <= self.get_min():
            self.minimum.append(num)

    def pop(self):
        if self.nums:
            to_return = self.nums.pop()
            if self.get_min() == to_return:
                self.minimum.pop()
            return to_return

    def peek(self):
        if self.nums:
            return self.nums[-1]

    def get_min(self):
        if self.minimum:
            return self.minimum[-1]


import unittest


class TestMinStack(unittest.TestCase):
    def setUp(self):
        self.minstack = MinStack()

    def tearDown(self):
        self.minstack = None

    def test_init(self):
        self.assertIsNotNone(MinStack())
        with self.assertRaises(TypeError):
            MinStack("an_argument")

    def test_repr(self):
        actual = str(self.minstack)
        expected = "MinStack with elements [] and min = None"
        self.assertEqual(actual, expected)

    def test_push(self):

        # Tests when stack was empty previously
        empty_stack = MinStack()
        empty_stack.push(1)

        expected_min = 1
        actual_min = empty_stack.get_min()
        self.assertEqual(actual_min, expected_min)

        expected_top = 1
        actual_top = empty_stack.peek()
        self.assertEqual(actual_top, expected_top)

        # Tests when new element is less than previous minimum
        self.minstack.push(5)
        self.minstack.push(2)

        actual_min = self.minstack.get_min()
        expected_min = 2
        self.assertEqual(actual_min, expected_min)

        actual_top = self.minstack.peek()
        expected_top = 2
        self.assertEqual(actual_top, expected_top)

        # Tests when new elment is equal to previous minimum
        

        # # Tests when new elment is greater than previous minimum
        # new_stack2 = MinStack().push(1).push(2)
        # actual_min = new_stack2.mininum[-1]
        # expected_min = 1
        # actual_top = new_stack2.nums[-1]
        # expected_top = 2
        # self.assertEqual(actual_min, expected_min)
        # self.assertEqual(actual_top, expected_top)

    def test_pop(self):
        pass

    def test_peek(self):
        pass

    def test_get_min(self):
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMinStack)
    unittest.TextTestRunner(verbosity=2).run(suite)
