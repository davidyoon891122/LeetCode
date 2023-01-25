"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None

        cur = head

        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
                
        if head.val == val:
            head= head.next
        return head

def displayNode(node: Optional[ListNode]):
    while node is not None:
        print(node.val)
        node = node.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(6)
d = ListNode(3)
e = ListNode(4)
f = ListNode(5)
g = ListNode(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

s = Solution()
result = s.removeElements(a, 6)

# displayNode(result)

