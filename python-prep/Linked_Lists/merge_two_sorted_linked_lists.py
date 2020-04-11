#!python3
from linkedlist import Node
from linkedlist import LinkedList

"""
Write a function that takes 2 sorted linked lists and merges them into one.

1 -> 5 -> 8 -> 10
0 -> 2 -> 6 -> 11

//merges into

0 -> 1 -> 2 -> 5 -> 6 -> 8 -> 10 -> 11

"""

def mergeTwoLists(self, l1: Node, l2: Node) -> Node:
    """
    Runtime: O(n+m) -> O(n) where n is one list and m is the other list we traverse through
    """
    # Dummy place holder for head and tail
    head = Node(0)
    tail = head
    
    # Loop as long as there are values in l1 and l2
    while l1 and l2:
        # Choose the l1 if value is less that l2
        if l1.val <= l2.val:
            head.next = l1
            l1 = l1.next
        else:
            head.next = l2
            l2 = l2.next
        
        # Continues the iteration
        head = head.next
    
    # Checks if there are remainding values in either LL 
    # to append the rest of the values
    head.next = l1 or l2

    # Grabs reference to the head and returns the merged list
    return tail.next

def mergeTwoListsRecur(self, l1: Node, l2: Node) -> Node:
    """
    Runtime: O(n+m) -> O(n) where n is one list and m is the other list we traverse through
    """
    if not l1 or not l2:
        return l1 or l2
    
    if l1.data <= l2.data:
        l1.next = self.mergeTwoListsRecur(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoListsRecur(l1, l2.next)
        return l2
