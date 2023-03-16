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

        list1 = self.nodeToList(root=l1)
        list2 = self.nodeToList(root=l2)

        min_length = min(len(list1), len(list2))
        max_length = max(len(list1), len(list2))
        
        diff = max_length - min_length

        if len(list1) < len(list2):
            list1 += [0] * diff
        else:
            list2 += [0] * diff
        carry = 0
        result = []
        for i in range(max_length):
            sum = list1[i] + list2[i] + carry
            if sum >= 10:
                result.append(sum % 10)
                carry = 1
            else:
                result.append(sum)
                carry = 0
        if carry == 1:
            result.append(1)
        result.reverse()
        return self.listToNode(list=result)
            
    
    def nodeToList(self, root: Optional[ListNode]) -> List[int]:
        result = []
        while root:
            result.append(root.val)
            root = root.next
        return result
    
    def listToNode(self, list: List[int]) -> Optional[ListNode]:
        result = []
        for i in range(len(list)):
            result.append(ListNode(list[i]))
            
        for i in range(len(result)):
            if len(result) != i + 1:
                result[i].next = result[i+1]
        
        return result[0]

    
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