class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        string = "123456789"
        substrings = {string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)}
        l = [int(i) for i in substrings if low <= int(i) and int(i) <= high]
        l.sort()
        return l
