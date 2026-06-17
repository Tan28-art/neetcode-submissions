# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # i would assume check curr, check left sub tree, check right sub tree

        # here iteration is via recursion
        # meaning to check p and q value you just pass left and right subtree and check p.val and q.val

        if p is None and q is None:
            return True
        elif (p is None and q) or (p and q is None):
            return False
        else:
            if p.val != q.val:
                return False
            else:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)