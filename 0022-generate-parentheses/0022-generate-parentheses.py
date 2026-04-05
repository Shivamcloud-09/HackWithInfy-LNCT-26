class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        r = []
        def g(s,o,c):
            if len(s) == 2 * n:
                r.append(s)
                return
            if o < n :
                g(s + "(" , o + 1 , c)
            if c < o :
                g(s + ")" , o , c + 1)
        g("" , 0 , 0)
        return r