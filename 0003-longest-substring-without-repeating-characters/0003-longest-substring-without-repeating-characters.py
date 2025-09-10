class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dupSet = set()
        l=0
        longest = 0
        for c in range(len(s)):
            while s[c] in dupSet:
                dupSet.remove(s[l])
                l+=1
            dupSet.add(s[c])
            longest = max(longest, c-l+1)
        return longest

        