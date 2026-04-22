class Solution:
    def itr_decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_str =""

        for ch in s:
            if ch.isnumeric():    # ch.isdigit()  -- only for 0-9, better here
                curr_num = curr_num * 10 + int(ch)

            elif ch == "[":
                # inner  = # level of recursion                 
                stack.append((curr_str, curr_num))
                curr_num = 0
                curr_str =""

            elif ch == "]":
                # return recursion acc
                pre_str, num = stack.pop()
                curr_str = pre_str + curr_str * num
                
            else:
                curr_str += ch

        
        return curr_str


    def decodeString(self, s: str) -> str:
        self.i = 0

        def decode():
            num = 0
            result = ""

            while self.i < len(s):

                ch = s[self.i]

                if ch.isdigit():
                    self.i+=1
                    num = num * 10 + int(ch)
                elif ch == "[":
                    self.i+=1
                    inner = decode()
                    
                    result += num * inner
                    num=0
                    # result=""
                    

                elif ch == "]":
                    self.i+=1
                    return result
                else:
                    self.i+=1
                    result+=ch
            return result
        return decode()




        
