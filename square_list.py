# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 05/15/2024
# Description: Squares the elements of a list and replaces each value.
def square_list(nums):
    """Square the elements of a list."""
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]