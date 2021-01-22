#145. Binary Tree Postorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.lrd(root, res)
        return res[::-1]

    def lrd(self, root, res):
        if root:
            res.append(root.val)
            self.lrd(root.right, res)
            self.lrd(root.left, res)


#Iterative
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stk = []
        while stk or root:
            if root:
                stk.append(root)
                ans.append(root.val)
                root = root.right

            else:
                node = stk.pop()
                root = node.left

        return ans[::-1]
