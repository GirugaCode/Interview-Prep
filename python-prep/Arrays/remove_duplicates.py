"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
"""

# Set a counter for the result length
# Iterate through the arrays 
# Evaluate each element in the array,
# Find a way to see if it has already occured and increment the count
# Keep in mind the array is sorted
# Return result length

def remove_duplicates(nums):
    nums[:] = list(set(nums)) # One Liner using dictionaries 
    return len(nums)

# print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))

def remove_duplicates_two(nums):
    current_index = 0

    while current_index < len(nums) - 1: # iterating through nums list till next-to-last element (curr_idx + 1 always checked)
        if nums[current_index] == nums[current_index + 1]: # if current and next element are the same
            del nums[current_index] # current element is deleted
            current_index -= 1 # to stay at the same place in list, we have to dicrease 1 (1 will be added in the next step)
        current_index += 1 # going further in the list
    return len(nums)

# print(remove_duplicates_two([-1,-1,0,0,0,1,1,1,6,8,8,8]))

def remove_duplicates_three(nums):
    curr = 0
    dup = curr + 1

    for _ in range(len(nums) - 1): 
        if nums[curr] == nums[dup]:
            nums.remove(nums[dup])
        else:
            curr += 1
            dup += 1

    return nums

print(remove_duplicates_three([]))
