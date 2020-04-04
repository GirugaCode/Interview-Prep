"""
Given an array nums, write a function to move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

Input: [-5, 3, 2, 1, -10, 0, 0]
num      ^
zer      ^
Output: [-5, 3, 2, 1, -10, 0, 0]

Brainstorm:
Linear scan through the array with two pointers
    If you see a 0 
    Swap it with the zero pointer and number pointer
    increment the zero pointer

"""

def moveZeros(nums):
    zero_pointer = 0
    for num_pointer in range(len(nums)):
        if nums[num_pointer] != 0:
            nums[num_pointer], nums[zero_pointer] = nums[zero_pointer], nums[num_pointer]
            zero_pointer += 1