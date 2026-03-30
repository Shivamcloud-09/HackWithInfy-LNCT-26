class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        res = []
        st = 0
        c = 0
        for i in range(len(s)):
            if s[i] == '1':
                c += 1
            else:
                c -= 1
            if c == 0:
                a =self. makeLargestSpecial(s[st+1:i])
                res.append("1" + a + "0")
                st = i+1
        res.sort(reverse = True)
        return "".join(res)