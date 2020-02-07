#!python

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

# Definition for singly-linked list.
class ListNode:
    def __init__(self, head):
        self.head = head
        self.next = None


"""
     Finds and returns the middle most node of the linked list
     
     Interview Challenge #2
     Given a linked list, write a function that returns the middle node.
     
    - Parameters:
        - head: The starting ListNode we will begin our reversal at
"""
class SolutionThree:
    def find_middle_node_one_pass(self, head: ListNode) -> ListNode:
        """
        Time Complexity: O(n/2) -> O(n) Where n is the number of nodes we pass through
        """
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow

"""
Code during Break-out session

Notes: The logic in the code is there but there are some error I encountered.
1) ListNode is not iterable. Because it is a linked list we can not index through it.
   perhaps a while loop would be more suitable.
"""
class SolutionTwo:
    def find_middle_node(self, head: ListNode) -> ListNode:
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
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
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




