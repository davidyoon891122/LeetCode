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
        elements = []

        elements = self.add_element_to_list(list1, elements)
        elements = self.add_element_to_list(list2, elements)
        elements.sort()

        result = self.createListNode(elements)

        return result 

        
    def add_element_to_list(self, node: Optional[ListNode], result: List[int]) -> List[int]:
        current_node = node
        if current_node == [] or current_node is None:
            return []
        while True:
            result.append(current_node.val)
            if current_node.next is not None:
                current_node = current_node.next
            else:
                return result
                break

    def createListNode(self, sortedList: List[int]) -> Optional[ListNode]:
        result = []
        if len(sortedList) == 0:
            return []
        for index, value in enumerate(sortedList):
            node = ListNode(value, None)
            result.append(node)
        for index in range(1, len(result)):
            result[index - 1].next = result[index]
        
        return result[0]
    

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
result = s.mergeTwoLists([], [0])
display_node_values(node=result)

