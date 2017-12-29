"""
Find the largest three elements in an array - "Geeks for Geeks"

Given an array with all distinct elements, find the largest three elements.
Expected time complexity is O(n), and extra space is O(1).

>>> get_top_three([10, 4, 3, 50, 23, 90])
90 50 23

>>> get_top_three([5, 22, 0, -1, 20, 6])
22 20 6

"""


def get_top_three(arr):

    first = second = third = float("-inf")

    for i in range(len(arr)):
        if arr[i] > first:
            third = second
            second = first
            first = arr[i]
        elif arr[i] > second:
            third = second
            second = arr[i]
        elif arr[i] > third:
            third = arr[i]

    print first, second, third
