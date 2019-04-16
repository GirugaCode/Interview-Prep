# Function => input [2, 5, 1, 6];
# Output => [6, 1, 5, 2];

# Create function takes in a list of ints and reverses it
# Get the last the index of the list 
# Remove it and append it to the begging
# Iterate as many time of how long the list is
# Return List

def reverse_list(nums):
    result = []
    last_index = len(nums) - 1 
    
    for index in range(last_index, -1, -1):
        result.append(nums[index])
    return result
    
print(reverse_list([2,5,1,6]))


def reverse_list_two(nums):
    result = []
    while nums:
        result.append(nums.pop())
    return result
print(reverse_list_two([2,5,1,6]))