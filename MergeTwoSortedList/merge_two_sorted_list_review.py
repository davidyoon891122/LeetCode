"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""
# Constraints
"""
* The number of nodes in both lists is in the range [0, 50].
* -100 <= Node.val <= 100
* Both list1 and list2 are sorted in non-decreasing order.
"""

from typing import Optional
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # list1 0 -> 1      3 -> 4
    # list2 3 -> 4      0 -> 1
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_node = current_node = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                current_node.next = list1
                list1 = list1.next
            else:
                current_node.next = list2
                list2 = list2.next
            current_node = current_node.next

        if list1:
            current_node.next = list1
        if list2:
            current_node.next = list2

        return new_node.next


def display_node_values(node: Optional[ListNode]):
    while node:
        print(node.val)

        node = node.next

third_node = ListNode(4, None)
second_node = ListNode(2, third_node)
first_node = ListNode(1, second_node)

sixth_node = ListNode(4, None)
fourth_node = ListNode(3, sixth_node)
third_node = ListNode(1, fourth_node)

s = Solution()

result = s.mergeTwoLists(first_node, third_node)

display_node_values(node=result)

