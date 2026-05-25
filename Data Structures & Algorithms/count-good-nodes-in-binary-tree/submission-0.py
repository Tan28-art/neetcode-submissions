# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.goodCount = 0

    def dfsHelper(self, node, maxVal):
        
        if node is None:
            return 0
        
        maxVal = max(node.val, maxVal)

        if node.val >= maxVal:
            goodCount = 1
        else:
            goodCount = 0
        
        goodCount += self.dfsHelper(node.left, maxVal)
        goodCount += self.dfsHelper(node.right, maxVal)

        return goodCount

    def goodNodes(self, root: TreeNode) -> int:

        return self.dfsHelper(root, root.val)
        