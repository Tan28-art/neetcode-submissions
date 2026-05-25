# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # we want to check if subroot is a subtree of root
        # subtree is essentially if subroot is the same tree as some part of root 
        # a tree is same if, vals are same, left is same and right is same, their children exactly same as well

        # if subroot is null then it is a subtree regardless of root
        if not subRoot:
            return True
        # if root is null then we know subroot is not, so it cannot be a subtree
        if not root:
            return False
        
        # after this we want to check whether or not the tree at root and tree at subroot are actually the same
        # if they are then we can return true, if not we need to recursively go through the entire tree and check
        if self.sameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot)) or (self.isSubtree(root.right, subRoot)) 

    
    def sameTree(self, tree1, tree2) -> bool:
        if not tree1 and not tree2:
            return True
        if tree1 and tree2 and (tree1.val == tree2.val):
            return self.sameTree(tree1.left, tree2.left) and self.sameTree(tree1.right, tree2.right)

        return False