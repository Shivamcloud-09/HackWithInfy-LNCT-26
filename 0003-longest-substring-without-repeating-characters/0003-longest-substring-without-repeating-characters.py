class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        r = 0
        l = 0
        maxi = 0
        while r < len(s):
            if s[r] in seen:
                l = max(l ,seen[s[r]] + 1 )
            maxi = max(maxi , r-l+1)
            seen[s[r]] = r
            r += 1
        return maxi