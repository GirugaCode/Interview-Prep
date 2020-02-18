"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, 
and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Example 3:
Input: [9,9,9,9]
Output: [1,0,0,0,0]
Explanation: The array represents the integer 9999.

Rephase: Given an array of non-negitive integers, add one to the integers such as an entire integer
will be returned back as an array of ints

Assumptions: 
- I will be able to use built in functions in python
- The array will be able to expand to larger values

Pseudocode:

Create a var to join the ints in the array

Add one to the int 

Split that int into an array

Return the result

"""

def plus_one_array(array):

    # Interpulates the given array into a string
    joinedArray = ''.join(str(i) for i in array)

    # Makes the string into an int and adds one to it
    int_result = int(joinedArray) + 1

    # Create the result that iterates the int as a string and stores it in an array
    result = [int(i) for i in str(int_result)]

    # Return result
    return result

print(plus_one_array([9,9,9,9]))
