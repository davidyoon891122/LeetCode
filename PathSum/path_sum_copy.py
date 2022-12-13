"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if root.val == targetSum and not root.left and not root.right:
            return True
        
        left = self.hasPathSum(root.left, targetSum - root.val)
        right = self.hasPathSum(root.right, targetSum - root.val)
        return left or right

# 1. check root is None, if None, return False 
# 2. check node is leaf(node.left == None, node.right == None), then if root.val is targetSum, return True
# 3. substract root.val from targetSum 
# 4. recursive left and right node ther if there is a matched targetSum with node.val, return True

node1 = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(8)
node4 = TreeNode(11)
node5 = TreeNode(13)
node6 = TreeNode(4)
node7 = TreeNode(7)
node8 = TreeNode(2)
node9 = TreeNode(1)

node1.left = node2
node1.right = node3
node2.left = node4
node3.left = node5
node3.right = node6
node4.left = node7
node4.right = node8
node6.right = node9
target = 22

node_1 = TreeNode(1)
node_2 = TreeNode(2)

node_1.left = node_2

s = Solution()
result = s.hasPathSum(node1, target)

print("result: {}".format(result))

result_2 = s.hasPathSum(node_1, 1)

print("result: {}".format(result_2))
