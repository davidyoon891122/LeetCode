"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.
"""

from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def post_order(curr: Optional[TreeNode]):
            if curr is None:
                return 

            post_order(curr.left)
            post_order(curr.right)
            result.append(curr.val)

        post_order(root)

        return result
        


node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)

node_1.right = node_2
node_2.left = node_3


s = Solution()

print("result: {}".format(s.postorderTraversal(node_1)))