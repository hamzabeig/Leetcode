# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.result = []
        def dfs(node: Optional[TreeNode], local_sum, list1):
            list2 = list1[:]
            if  node == None:
                return

            local_sum  += node.val
            list2.append(node.val)
            if not node.left and not node.right:
                if local_sum == targetSum:
                    self.result.append(list2)
                    return
            dfs(node.left, local_sum,list2)
            dfs(node.right, local_sum,list2)

        dfs (root, 0, [])
        return self.result












        