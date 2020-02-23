"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Psuedocode:

Go over every number in the array
Find the first number of the sequence
Check if every number in that array has a sequence of that number 
Calulate the the length from there
"""
def longest_consecutive(arr):
    # Put all items into a Set
    setNums = set(arr)

    # Keeps track of the longest number
    longest = 0

    for num in setNums:
        # Finds the starting point of the sequence
        if num - 1 not in setNums:
            curr_longest = 1 # Tracks the longest number
            counter = num + 1 # Keeps a check if the sequential number
        while counter in setNums: # As long as the sequential number is in the set
            curr_longest += 1 # Iterate
            counter += 1 # Iterate
        longest = max(longest, curr_longest) # Longest sequence between 0 and x num
    return longest
    
print(longest_consecutive([0, -1]))