# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def h(node):
            if not node:
                return [True, 0]
            left = h(node.left)
            right = h(node.right)
            return [left[0] and right[0] and abs(right[1] - left[1]) <= 1, 1 + max(left[1], right[1])]
        return h(root)[0]
        
        