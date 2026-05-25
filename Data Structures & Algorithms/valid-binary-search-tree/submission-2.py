# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfsHelper(node, left, right):
            if node is None:
                return True
            elif not(left < node.val < right):
                return False
            
            return (dfsHelper(node.left, left, node.val) and 
                    dfsHelper(node.right, node.val, right))

        return dfsHelper(root, float("-inf"), float("inf"))