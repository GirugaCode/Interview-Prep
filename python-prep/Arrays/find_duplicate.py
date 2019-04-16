# Find number of duplicates
# Input => [1, 2, 1, 2, 3, 4, 5];
# Output => 2

# Result = 0
# Create an empty array
# Iterate through the list
# If empty has the value => Result += 1 
    #else: Pushing value into the empty array
# Return result

def find_duplicate(nums):
    result = 0
    empty_array = [] #[1,2,3,4,5]
    
    for index in nums:
        print(index)
        if index in empty_array:
            result += 1 
        else:
            empty_array.append(nums[index])
    return result

print(find_duplicate([1,2,1,2,3,4,5]))