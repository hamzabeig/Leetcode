# storing prefixSum in a dict and checking curSum - k in prefixSum
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        # to count first sum, we initialize 0 before it as 1 to count
        prefixSum = {0:1}
        for n in nums:
            curSum += n
            diff = curSum - k
            # now we check how many diff we have stored in prefix Sum
            res += prefixSum.get(diff,0)
            prefixSum[curSum] = 1 + prefixSum.get(curSum,0)
        return res
