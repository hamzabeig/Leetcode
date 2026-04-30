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
        if n < 0:
            x=1/x
            n=-n
            
        if n == 0: 
            return 1

        h = self.myPow(x,n//2)
        
        if n % 2 ==0:
            return h * h
        else:
            return x * h * h
        