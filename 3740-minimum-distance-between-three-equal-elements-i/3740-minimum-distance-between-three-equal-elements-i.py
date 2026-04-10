class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        lst = []
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i] == nums[j] == nums[k]:
                        a = abs(i - j) + abs(j - k) + abs(k - i)
                        lst.append(a)
        return min(lst) if lst else -1
