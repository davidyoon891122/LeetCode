"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.
"""

from typing import Optional
from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        count = 0
        queue = deque()
        
        queue.append(root)

        while queue:
            level_size = len(queue)
            count += 1
            print("queue: {}".format(queue))
            for i in range(level_size):
                curr = queue.popleft()
                if not curr.left and not curr.right:
                    return count
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return count


node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5

# node1 = TreeNode(-9)
# node2 = TreeNode()

s = Solution()
result = s.minDepth(node1)
print("result: {}".format(result))