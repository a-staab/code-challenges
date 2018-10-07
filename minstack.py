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
        pass

    def test_pop(self):
        pass

    def test_peek(self):
        pass

    def test_get_min(self):
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMinStack)
    unittest.TextTestRunner(verbosity=2).run(suite)
