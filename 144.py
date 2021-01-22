#144. Binary Tree Preorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Recursive
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.dlr(root, res)
        return res

    def dlr(self, root, res):
        if root:
            res.append(root.val)
            self.dlr(root.left, res)
            self.dlr(root.right, res)


#Iterative
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stk, ans = [], []
        while stk or root:
            if root:
                stk.append(root)
                ans.append(root.val)
                root = root.left

            else:
                node = stk.pop()
                root = node.right

        return ans
