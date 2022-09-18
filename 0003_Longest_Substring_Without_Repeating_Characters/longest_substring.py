class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        record = ""
        for i in range(len(s)):
            this_try = s[i]
            for j in range(i+1, len(s)):
                if s[j] in this_try:
                    break
                this_try += s[j]
                 
            if len(record) < len(this_try):
                record = this_try
        return len(record)