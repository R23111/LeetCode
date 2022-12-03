class Solution:
    def reverse(self, x: int) -> int:

#        neg = False
#        if x < 0:
#            x*=-1
#            neg = True   
#        x = int(str(x)[::-1])        
#        if neg:
#            x *=-1
#        return x

        sig = 1
        if x < 0:
            sig = -1

        xn = 0        
        while x !=0:
            xn*=10
            xn += x%(10*sig)
            x = int(x/10)        
            
        if xn <= -2**31 or xn >= 2**31-1:
            return 0             
        
        return xn