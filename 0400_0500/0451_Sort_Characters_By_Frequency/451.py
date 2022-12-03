from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:

        freq_dict = sorted(dict(Counter(s)).items(), key=lambda x: x[1])[::-1]
        ans = ""
        for i in freq_dict:
            for j in range(i[1]):
                ans += i[0]

        return ans
