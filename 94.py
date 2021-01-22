#94. Binary Tree Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.ldr(root, res)
        return res

    def ldr(self, root, res):
        if root:
            self.ldr(root.left, res)
            res.append(root.val)
            self.ldr(root.right, res)



#Iterative
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stk, res = [], []
        while stk or root:
            if root:
                stk.append(root)
                root = root.left

            else:
                node = stk.pop()
                res.append(node.val)
                root = node.right

        return res
