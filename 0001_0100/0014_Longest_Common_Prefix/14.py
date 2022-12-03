class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longest = ""
        min_len = min([len(s) for s in strs])+1
        for i in range(min_len):
            if len(set([c[:i] for c in strs])) == 1:
                longest = strs[0][:i]
        return longest