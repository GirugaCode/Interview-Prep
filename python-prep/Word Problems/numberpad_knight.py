"""
The numbers on a telephone keypad are arranged thus:

1 2 3
4 5 6
7 8 9
  0

Starting from any digit, and choosing successive digits as a knight moves in chess, 
determine how many different paths can be formed of length n. 
There is no need to make a list of the paths, only to count them.

A knight moves two steps either horizontally or vertically followed by one step in the 
perpendicular direction; thus, from the digit 1 on the keypad a knight can move to digits 6 or 8, 
and from the digit 4 on the keypad a knight can move to digits 3, 9 or 0. A path may visit the same 
digit more than once.

Your task is to write a function that determines the number of paths of length n 
that a knight can trace on a keyboard starting from any digit .

def findNumberOfPaths(int: digit, int: step):
    
"""
knightPaths = {}
knightPaths[1] = [6,8]
knightPaths[2] = [9,7]
knightPaths[3] = [4,8]
knightPaths[4] = [3,9,0]
knightPaths[5] = []
knightPaths[6] = [1,7,0]
knightPaths[7] = [6,2]
knightPaths[8] = [3,1]
knightPaths[9] = [4,2]
knightPaths[0] = [6,4]

def findNumberOfPaths(digit, step):
    neighbors = knightPaths[digit]
    count = 0
    if step == 1:
        return len(neighbors)
    for neighbor in neighbors:
        count += findNumberOfPaths(neighbor, step - 1)
    
    return count

print(findNumberOfPaths(2,3))