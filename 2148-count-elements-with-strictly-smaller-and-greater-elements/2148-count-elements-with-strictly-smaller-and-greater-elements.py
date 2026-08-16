class Solution:
    def countElements(self, nums: List[int]) -> int:
        n = len(nums)
        c = 0
        for i in nums:
            p = 0
            d = 0
            for j in nums:
                if j > i :
                    p += 1
                elif j < i:
                    d += 1
            if p > 0 and d > 0:
                c += 1
        return c