"""
Best Time to Buy and Sell Stock II

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time 
(i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Pseudocode:
    # Create a max_profit holder

    # Go through each index from 1 to the end
        # If the number before it is less than the current number
            # Add the result of the current number minus the previous number to max_profit
    
    # Return max_profit
"""

def max_profit(prices):
    max_profit = 0

    for index in range(1, len(prices)): # Iterate through the indexes starting at i: 1
        # If value of the day is greater than the previous day
        if prices[index] > prices[index - 1]: 
            # Get the profit from the two days and add it to max_profit
            max_profit += prices[index] - prices[index - 1] 

    return max_profit

print(max_profit([7,1,5,3,6,4]))
