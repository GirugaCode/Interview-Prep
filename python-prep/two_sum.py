"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

def twoSum(nums, target):
    """
    Runtime: O(n^2)
    """
    # Create an empty list
    sum_indexes = []
    
    for first_index in range(len(nums)):
        for second_index in range(first_index, len(nums)):
            sum = nums[first_index] + nums[second_index]
            if sum == target:
                print(sum)
                sum_indexes.append(first_index)
                sum_indexes.append(second_index)
                return sum_indexes

print(twoSum([2, 3, 11, 15, 1, 6], 9))