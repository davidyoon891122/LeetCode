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
        value_array = []
        node = head
        while node:
            if node:
                print(node.val)
                value_array.append(node.val)
            
            node = node.next   
        print(value_array)
        if len(value_array) == 1:
            return True
        if len(value_array) % 2 != 0:
            
            half = len(value_array) // 2
            first = value_array[:half]
            second = value_array[half:]
            for i in range(len(first)):
                if first.pop() != second[i + 1]:
                    return False
            return True
        else:
            half = len(value_array)//2
            first = value_array[:half]
            second = value_array[half:]
            for i in range(len(first)):
                if first.pop() != second[i]:
                    return False
            return True

                



node1 = ListNode(1)
node2 = ListNode(0)
node3 = ListNode(0)
node4 = ListNode(1)

node1.next = node2
node2.next = node3
# node3.next = node4

s = Solution()

print(s.isPalindrome(node1))