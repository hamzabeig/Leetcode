class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0
        def decode():
            result = ""
            num = 0
            while self.i < len(s):
                if s[self.i].isdigit():
                    num = num * 10 + int(s[self.i])
                    self.i+=1
                elif s[self.i] == "[":
                    self.i+=1
                    inner = decode()
                    result += inner*num
                    num = 0
                elif s[self.i]=="]":
                    self.i+=1
                    return result
                else:
                    result = result + s[self.i]
                    self.i += 1
            return result  
        return decode()                  

