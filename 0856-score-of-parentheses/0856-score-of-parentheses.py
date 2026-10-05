class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        a = 0
        b = 0
        for i in range(len(s)):
            if s[i] == "(":
                b += 1
            else:
                b -= 1
                if s[i-1] == "(":
                    a += 2 ** b
        return a