class Solution:
    def longestPalindrome(self, s: str) -> str:
        long_c = 1
        long_s = s[0]
        i = 0;
        while len(s[i:]) > long_c:
            for j in range(len(s), long_c+i-1, -1):                    
                cs = s[i:j]
                if cs == cs[::-1] and len(cs) > long_c:
                    long_s = cs
                    long_c = len(cs)
            i += 1 
        return long_s