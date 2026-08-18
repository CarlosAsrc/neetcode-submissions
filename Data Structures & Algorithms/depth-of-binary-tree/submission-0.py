# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left, right = 0, 0
        
        if root.left is None:
            left = 1
        else:
            left = self.maxDepth(root.left) + 1

        if root.right is None:
            roght = 1
        else:
            right = self.maxDepth(root.right) + 1
        
        return max(left, right)
        