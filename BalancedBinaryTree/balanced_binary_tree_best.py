"""
Given a binary tree, determine if it is height-balanced.
(A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.)
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 0
        
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            height = max(left, right) + 1

            if abs(left - right) > 1 or left == -1 or right == -1:
                return -1
            
            return height

        if dfs(root) == -1:
            return False
        return True
        





node_1 = TreeNode(3)
node_2 = TreeNode(9)
node_3 = TreeNode(20)
node_4 = TreeNode(15)
node_5 = TreeNode(7)

node_1.left = node_2
node_1.right = node_3
node_3.left = node_4
node_3.right = node_5

s = Solution()

print("result : {}".format(s.isBalanced(node_1)))

