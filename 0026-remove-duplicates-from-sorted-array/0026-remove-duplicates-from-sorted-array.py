class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=0
        check = set()
        for r in range(len(nums)):
            if nums[r] not in check:
                nums[l] = nums[r]
                l+=1
                check.add(nums[r])
        return l

        