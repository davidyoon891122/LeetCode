"""
Given the root of a binary tree, invert the tree, and return its root.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        temp = root
        root.left = temp.right
        root.right = temp.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root



def printPost(root: Optional[TreeNode]):
    printPost(root.left)
    printPost(root.right)
    print(root.val)

node1 = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(7)
node4 = TreeNode(1)
node5 = TreeNode(3)
node6 = TreeNode(6)
node7 = TreeNode(9)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

s = Solution()
result = s.invertTree(node1)

printPost(result)