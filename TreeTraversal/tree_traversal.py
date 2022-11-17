"""
Tree Traverse
Pre NLR
In LNR
Post LRN
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7


def preorder_traversal(node: TreeNode):
    if node == None:
        return

    print(node.val)
    preorder_traversal(node.left)
    preorder_traversal(node.right)

def inorder_traversal(node: TreeNode):
    if node == None:
        return
    inorder_traversal(node.left)
    print(node.val)
    inorder_traversal(node.right)

def postorder_traversal(node: TreeNode):
    if node == None:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.val)



print("----------------")
preorder_traversal(node1)
print("----------------")
inorder_traversal(node1)
print("----------------")
postorder_traversal(node1)


