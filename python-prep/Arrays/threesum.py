"""
Given an array nums of n integers, are there elements a, b, c 
in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.


Note:
The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Psuedocode:
Create a results array
Sort the given numbers array = [-4, -1, 0, 1 , 2]

Iterate through every index of the array
    Skip over the starting index
    Have two other pointers at the next and last element

    As long as the left pointer is less than the right pointer
        Calculate the sum of all three elements

        If the sum is less than 0
            increase the left pointer
        or when the sum is greater than 0
            increase the right pointer
        otherwise
            append the three numbers in the result array

            As long as left is less than right and
            the left element is equal to the one before
                skip left
            As long as left is less than right and
            the right element is equal to the one after
                skip right
            
            increase left pointer
            increase right pointer

return the result
"""
def threeSum(nums):
    result = []
    nums = nums.sort()

    for i in range(len(nums) - 1):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1

        while left < right:
            sum_total = nums[i] + nums[left] + nums[right]

            if sum_total < 0:
                left += 1
            elif sum_total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
                left += 1
                right -= 1

    return result


print(threeSum([-1,0,1,2,-1,-4]))

