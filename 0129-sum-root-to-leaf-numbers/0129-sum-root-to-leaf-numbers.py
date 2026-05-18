# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        def dfs(root, curr_sum):
            if not root:
                return 0
            if not root.left and not root.right:
                self.sum += curr_sum *10 + root.val

            curr_sum = curr_sum *10 + root.val
            dfs(root.left,curr_sum)
            dfs(root.right, curr_sum)

        dfs(root, 0)
        return self.sum