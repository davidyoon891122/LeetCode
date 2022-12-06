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
        return (self.depthCheck(root) >= 0)
        

    def depthCheck(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        leftHeight, rightHeight = self.depthCheck(root.left), self.depthCheck(root.right)
        print("leftHeight: {}, rightHeight: {}".format(leftHeight, rightHeight))
        if leftHeight < 0 or rightHeight < 0 or abs(leftHeight - rightHeight) > 1:
            return -1
        return max(leftHeight, rightHeight) + 1






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

