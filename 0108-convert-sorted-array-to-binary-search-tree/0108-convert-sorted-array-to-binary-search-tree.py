# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def recursion(nums, l , r):
            if l>r :
                return

            mid = l+ (r-l)//2

            root = TreeNode(nums[mid])
            root.left = recursion(nums,l,mid-1)
            root.right = recursion(nums,mid+1,r)

            return root

        return recursion(nums, 0, len(nums)-1)        