"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        if current_node == [] or current_node == None:
            return current_node
        next_node = head.next   
        while True:
            if next_node == None:
                break
            if current_node.next != None:
                if current_node.val == next_node.val:
                    current_node.next = next_node.next
                    next_node = next_node.next
                else:
                    current_node = current_node.next
            else:
                break

        return head


# Test Cases
third_node = ListNode(1, None)
second_node = ListNode(1, third_node)
first_node = ListNode(1, second_node)

eighth_node = ListNode(3, None)
seventh_node = ListNode(3, eighth_node)
sixth_node = ListNode(2, seventh_node)
fiveth_node = ListNode(2, sixth_node)
fourth_node = ListNode(1, fiveth_node)


def display_nodes(nodes: Optional[ListNode]):
    if nodes == []: 
        return 
    current_node = nodes
    while True:
        print(current_node.val)
        if current_node.next != None:
            current_node = current_node.next
        else:
            break

s = Solution()
first_result = s.delete_duplicates(first_node)
second_result = s.delete_duplicates(fourth_node)
display_nodes(first_result)
print("--------")
display_nodes(second_result)