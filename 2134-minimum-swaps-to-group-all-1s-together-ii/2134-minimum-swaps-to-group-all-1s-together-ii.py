class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k = sum(nums)
        if k == 0:
            return 0
        nums = nums + nums
        z = nums[:k].count(0)
        a = z
        for i in range(k,len(nums)):
            if nums[i] == 0:
                z += 1
            if nums[i-k] == 0:
                z -= 1
            a = min(a,z)
        return a