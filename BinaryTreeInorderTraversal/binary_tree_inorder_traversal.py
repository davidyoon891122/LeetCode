"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""

from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        test = self.inorder_traversal_test(root, result)
        return test

    def inorder_traversal_test(self, root: Optional[TreeNode], result: []) -> List[int]:
        if root == None:
            return
        self.inorder_traversal_test(root.left, result)
        result.append(root.val)
        self.inorder_traversal_test(root.right, result)
        return result

# root_ex1 = [1, null, 2, 3]

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node1.right = node2
node2.left = node3


s = Solution()
s.inorder_traversal(node1) # 1 3 2

# PreOrder InOrder PostOrder traversal 출력에 대한 부분은 해결 했으나, 값을 Array에 담아 리턴하는 방법을 고민
# 다른 유저의 코드를 참고하니 함수 밖에서 Array를 넣어주어 Array에 값을 넣어주는 방식으로 해결