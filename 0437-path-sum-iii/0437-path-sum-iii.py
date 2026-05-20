# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        def dfs(root, path):
            if not root:
                return
            path.append(root.val)
            dfs(root.left, path)
            dfs(root.right, path)
            sum = 0
            for i in range(len(path)-1, -1, -1):
                sum+= path[i]
                if sum == targetSum:
                    self.count+=1
            path.pop()

        dfs(root, [])
        return self.count

        