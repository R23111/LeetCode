from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:

        freq_dict = sorted(dict(Counter(s)).items(), key=lambda x: x[1])[::-1]
        ans = ""
        for i in freq_dict:
            for j in range(i[1]):
                ans += i[0]

        return ans


# Problem of the day Feb 7th, 2024

class Solution:
    def frequencySort(self, s: str) -> str:
        occ = []
        for c in set(s):
            occ.append((c, s.count(c)))
        occ = sorted(occ, key=lambda x: x[1], reverse=True)
        return "".join(c[0]*c[1] for c in occ)

        