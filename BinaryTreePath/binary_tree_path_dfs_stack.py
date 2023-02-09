"""
Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.
"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.right:
                stack.append((node.right, ls+str(node.val) + "->"))
            if node.left:
                stack.append((node.left, ls+str(node.val) + "->"))
        return res

        

        


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(5)

node1.left = node2
node1.right = node3
node2.right = node4


s = Solution()
print(s.binaryTreePaths(node1))

