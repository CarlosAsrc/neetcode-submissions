# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0

        def h(node):
            if node is None:
                return 0
            lefth = h(node.left)
            righth = h(node.right)
            self.d = max(lefth + righth, self.d)
            return 1 + max(lefth, righth)
        h(root)
        return self.d
