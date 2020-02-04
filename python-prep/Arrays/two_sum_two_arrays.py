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
    # Sort both arrays
    # [0, 1, 4, 5, 8, 9, 12, 13]
    # [3, 4, 6, 14, 17]
    # Create a results array
    # Create a left pointer on array (a)
    # Create a right pointer on array (b)
    # Set a complement between array(a) + array(b)
    # If array (a) pointer and array(b) pointer is equal to the target
        # Append array(a) element into results
        # Append array(b) element into results
        # Return results here
    # If target is greater than complement
        # Move the right pointer -= 1
    # If target is less than complement
        # Move the left pointer += 1
    # Return None
    array_one.sort()
    array_two.sort()
    results = []
    left_pointer = 0
    right_pointer = len(array_two) - 1

    while left_pointer <= right_pointer:
        complement = array_one[left_pointer] + array_two[right_pointer]
        if complement == target:
            results.append(array_one[left_pointer])
            results.append(array_two[right_pointer])
            return results

        if complement > target:
            right_pointer -= 1

        if complement < target:
            left_pointer += 1

    return None


print(two_sum_two_arrays([9, 13, 1, 8, 12, 4, 0, 5], [3, 17, 4, 14, 6], 20))