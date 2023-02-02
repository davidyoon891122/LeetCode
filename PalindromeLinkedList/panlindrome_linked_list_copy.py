"""
Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.
"""

"""
Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []

        while head:
            vals += head.val,
            head = head.next

        print(vals, vals[::-1])
        return vals == vals[::-1]

                



node1 = ListNode(1)
node2 = ListNode(0)
node3 = ListNode(1)
# node4 = ListNode(1)

node1.next = node2
node2.next = node3
# node3.next = node4

s = Solution()

print(s.isPalindrome(node1))