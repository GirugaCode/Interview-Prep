"""
Given a string of digits 2 to 9 a user has pressed on a T9 “old school” telephone keypad, 
return a list of all letter combinations they could have been trying to type on the keypad.

Example execution 1:  t9_letters("23")  ⇒  
                      ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])

Example execution 2:  t9_letters("4663")  ⇒  
                      ["gmmd", …, "gone", …, "good", …, "home", …, "hood", …, "ioof"]
"""

def t9LetterCombination(digits):
    """
    Runtime: O(n(4^n)) where 4^n is the maxiumum number of characters in each number and 
                       n is the possible calls to make + O(n) to copy each string over
    Space Complexity: O(4^n) where 4 is the maximum number of characters in each number.
                             n is the number of possible depth of recurssion calls.
    """
    res = [] # Holds the results
    # Checks for empty input
    if len(digits) == 0:
        return None
    # Recursivly calls the helper func until all digits are complete
    t9Helper(digits, '', res)
    return res

def t9Helper(digits, curr_str, res):
    if len(digits) == 0: # Base Case to add string to result
        # Adds the completed string to results
        res.append(curr_str)
        return # Continues after its own recursive call
    
    # Gets all characters for each digit starting at the first one
    possible_chars = digitToLetters(digits[0])

    # Iterate through all characters
    for char in possible_chars:
        curr_str += char # Add the character to current string
        t9Helper(digits[1:], curr_str, res) # Recursive call w/ slicing of first digit
        curr_str = curr_str[:-1] # Slice the last character to find other combinations


def digitToLetters(digit):
    mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    return mapping[digit]


print(t9LetterCombination("23"))