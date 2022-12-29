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
        stack = [root]
        visit = [False]
        res = []

        while stack:
            print(stack)
            curr, visited = stack.pop(), visit.pop()

            if curr:
                if visited:
                    res.append(curr.val)
                else:
                    stack.append(curr)
                    visit.append(True)
                    stack.append(curr.right)
                    visit.append(False)
                    stack.append(curr.left)
                    visit.append(False)
        return res
        


node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)

node_1.right = node_2
node_2.left = node_3


s = Solution()

print("result: {}".format(s.postorderTraversal(node_1)))