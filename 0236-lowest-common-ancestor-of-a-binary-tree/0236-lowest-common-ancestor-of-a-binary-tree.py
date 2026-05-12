# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # base case
        if not node:
            return None
        if node == p or node == q:
            return node

        #recursive case
        left = self.lowestCommonAncestor(node.left,p,q)
        right= self.lowestCommonAncestor(node.right,p,q)
        #return value
        #agr ap k left aur right dono mein values hain p and q to ap khud ko return kro
        #agr left pr value hai to left ko return kro
        #agr right pr value hai to right ko return kro
        if left and right :
            return node
        if left:
            return left
        if right:
            return right
        

        