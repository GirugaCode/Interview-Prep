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
    
    # Iterate through the nums to get the first_index
    for first_index in range(len(nums)):
        # Iterate through with the first_index to get second_index
        for second_index in range(first_index, len(nums)):
            # Gather the sum of all possible elements in list
            sum = nums[first_index] + nums[second_index]
            # Once the sum is the target number we want add it to the empty list
            if sum == target:
                sum_indexes.append(first_index)
                sum_indexes.append(second_index)
                return sum_indexes

# print(twoSum([2, 7, 11, 13, 15], 9))

def twoSumDictionary(nums, target):
    """
    Runtime: O(n)
    """
    
    dict = {}

    # Interates through nums and compares the complement between the target and elements
    for index, element in enumerate(nums):
        complement = target - element
        if complement in dict: 
            complement_index = dict[complement]         
            return [complement_index, index]
        dict[element] = index
    return None

# print(twoSumDictionary([2, 7, 11, 13, 15], 9))

def twoSumPointers(array, target):
    """
    Runtime: O(n) where n is the number of elements in the array to move through
    """
    left_index = 0
    right_index = len(array) - 1

    results = []

    while left_index < right_index:
        complement = array[left_index] + array[right_index]

        if complement == target:
            results.append(array[left_index])
            results.append(array[right_index]) 
            return results

        if complement > target:
            right_index -= 1
        
        if complement < target:
            left_index += 1

    return None

print(twoSumPointers([2, 7, 11, 13, 15], 9))