class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return x ** n

#-----------------------------------------------------------
#Time Limit Exceed
        # if n< 0:
        #      x= 1/x
        #      n = -n
        # out = 1
        # while n>0:
        #     out = out * x
        #     n-=1
        # return out

#-----------------------------------------------------------
# Recusrion
        # if n < 0:
        #     x=1/x
        #     n=-n

        # if n == 0: 
        #     return 1

        # h = self.myPow(x,n//2)
        
        # if n % 2 ==0:
        #     return h * h
        # else:
        #     return x * h * h
        
#---------------------------------
        '''
        in binary we can represent any number in powers of two
        10 = 1010 in binary
        x^10 = x^8 + x^2
        so we add keep on increasing power of x and add in result 
        once least bit is 1 by cheking if n is odd.
        we keeping on dividing powers n by 2 to shift right
        and we check if least bit is set by checking if its odd
        then we add that power of x to result, otherwise increase x but
        don't add in result once least bit is 0
        '''
        if n < 0:
            x = 1 / x
            n = -n
        
        res = 1.0

        while n:
            if n % 2 == 1:
                res *= x
            x *= x
            n //= 2
        return res
    
    