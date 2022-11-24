"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""

from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        first_array = []
        second_array = []

        if root.left == None and root.right == None:
            return True

        first_result = self.get_preorder_traversal(root.left, first_array)
        second_result = self.get_postorder_traversal(root.right, second_array)

        if second_result == None:
            return False
        second_result.reverse()
        print("first_result {}".format(first_result))
        print("second_result {}".format(second_result))
        

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
node3 = TreeNode(2)
node4 = TreeNode(3)
node5 = TreeNode(4)
node6 = TreeNode(4)
node7 = TreeNode(3)

# node1.left = node2
# node1.right = node3
# node2.left = node4
# node2.right = node5
# node3.left = node6
# node3.right = node7

# pre 1 -> 2 -> 3

node1.left = node2
node1.right = node3
node2.right = node4
node3.right = node7


s = Solution()
print(s.isSymmetric(node1))
