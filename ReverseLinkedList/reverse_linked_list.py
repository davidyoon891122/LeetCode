"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        if cur is None:
            return
        node_array = []
        while cur:
            node_array.append(cur)
            cur = cur.next
        j = len(node_array) - 2 
        for i in node_array[::-1]:
            if j < 0:
                i.next = None
            i.next = node_array[j]
            j = j - 1
        node_array[0].next = None
        
        return node_array[-1]

        
            

    
            






node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

s = Solution()
result = s.reverseList(node1)
# print(result.val)
while result:
    print(result.val)
    result = result.next