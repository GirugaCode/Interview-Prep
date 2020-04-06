"""
Given a string, find the length of the longest substring without repeating characters.
​
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
​
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

max = 4 
Input: "abcadcdb"
              ^  
            ^    
Output: 3

Assumptions: 
- All lower case
- Guarenteed given a string


create a max variable to keep track
create a start pointer starting at the first character

iterate through the string
    check if the next index is in our window
        update the max to the length of window
        as long as the next index is in window
            increment our start pointer
return our max


max = 4 
Input: "abcabcbb"
           ^i  
        ^s    
Output: 3

Feedback:
Notice code repititos and minimize it
keep conventions more in mind

"""
def longest_substring(s):
    max_v = 0
    start_pointer = 0

    for i in range(len(s)):
        if i == len(s) - 1:
            break
        if s[i+1] in s[start_pointer:i+1]:
            max_v = max(max_v, len(s[start_pointer:i+1]))
            while s[i+1] in s[start_pointer:i+1]:
                start_pointer += 1
    return max_v

def longest_substring_two(s):
    max_v = 0
    start_pointer = 0

    for i in range(len(s) - 1):
        next_char = s[i+1]
        current_window = s[start_pointer:i+1]
        max_v = max(max_v, len(current_window))
        while next_char in current_window:
            start_pointer += 1
            current_window = s[start_pointer:i+1]

    return max_v
"""

left = 0
right = 0
longest = 3
dict = {k,e,w}
"pwwkew"
    ^l 
       ^r
"""
def longest_substring_three(string):
    max_v = 0
    left = 0
    right = 0
    string_dict = set()

    while left < len(string) and right < len(string):
        if string[right] not in string_dict:
            string_dict.add(string[right])
            right += 1
            max_v = max(max_v, len(string_dict))
        else:
            string_dict.remove(string[left])
            left += 1
    return max_v



# print(longest_substring("abcadcdb"))
# print(longest_substring("bbbbb"))
# print(longest_substring("abcabcbb"))

print(longest_substring_three("abcadcdb"))
print(longest_substring_three("bbbbb"))
print(longest_substring_three("pwwkew"))