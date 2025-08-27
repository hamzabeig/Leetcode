# Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] +=1
            if len(count) <=2:
                continue
            else:
                new_count= defaultdict(int)
                for n,v in count.items():
                    if v>1:
                        new_count[n]= v-1
                count = new_count
        res = []
        for n in count.keys():
            if nums.count(n) > len(nums)//3:
                res.append(n)
        return res 