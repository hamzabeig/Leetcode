class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ref = {}
        for i in range(len(nums)):
            if nums[i] not in ref:
                ref[nums[i]] = 1
            else:
                return True
        return False