"""
Let’s practice recursion on a very well-known (and pretty tired, tbh) interview problem.
You’re asked to write recursive FizzBuzz. Your function takes 2 integers: start and end, 
which are the first and last number in the sequence of integers to return in a list (array). 
However, if the number is a multiple of 3, put “Fizz” in the list instead of the number. 

If it’s a multiple of 5 put “Buzz” in the list. 
If it’s a multiple of 3 and 5, put “FizzBuzz” in the list.

Example: fizzbuzz(1, 20) ⇒ 
[1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz]

"""

def fizzbuzz(start, end, result=None):

    # Initializes the result array
    if result == None:
        result = []

    # Appends FizzBuzz
    if start % 3 == 0 and start % 5 == 0:
        result.append("FizzBuzz")
    
    # Appends Fizz
    if start % 3 == 0:
        result.append("Fizz")

    # Appends Buzz
    if start % 5 == 0:
        result.append("Buzz")
    else:
        result.append(start)

    # Base Case, Once the start reaches the end
    if start < end: 
        return fizzbuzz(start+1, end, result)
    
    # Returns the result
    return result

print(fizzbuzz(1,20))


    

    
