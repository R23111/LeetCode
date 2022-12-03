from collections import Counter

class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        win, los = zip(*matches)
        winners = sorted(set(win) - set(los))
        loosers = sorted([l for l, c in Counter(los).items() if c == 1])
        return [winners, loosers]