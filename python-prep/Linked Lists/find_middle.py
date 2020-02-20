#!python
from linkedlist import Node

"""
Given a non-empty, singly linked list with head node head, 
return a middle node of linked list.

If there are two middle nodes, return the second middle node.

Input: [1,2,3,4,5]

Output: Node 3 from this list (Serialization: [3,4,5])

The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
"""

"""
     Finds and returns the middle most node of the linked list
     
     Interview Challenge #2
     Given a linked list, write a function that returns the middle node.
     
    - Parameters:
        - head: The starting ListNode we will begin our reversal at
"""

def find_middle_node_one_pass(head: Node) -> Node:
    """
    Time Complexity: O(n/2) -> O(n) Where n is the number of nodes we pass through
    """
    slow = head # Pointer at regular speed
    fast = head # Pointer at regular double speed
    
    # Iterate as long as there is valid node for fast pointer
    while fast and fast.next: 
        slow = slow.next
        fast = fast.next.next
        
    # Returns the middle node    
    return slow 

"""
Code during Break-out session

Notes: The logic in the code is there but there are some error I encountered.
1) ListNode is not iterable. Because it is a linked list we can not index through it.
   perhaps a while loop would be more suitable.
"""

def find_middle_node(head: Node) -> Node:
    length = 0
    for _ in head:
        length += 1
    middle_node = length // 2

    node = head

    for _ in range(middle_node):
        node.next
    return node

"""
Code after doing research on the question

Notes: This is nearly identical to my initial code above however, 
it is more explicit and in working condition because of the while-loop
implemented.
 
"""

def middleNode(head: Node) -> Node:
    # Keep track of the current node so we can iterate through the LL
    current = head
    # A count to keep track of the total of nodes we iterate through
    count = 0

    # While current exists
    while current:
        # Increase the count
        count += 1
        # set the current to the next node
        current = current.next
    
    # Get the middle node after your iteration
    middle_node = int(count / 2)
    
    # Redefine the current for it to be ready to iterate again
    current = head
    # Iterate through the LL once more by the range of the middle variable
    for _ in range(middle_node):
        # Set the current to the next node
        current = current.next
    # return the current because it should be the middle now
    return current


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

print(find_middle_node_one_pass(node1))



