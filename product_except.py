"""
You have a list of integers, and for each index you want to find the product of
every integer except the integer at that index. Write a function
get_products_of_all_ints_except_at_index() that takes a list of integers and
returns a list of the products. (Interview Cake)

>>> [1, 7, 3, 4]
[84, 12, 28, 21]

>>> [0, 1, 2, 3]
[6, 0, 0, 0]

"""


def get_products_of_all_ints_except_at_index(nums):

    if len(nums) < 2:
        raise IndexError("Array must contain two or more integers.")

    products_of_all_nums_except_at_index = []
    product_so_far = 1

    # First loop populates list with products of all numbers before
    # corresponding index
    for i in xrange(len(nums)):
        products_of_all_nums_except_at_index.append(product_so_far)
        product_so_far *= nums[i]

    product_so_far = 1
    j = -1

    # Then, we loop again, multiplying each number in the list by the product of
    # the numbers after its index, starting from the end of the list
    for i in xrange(len(nums)):
        products_of_all_nums_except_at_index[j] *= product_so_far
        product_so_far *= nums[j]
        j -= 1

    return products_of_all_nums_except_at_index
