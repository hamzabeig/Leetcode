class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        #take xor of all numbers of range[0,n]
        for i in range(len(nums)+1):
            xor ^= i
        # xor of a number with itself is 0, so we will get missing number
        for num in nums:
            xor ^= num
        return xor

        