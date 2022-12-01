class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        half = int(len(s)/2)
        s1 = 0
        s2 = 0
        for i in range(half):
            if s[i] in vowels:
                s1 += 1
            if s[half+i] in vowels:
                s2 += 1
        return s1 == s2
