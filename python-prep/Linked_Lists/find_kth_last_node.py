#!python3
from linkedlist import Node


"""
Given a singly-linked list and an integer k, 
find the value in the kth-to-last node.

Input: LL: 1 -> 2 -> 3 -> 4 -> 5 -> //, k: 2
Output: 4

Assumptions:
- We will not know the length of the linked list
- We can do this in multiple passes if necessary
- We want to return the data of the node

Pseudocode: 
Traverse the LL and keep a count of how many nodes are
inside for the length

Use that count minus the k to help find the kth last node

Traverse the LL kth times to find the result
Return the data
"""

def find_kth_last_node(node, k):
    # Define the current node
    curr_node = node

    # Keeps track of our length of LL
    count = 0

    # Traverse through the Linked List 
    while curr_node is not None:
        count += 1 # Increment the count
        curr_node = curr_node.next # Traverse

    # Calculates our target data 
    target = count - k

    # Restate the head
    curr_node = node

    # Iterate target times
    for _ in range(target):
        curr_node = curr_node.next # Finds target data
    
    # Return the data
    return curr_node.data

# Test Code
# 1 -> 2 -> 3 -> 4 -> 5 -> //
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5) 

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print(find_kth_last_node(node1, 4))

