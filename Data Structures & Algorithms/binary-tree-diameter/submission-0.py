# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0

    def depthOfTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.depthOfTree(root.left)
        right = self.depthOfTree(root.right)
        depth = 1 + max(left, right)
        
        self.diameter = max(self.diameter, left + right)
        return depth
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depthOfTree(root)
        return self.diameter
        