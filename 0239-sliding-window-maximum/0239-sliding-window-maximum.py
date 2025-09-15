class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        Max = deque()
        l = 0
        r = 0
        res= []
        while r < len(nums):
            while Max and nums[r]> nums[Max[-1]]:
                Max.pop()
            Max.append(r) 

            if l > Max[0]:
                Max.popleft()

            if (r+1) >= k :
                res.append(nums[Max[0]])
                l+=1
                
            r+=1
            
        return res

        