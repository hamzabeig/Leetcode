class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=0
        r=0
        res=[]
        while l < len(word1) or r<len(word2):
            if l<len(word1):
                res.append(word1[l])
            if r<len(word2):
                res.append(word2[r])
            l+=1
            r+=1
        return "".join(res)