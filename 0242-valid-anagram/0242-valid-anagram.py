class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        compare1 = {}
        compare2 = {}
        for i in range(len(s)):
            if s[i] not in compare1:
                compare1[s[i]] = 1    
            else:
                compare1[s[i]] += 1
        for j in range(len(t)):
            if t[j] not in compare2:
                compare2[t[j]] = 1 
            else:
                compare2[t[j]] += 1 
        for c in compare1.keys():
            if c in compare1 and c in compare2 and compare1[c] != compare2[c]:
                return False
            elif c in compare1 and c not in compare2:
                return False
        return True