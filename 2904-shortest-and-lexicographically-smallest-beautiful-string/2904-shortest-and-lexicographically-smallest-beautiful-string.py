class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        lst = []
        a = []
        se = list(s)
        for i in range(len(se)):
            for j in range(i , len(se)):
                lst.append(se[i:j+1])
        for l in lst:
            if l.count("1") == k:
                a.append("".join(l))
        if not a :
            return ""
        ar = min(a,key = lambda x: (len(x), x))
        return (ar)