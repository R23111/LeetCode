class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []
        buttons = {'2': ['a', 'b', 'c'],
                   '3': ['d', 'e', 'f'],
                   '4': ['g', 'h', 'i'],
                   '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'],
                   '7': ['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'],
                   '9': ['w', 'x', 'y', 'z']}
        ans = []

        def backtrack(k, curr):
            if len(curr) == len(digits):
                ans.append(curr)
                return
            for b in buttons[digits[k]]:
                backtrack(k+1, curr+b)
        backtrack(0, '')
        return ans
