"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
"""

from typing import Optional, List

# Time Limit Exceeded
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None

        point_a = headA
        point_b = headB
        count = 0
        while point_a is not point_b:
            count += 1
            print("count: {}".format(count))
            point_a = headB if point_a is None else point_a.next
            point_b = headA if point_b is None else point_b.next

        return point_a

# state node
a_node_1 = ListNode(4)
a_node_2 = ListNode(1)

b_node_1 = ListNode(5)
b_node_2 = ListNode(6)
b_node_3 = ListNode(1)

c_node_1 = ListNode(8)
c_node_2 = ListNode(4)
c_node_3 = ListNode(5)

# make connections
a_node_1.next = a_node_2
# a_node_2.next = c_node_1

b_node_1.next = b_node_2
b_node_2.next = b_node_3
# b_node_3.next = c_node_1

s = Solution()

result = s.getIntersectionNode(a_node_1, b_node_1)
print("result: {}".format(result))