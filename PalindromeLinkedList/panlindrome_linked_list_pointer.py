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
        slow = fast = head
        
        # Find the Middle Node of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        # Reverse the second half of the Linked List
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # Compare the two value of linked Lists to check for palindrome
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
            
        return True
        




node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(0)
node4 = ListNode(1)
node5 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

s = Solution()

print(s.isPalindrome(node1))