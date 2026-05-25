# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root) -> [bool, int]:
        # base case
        if root is None:
            return [True, 0]

        left = self.helper(root.left)
        right = self.helper(root.right)
        balanced = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)

        return [balanced, 1 + max(left[1], right[1])]


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = self.helper(root)[0]
        return balanced



        