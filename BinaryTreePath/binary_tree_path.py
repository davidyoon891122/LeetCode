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
        res = []

        self.create_path(root, "", res)

        return res

    def create_path(self, root, path, result):
        if not root:
            return

        if not root.left and not root.right:
            path += "{}".format(root.val)
            result.append(path)
        
        if root.left:
            self.create_path(root.left, "{}{}->".format(path, root.val), result)
        if root.right:
            self.create_path(root.right, "{}{}->".format(path, root.val), result)

        

        


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(5)

node1.left = node2
node1.right = node3
node2.right = node4


s = Solution()
print(s.binaryTreePaths(node1))

