# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        def dfs(start,end):

            if (start,end) in memo:
                return memo[(start,end)]


            if start > end:
                return [None]

            all_trees = []
           
            for root_val in range(start,end+1):
                
                left_trees = dfs(start, root_val-1)
                right_trees = dfs(root_val+1 , end)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                       
                        all_trees.append(root)

            memo[(start,end)] = all_trees
            return memo[(start,end)] 
            
        
        
        return dfs(1,n)




        





