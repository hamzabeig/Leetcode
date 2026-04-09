class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def countDigit(n):
            d = 0
            while n>0:
                n//=10
                d+=1
            return d
        count = 0
        for num in nums:
            if countDigit(num) % 2 == 0 :
                count +=1
        return count      