class Solution:
    def convert(self, s: str, numRows: int) -> str:
        new_str = ''
        n = numRows-1
        if(n==0):
            n=1
        i=0
        while i < numRows:
            j=i
            k=2*n-i
            while j < len(s):
                new_str += s[j]
                if (i!= 0 and i != n) and k < len(s):
                    new_str += s[k]
                if numRows == 1:
                    j+=1
                else:
                    j+=2*n
                k+=2*n
            i+=1
        return new_str
            
            
            