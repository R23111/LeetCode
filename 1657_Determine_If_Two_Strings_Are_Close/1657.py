class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        for w in word1:
            if not w in word2:
                return False

        c1 = list(Counter(word1).values())
        c2 = list(Counter(word2).values())

        c1.sort()
        c2.sort()

        if c1 != c2:
            return False

        return True
