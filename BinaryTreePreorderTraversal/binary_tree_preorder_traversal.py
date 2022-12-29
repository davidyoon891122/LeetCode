"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.
"""

from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.setValueInArray(root, result)
        return result
        


    def setValueInArray(self, root: Optional[TreeNode], result: List[int]):
        if root is None:
            return
        result.append(root.val)
        self.setValueInArray(root.left, result)
        self.setValueInArray(root.right, result)


node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)

node_1.right = node_2
node_2.right = node_3

s = Solution()

print("result: {}".format(s.preorderTraversal(node_1)))