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
Code during Break-out session

Notes: The logic in the code is there but there are some error I encountered.
1) ListNode is not iterable. Because it is a linked list we can not index through it.
   perhaps a while loop would be more suitable.
"""
class SolutionTwo:
    def find_middle_node(self, head: ListNode) -> ListNode:
        length = 0
        for item in ListNode:
            length += 1
        middle_node = length // 2

        node = head

        for item in range(middle_node):
            node.next
        return node




