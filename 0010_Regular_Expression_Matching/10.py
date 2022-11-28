class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        match = len(text) > 0 and pattern[0] in [text[0], '.']

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or match and self.isMatch(text[1:], pattern))
        else:
            return match and self.isMatch(text[1:], pattern[1:])