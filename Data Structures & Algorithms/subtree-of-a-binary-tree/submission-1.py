# Definition for a binary tree node.
# class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSametree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return self.isSametree(p.left, q.left) and self.isSametree(p.right, q.right)

        else:
            return False

    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # match not found
        if root is None:
            return False
        
        elif root.val == subRoot.val:
            return self.isSametree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        # move on to next node
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

                