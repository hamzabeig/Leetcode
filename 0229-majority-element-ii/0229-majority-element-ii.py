class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num1 = num2 = -1
        cnt1 = cnt2 = 0

        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
            elif cnt1 == 0:
                cnt1 = 1
                num1 = num
            elif cnt2 == 0:
                cnt2 = 1
                num2 = num
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1 = cnt2 = 0
        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1

        res = []
        if cnt1 > n // 3:
            res.append(num1)
        if cnt2 > n // 3:
            res.append(num2)

        return res

 # Boyer-Moore Voting Algorithm
# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
#         count = defaultdict(int)
#         for n in nums:
#             count[n] +=1
#             if len(count) <=2:
#                 continue
#             else:
#                 new_count= defaultdict(int)
#                 for n,v in count.items():
#                     if v>1:
#                         new_count[n]= v-1
#                 count = new_count
#         res = []
#         for n in count.keys():
#             if nums.count(n) > len(nums)//3:
#                 res.append(n)
#         return res 