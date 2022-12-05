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
        middle_value_index = len(nums) // 2
        # print(middle_value_index)

        if middle_value_index == 0 and len(nums) == 0:
            return 

        root = TreeNode(nums[middle_value_index])


        left_node = self.sortedArrayToBST(nums[0:middle_value_index])
        right_node = self.sortedArrayToBST(nums[middle_value_index + 1:])
        
        root.left = left_node
        root.right = right_node
        return root
        

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

