"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

# def reverseString(string):
#     index = 0
#     string_size = len(string) -1

#     while index < string_size:
#         string[index], string[string] = string[string_size], string[index]
#         index += 1
#         string_size -= 1
#     return string





def reverseString(s):
    """
    :type s: List[str]
    :rtype: void Do not return anything, modify s in-place instead.
    """
    index = 0
    last_index = len(s) - 1
    while index <= last_index:
        s[index], s[last_index] = s[last_index], s[index]
        index += 1
        last_index -= 1

print(reverseString(["h","e","l","l","o"]))