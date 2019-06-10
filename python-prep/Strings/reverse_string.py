"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Communication Steps:

Rephrase Question:
Okay, so I am given a list of strings and I have to reverse without modifying space complexity
by moving it to another array for example. All characters in the list will be ascii characters.

Questions:
Would there be a possible for the array of strings to be empty?
Does the output have to be case-sensitive to the input?
Since I have to keep O(1) time in memory, will I have to account that rule for
space complexity as well?

Assumptions:
I can safely assume that I can not use built-in functions.
I should account for empty strings in the list.
The output should clearly reflect the case-sensitivity.
I need to keep O(1) in time in memory but I should not worry about
the space complexity.

Example 1:
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]



"""





def reverseString(array):

    """
    :type s: List[str]
    :rtype: void Do not return anything, modify s in-place instead.
    """
    first_index = 0
    last_index = len(array) - 1
    while first_index <= last_index:
        array[first_index], array[last_index] = array[last_index], array[first_index]
        first_index += 1
        last_index -= 1

    return array

print(reverseString(["h","e","l","l","o"]))