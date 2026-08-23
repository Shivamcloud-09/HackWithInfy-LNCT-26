class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(1 , len(nums)):
            if nums[i] <= nums[i-1]:
                x = nums[i-1] + 1 - nums[i]
                ans += x
                nums[i] += x
        return ans