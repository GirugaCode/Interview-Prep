"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

def single_number(nums):
    """
    Time Complexity: O(n + n) where we add all the nums in the set and get the other sum of the input
    Space Complexity: O(n) where we add each number in a set
    """
    return 2 * sum(set(nums)) - sum(nums)