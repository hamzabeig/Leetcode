# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #nlogn
    def pathSum_o(self, root: Optional[TreeNode], targetSum: int) -> int:
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
    #O(n)
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.pref = {0:1}
        def dfs(root, curr_max):
            if not root:
                return 0
            
            curr_max += root.val
            count = self.pref.get(curr_max-targetSum, 0)
            self.pref[curr_max] = self.pref.get(curr_max,0) + 1
            count += dfs(root.left, curr_max)
            count += dfs(root.right, curr_max)
            self.pref[curr_max]-=1
            
            return count
        return dfs(root, 0)