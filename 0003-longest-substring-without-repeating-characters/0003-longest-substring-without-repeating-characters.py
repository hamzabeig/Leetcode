class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        eye = set()
        l=0
        length = 0
        for r in range(len(s)):
            while s[r] in eye:
                eye.remove(s[l])
                l+=1
            eye.add(s[r])
            length = max(length, r-l+1)

        return length
        