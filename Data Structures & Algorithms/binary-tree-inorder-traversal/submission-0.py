# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        def inorder(node):
            # Think about when we are returning, when the node becomes None
            if not node:
                return

            # visit left
            inorder(node.left)
            # current we add
            res.append(node.val)
            # visit right
            inorder(node.right)

        inorder(root)
        return res
        