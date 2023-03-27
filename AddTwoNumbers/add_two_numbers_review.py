"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newNode = currentNode = ListNode()
        carry = 0

        while l1 or l2 or carry:
            v1 = v2 = 0

            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            sum = v1 + v2 + carry
            value = sum % 10
            carry = sum // 10
            currentNode.next = ListNode(val=value)
            currentNode = currentNode.next

        return newNode.next

       
def printNode(node: Optional[ListNode]):
    while node.val:
        print(node.val)
        node = node.next


s = Solution()

first_node1 = ListNode(9)
first_node2 = ListNode(9)
first_node3 = ListNode(9)

first_node1.next = first_node2
first_node2.next = first_node3

second_node1 = ListNode(1)
second_node2 = ListNode(0)
second_node3 = ListNode(0)

# second_node1.next = second_node2
# second_node2.next = second_node3

result = s.addTwoNumbers(l1=first_node1, l2=second_node1)
printNode(node=result)