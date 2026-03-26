class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        a = 1
        c = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1] +1:
                c += 1
            else:
                a = max(a,c)
                c = 1
        return max(a,c)