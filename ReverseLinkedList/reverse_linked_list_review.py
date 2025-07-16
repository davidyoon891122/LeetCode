# Definition for singly-linked list.


from typing import Optional
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None # 두 개의 변수가 필요 움직이는 포인터 역할의 node, 이전값을 저장할 prev

        while node: # node가 존재하면 계속 진행
            next, node.next = node.next, prev # 다음 값들을 미리 저장 next 에는 현재 노드의 다음 값을 저장, node의 다음은 prev 를 가리키도록 적용(역순 처리를 위함)
            prev, node = node, next # 다음 순회를 위한 값 변경 prev는 현재 node가 되고, node는 미리 저장해둔 next를 넣어서 다음 순회를 준비
        return prev


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


s = Solution()

result = s.reverseList(node1)
print(result.val)