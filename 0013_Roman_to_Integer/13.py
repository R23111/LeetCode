class Solution:
    def romanToInt(self, s: str) -> int:
        rom = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        ans = 0
        
        for i in range(len(s)-1):
            if rom[s[i]] < rom[s[i+1]]:
                ans -= rom[s[i]]
            else: 
                ans += rom[s[i]]    
            
        ans += rom[s[-1]]
        return ans