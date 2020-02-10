#!python3
from linkedlist import Node
from linkedlist import LinkedList

"""
Write a function that removes all occurrences of a given element in a linked list.

1 -> 6 -> 8 -> 8 -> 4

// after removing all occurrences of 8
1 -> 6 -> 4
"""

def removeElements(self, head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    
    # Creates a dummy node starter head
    # Ensures the case of deleting the head node in LL 
    dummy_head = Node(-1)
    dummy_head.next = head
    
    current_node = dummy_head

    # Traverse through the LL
    while current_node.next is not None:
        # Once the value is found, change the pointer to the next value
        if current_node.next.val == val:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next # Base case traversal
            
    return dummy_head.next # Head of the node