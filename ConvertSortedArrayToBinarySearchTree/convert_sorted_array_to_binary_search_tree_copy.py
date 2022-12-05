"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.
"""

from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def rec(nums, start, end):
            if start <= end:
                mid = (start + end) // 2
                node = TreeNode(nums[mid])
                node.left = rec(nums, start, mid - 1)
                node.right = rec(nums, mid + 1, end)
                return node
        return rec(nums, 0, len(nums) - 1)
        

def inorder_traversal(node: TreeNode):
    if node == None:
        return
    inorder_traversal(node.left)
    print(node.val)
    inorder_traversal(node.right)


nums = [-10, -3, 0, 5, 9]


s = Solution()
root = s.sortedArrayToBST(nums)

inorder_traversal(root)

