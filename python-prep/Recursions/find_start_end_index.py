"""
Given a sorted array of strings, 
write a recursive function to find the index of the first and last occurrence of a target string. 
If the target string is not found in the array, report that.
Example input:  

instructors = [Adriana, Adriana, Alan, Alan, Alan, Alan, Alan, 
               Braus, Braus, Braus, Braus, Dan, Dan, Dan, Dan, 
               Dan, Dani, Dani, Jess, Meredith, Milad, Milad, 
               Mitchell, Mitchell, Mitchell, Mitchell]

Example execution:  find_indexes(instructors, 'Braus')  ⇒  (7, 10)


"""

def search_range(instructors, target, curr_index=0, result=None):
    """
    Runtime: O(n) where n is the number of times we have to traverse through the list
    Space Complexity: O(2n) -> O(n) where 2n is the number of space we create with an array + tuple
    """
    # Return None if there are no targets
    if target not in instructors:
        return None
    
    # Instantiate the results
    if result == None:
        result = []
    
    # Base case to check if we've went through the entire list
    if instructors[curr_index] > target:
        first_index = result[0] # Gets the first index
        last_index = result[len(result) - 1] # Gets the last index
        new_result = (first_index, last_index) # Create the result as tuple
        return new_result

    # Appends all occurrences of target in array
    if instructors[curr_index] == target:
        result.append(curr_index)

    # Recursive call that goes through every index of list
    return search_range(instructors, target, curr_index + 1, result)

print(search_range(["Adriana", "Adriana", "Alan", "Alan", "Alan", "Alan", "Alan", 
               "Braus", "Braus", "Braus", "Braus", "Dan", "Dan", "Dan", "Dan", 
               "Dan", "Dani", "Dani", "Jess", "Meredith", "Milad", "Milad", 
               "Mitchell", "Mitchell", "Mitchell", "Mitchell"], "Braus"))

