class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A = nums1
        B = nums2
        if len(A) > len(B):
            A , B = nums2, nums1
        total = len(A) + len(B)
        half = total // 2
        l=0
        r=len(A)-1

        while True:
            i = (l+r) //2
            j = half - i - 2

            Aleft = A[i] if i>=0 else float("-infinity")
            Aright = A[i+1] if i+1<len(A) else float("infinity")
            Bleft= B[j] if j>=0 else float("-infinity")
            Bright = B[j+1] if j+1<len(B) else float("infinity")

            if Aleft<=Bright and Bleft<=Aright: #cut is valid
                #odd
                if total % 2 !=0:
                    return min(Aright,Bright)
                else:
                    return (max(Aleft,Bleft) + min(Aright,Bright)) / 2
                #even
            elif Aleft>Bright:
                r = i-1
            else: #Bleft>Aright
                l = i+1