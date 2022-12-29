"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
"""

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        value_array = []
        if head is None:
            return False

        while True:
            if id(head) in value_array:
                return True
            value_array.append(id(head))
            if head.next is None:
                return False
            head = head.next

            



node_1 = ListNode(3)
node_2 = ListNode(2)
node_3 = ListNode(0)
node_4 = ListNode(-4)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_2

s = Solution()
s.hasCycle(node_1)

