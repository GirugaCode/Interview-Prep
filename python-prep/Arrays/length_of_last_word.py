"""
Given a string s consists of upper/lower-case alphabets 
and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5

"""

def length_of_last_word(string):
    """
    Worst case: O(1), everything is in constant time
    """
    # Seperate the words in the string with the split function
    string_to_list = string.split(" ")
    # Retrives the last index which is the last element of the string
    last_index = len(string_to_list) - 1
    # Outpus the amount of characters in the list
    result = len(string_to_list[last_index])
    return result

print(length_of_last_word("Hello my name is jeff"))