# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMax(self,node):
        if not node:
            return float('-inf')
        return max(node.val,self.getMax(node.right),self.getMax(node.left))

    def getMin(self,node):
        if not node:
            return float('inf')
        return min(node.val,self.getMin(node.right),self.getMin(node.left))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        if root.left and self.getMax(root.left)>=root.val:
            return False
        if root.right and self.getMin(root.right)<= root.val:
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)
