class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        for j in nums:
            i ^= j
        if i != 0:
            return n
        for k in nums:
            if k != 0 :
                return n-1
        return 0