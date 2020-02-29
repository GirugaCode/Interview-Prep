"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

def contains_duplicate(nums):
    """
    Time Complexity: O(nlog(n)) Sorting + O(n) Linear search -> O(nlog(n))
    Space Complexity: O(1) assuming we are using heap sort
    """
    # Sort the list of numbers
    nums = sorted(nums)

    # Iterate through all the indexes of the the array
    for index in range(len(nums) - 1):
        # Since its sorted we can linearly check if the next number is equal to it
        if nums[index] == nums[index + 1]:
            return True

    return False

def contains_duplicate_hash(nums):
    """
    Time Complexity: O(n) + O(1) where we are adding to the hash set (n) times but using constant lookup to find duplicate
    Space Complexity: O(n) where (n) is the number of times we are adding to the hash set
    """
    nums_hash = set()

    for num in nums:
        if num in nums_hash:
            return True

        nums_hash.add(num)      
    return False