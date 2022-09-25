from typing import Optional
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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
        if current_node == [] or current_node.val is None:
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
            return None
        for index, value in enumerate(sortedList):
            node = ListNode(value, None)
            result.append(node)
        for index in range(1, len(result)):
            result[index - 1].next = result[index]

        return result[0]

    def printAllNodeValue(self, node: ListNode):
        current_node = node
        if current_node == []:
            return current_node
        while True:
            print(current_node.value)
            if current_node.next != None:
                current_node = current_node.next
            else:
                break

third_node = ListNode(4, None)
second_node = ListNode(2, third_node)
first_node = ListNode(1, second_node)

sixth_node = ListNode(4, None)
fourth_node = ListNode(3, sixth_node)
third_node = ListNode(1, fourth_node)

test_node = ListNode(None, None)

s = Solution()

result = s.mergeTwoLists([], sixth_node)