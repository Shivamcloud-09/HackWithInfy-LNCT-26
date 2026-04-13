class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        lst = []
        for i in range(n):
            if nums[i] == target :
                c = abs(i - start)
                lst.append(c)
        return min(lst)