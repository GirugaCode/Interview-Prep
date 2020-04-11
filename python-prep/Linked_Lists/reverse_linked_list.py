#!python3
from linkedlist import Node
from linkedlist import LinkedList
"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""

def reverseList(self, head: Node) -> Node:
    # Start of the Linked List
    current_node = head

    # Assigns the prev to None
    prev = None

    while current_node is not None:
        next = current_node.next # Sets the next pointer to the next inital node
        current_node.next = prev # Sets the current.next pointer to the reversal side
        prev = current_node # Move to prev pointer to currentNode
        current_node = next # Iterates the current node through the Linked List
    
    # Returns the head to None to complete reversal
    return prev