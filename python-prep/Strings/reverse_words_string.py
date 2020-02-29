"""
Given an input string, reverse the string word by word.

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 
Note:
A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.

Psuedocode:
Use an empty string to hold each character through the iteration
Create an empty array to hold the soon-to-be result

Going through the string
    if the character is empty
        and validate that the current string is not empty
            add the string into the array
            reset the current string
    if the current string is empty 
        set it to the character
    
    or add the character to the current string

The get the result and reverse it 
as well as strip the array

Time Complexity: O(3n) -> O(n) 3n being each time we go through each character, joining each word into a list, and reversing a list
Space Complexity: O(n) -> from using an new array to hold all our values

"""
def reverse_words(s):
    s = s + ' '
    curr_char = ' '
    result = []
    
    for char in s: 
        if char == ' ':
            if curr_char != ' ':
                result.append(curr_char)
                curr_char = ' '
        else:
            if curr_char == ' ':
                curr_char = char
            else:
                curr_char = curr_char + char
    
    return ' '.join(result[::-1])

print(reverse_words("the    sky is   babab   wwww     blue      "))
