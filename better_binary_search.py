
"""
Given a sorted array of integers, return the index of a target element in the
array. If the element is not in the array, return -1. Assume there are no
duplicates in the array.

>>> get_index([0, 20, 34, 60, 79, 80], 31)
-1

>>> get_index([0, 20, 34, 60, 79, 80], 100)
-1

>>> get_index([20, 34, 60, 79, 80], 0)
-1

>>> get_index([0, 20, 34, 60, 79, 80], 0)
0

>>> get_index([0, 20, 34, 60, 79, 80], 20)
1

>>> get_index([0, 20, 34, 60, 79, 80], 34)
2

>>> get_index([0, 20, 34, 60, 79, 80], 60)
3

>>> get_index([0, 20, 34, 60, 79, 80], 79)
4

>>> get_index([0, 20, 34, 60, 79, 80], 80)
5

"""


def get_index(arr, target):

    lower = 0
    upper = len(arr) - 1
    result = -1

    while lower <= upper and result == -1:
        midpoint = lower + (upper - lower)/2

        if target == arr[midpoint]:
            result = midpoint

        elif target < arr[midpoint]:
            upper = midpoint - 1

        elif target > arr[midpoint]:
            lower = midpoint + 1

    return result
