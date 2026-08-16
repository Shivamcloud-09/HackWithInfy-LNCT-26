class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        f = {}
        for i in nums:
            f[i] = f.get(i,0) + 1
        for key , val in f.items():
            if val == 1:
                return key