# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(node):
            if not node:
                return 0
            
            leftHeight = 1 + height(node.left)
            rightHeight = 1 + height(node.right)
            
            return leftHeight if leftHeight > rightHeight else rightHeight

        # leaf node is balanced
        if not root:
            return True

        #check root and subtrees
        left = height(root.left)
        right = height(root.right)
        
        if abs(left - right) > 1:
            return False

        rootLH = self.isBalanced(root.left)
        rootRH = self.isBalanced(root.right)

        return rootLH and rootRH