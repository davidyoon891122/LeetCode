"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""

# 두 개의 트리어 주어 졌을때, 두 트리가 같은 같은 트리인지 확인하는 함수를 구현
# Pre, In, Post 중 하나의 값으로 출력하여 값이 동일하면 true

from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        first_array = []
        second_array = []

        first_result = self.get_preorder_traversal(p, first_array)
        second_result = self.get_preorder_traversal(q, second_array)
        print("first result: {}".format(first_result))
        print("second result: {}".format(second_result))
        if first_result == second_result:
            return True
        else:
            return False


    
    def get_preorder_traversal(self, root: Optional[TreeNode], result: []) -> List[int]:
        if root == None:
            result.append(None)
            return
        result.append(root.val)
        self.get_preorder_traversal(root.left, result)
        self.get_preorder_traversal(root.right, result)
        return result

    def get_inorder_traversal(self, root: Optional[TreeNode], result: []) -> List[int]:
        if root == None:
            return
        self.get_inorder_traversal(root.left, result)
        result.append(root.val)
        self.get_inorder_traversal(root.right, result)
        return result

    def get_postorder_traversal(self, root: Optional[TreeNode], result: []) -> List[int]:
        if root == None:
            result.append(None)
            return
        self.get_postorder_traversal(root.left, result)
        self.get_postorder_traversal(root.right, result)
        result.append(root.val)
        return result



node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node1.right = node2


node4 = TreeNode(1)
node5 = TreeNode(2)

node4.right = node5

# pre 1 -> 2 -> 3

s = Solution()
print(s.isSameTree(node1, node4))
