"""
Given two arrays (a) and (b) of numbers and a target value (t), 
find a number from each array whose sum is closest to (t).

Restate: 
Given two arrays and a target value, output two numbers, one from each array,
that add up to the closest target value. 

Input: a=[9, 13, 1, 8, 12, 4, 0, 5], b=[3, 17, 4, 14, 6], t=20
Output: [13, 6] or [4, 17] or [5, 14]

Implemented a version to get exact number rather than closest
"""

def two_sum_two_arrays(array_one, array_two, target):
    
    # Sort both the arrays to perform a pointer method
    array_one.sort()
    array_two.sort()

    # Left pointer of the 0 index in array_one
    left_pointer = 0

    # Right pointer of the last index in array_two
    right_pointer = len(array_two) - 1

    # Initializes the first pair of values to find the closest to target
    best_pair = [array_one[left_pointer], array_two[right_pointer]]

    # Continue the while loop as long as their are numbers to traverse in each array
    while left_pointer <= len(array_one) - 1 and right_pointer >= 0:

        # Holds reference to the current pair of elements to add to target
        current_pair = [array_one[left_pointer], array_two[right_pointer]]

        # Switch case, compares if the best pair complement is greater than the current pair complement.
        if abs(sum(best_pair) - target) > abs(sum(current_pair) - target):
            best_pair = current_pair

        # Moves the right pointer
        if sum(current_pair) > target:
            right_pointer -= 1

        # Moves the left pointer
        if sum(current_pair) < target:
            left_pointer += 1
        
        # Break out of while-loop if the EXACT number is found
        else:
            break

    return best_pair


print(two_sum_two_arrays([9, 13, 1, 8, 12, 4, 0, 5], [3, 17, 4, 14, 6], 33))