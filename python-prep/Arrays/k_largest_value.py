"""
Given an array (a) of (n) numbers and a count (k) find the (k) largest values in the array (a)

Input: [5,1,3,6,8,2,4,7], k = 3
Output: [6,7,8]
"""

def k_largest_value(array, k):
    """
    Runtime: O(nlogn) + O(n) -> O(nlogn)
    """

    # Create a results array
    results = []
    # Sort the array
    array.sort()

    # Loop over the range of k
    for _ in range(k):
        # Pop and append the last values 
        results.append(array.pop())
    # Return the array
    return results

print(k_largest_value([5,1,3,6,8,2,4,7], 6)) 