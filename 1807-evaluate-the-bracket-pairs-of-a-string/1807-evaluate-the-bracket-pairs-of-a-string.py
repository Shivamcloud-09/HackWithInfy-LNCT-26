class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        ans = ""
        i = 0
        d = {}
        for key , val in knowledge:
            d[key] = val
        while i < len(s):
            if s[i] == "(":
                st = ""
                i += 1
                while s[i] != ")":
                    st += s[i]
                    i += 1
                ans += d.get(st , "?")
                i += 1
            else:
                ans += s[i]
                i += 1
        return ans