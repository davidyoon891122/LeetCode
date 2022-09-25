from typing import Optional
from typing import List

# Definition for singly-linked list.

# list1 0 -> 1      3 -> 4
# list2 3 -> 4      0 -> 1
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp_node = ListNode(0)
        cur = temp_node
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return temp_node.next
            
        
    def printAllNodeValue(self,node: ListNode):
        current_node = node
        if current_node == []:
            return current_node
        while True:
            print(current_node.val)
            if current_node.next != None:
                current_node = current_node.next
            else:
                break



# Test Cases
third_node = ListNode(4, None)
second_node = ListNode(2, third_node)
first_node = ListNode(1, second_node)

sixth_node = ListNode(4, None)
fiveth_node = ListNode(3, sixth_node)
fourth_node = ListNode(1, fiveth_node)

test_node = ListNode(None, None)

s = Solution()

result = s.mergeTwoLists(first_node, fourth_node)
s.printAllNodeValue(result)
