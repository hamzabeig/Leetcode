class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "" or len(s) < len(t):
            return ""
        countT, window = {}, {}
        resL, resR, resSize = 0 , 0 , len(s)+1
        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i],0)
        l=0
        have=0
        need= len(countT)
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r],0)
            if s[r] in countT and window[s[r]]==countT[s[r]]:
                have+=1
            while have == need:
                if (r-l+1) < resSize:
                    resL = l
                    resR = r
                    resSize = r-l+1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        return s[resL:resR+1] if resSize != len(s)+1 else ""

