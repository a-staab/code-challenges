"""
Given an array of integers, return the largest sum of k consecutive numbers in
the array.

>>> get_max_subarray([-1, 0, 10, 5], 2)
15

>>> get_max_subarray([-1, 0, 10, 5], 1)
10

>>> get_max_subarray([2], 1)
2

"""


def get_max_subarray(arr, k):

# Write error handling for invalid input: empty list, k < 1, or k > len(arr)

    i = 0
    j = k
    max_so_far = sum_subarray = sum(arr[i:j])

    while j < len(arr):

        sum_subarray += (arr[j] - arr[i])
        if sum_subarray > max_so_far:
            max_so_far = sum_subarray
        i += 1
        j += 1

    return max_so_far
