#102. Binary Tree Level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        ans = []
        lvl = [root]
        while lvl:
            ans.append([node.val for node in lvl])
            temp = []
            for node in lvl:
                temp.extend([node.left, node.right])

            lvl = [node for node in temp if node]

        return ans
