# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      dummy = ListNode()
      current = dummy
      while list1 and list2:
        if list1.val > list2.val:
            current.next = list2
            list2 = list2.next
        else:
            current.next = list1
            list1 = list1.next
        current = current.next

      if list1:
        current.next = list1
      else:
        current.next = list2

      return dummy.next 




third_node = ListNode(4, None)
second_node = ListNode(2, third_node)
first_node = ListNode(1, second_node)

sixth_node = ListNode(4, None)
fourth_node = ListNode(3, sixth_node)
third_node = ListNode(1, fourth_node)

s = Solution()

result = s.mergeTwoLists(first_node, third_node)


