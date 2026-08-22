class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [-1] * n
        def ispal(st, i):
            return s[st:i+1] == s[st:i+1][::-1]
        def b(st):
            if st == n:
                return 0
            if dp[st] != -1:
                return dp[st]
            ans = n
            for i in range(st, n):
                if ispal(st, i):
                    ans = min(ans, 1 + b(i + 1))
            dp[st] = ans
            return ans
        return b(0) - 1