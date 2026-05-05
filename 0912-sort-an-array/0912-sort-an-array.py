class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:        
        def devide(nums):
            #base condition
            l = len(nums)
            if l <= 1:
                return nums

            mid = l //2
            return merge(devide(nums[:mid]),  devide(nums[mid: ]))  

        def merge(nums_left, nums_right):
            sub = []
            i , j = 0 ,0
            while i < len(nums_left) and j < len(nums_right):
                if nums_left[i] < nums_right[j]:
                    sub.append(nums_left[i])
                    i += 1
                else:
                    sub.append(nums_right[j])
                    j += 1

            while i < len(nums_left):
                sub.append(nums_left[i])
                i += 1

            while j < len(nums_right):
                sub.append(nums_right[j])
                j += 1

            return sub
        
        return devide(nums)