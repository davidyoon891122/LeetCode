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
        print("getIntersctionNode")

        if headA is None or headB is None:
            return ListNode(0)
        
        a_list = self.getListFromNode(headA)
        b_list = self.getListFromNode(headB)

        match_index = None
    
        for i in range(len(a_list)):
            if a_list[i] in b_list:
                match_index = i
                break

        if match_index is None:
            return None
        else:
            return self.getValueFromNode(headA, match_index)


    def getListFromNode(self, node: ListNode) -> List[int]:
        result = []

        while True:
            if node is None:
                return result
            result.append(id(node))
            node = node.next

    def getValueFromNode(self, node: ListNode, index: int):
        i = 0 

        while True:
            if i == index:
                return node
            
            node = node.next
            i += 1            


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