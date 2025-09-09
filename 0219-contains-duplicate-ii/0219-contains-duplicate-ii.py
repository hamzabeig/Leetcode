class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        contain = {}
        for i,j in enumerate(nums):
            if j in contain and (i - contain[j] <=k):
                return True
            contain[j] = i
        return False
        
        