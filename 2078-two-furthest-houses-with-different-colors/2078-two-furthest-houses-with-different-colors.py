class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        c = 0
        a = 0
        m = 0
        n = len(colors)
        for i in range(1,n):
            if colors[c] != colors[i]:
                m = max(m, abs(c - i))
        c = n - 1
        for i in range(n):
            if colors[c] != colors[i]:
                m = max(m, abs(c - i))
        return m
