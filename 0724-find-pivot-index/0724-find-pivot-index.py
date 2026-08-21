class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lst = []
        c = -1
        for i in range(len(nums)):
            if i == 0:
                lsum = 0
                rsum = sum(nums[i+1:])
                if lsum == rsum:
                    return i
            elif i == (len(nums)-1):
                lsum = sum(nums[:i])
                rsum = 0
                if lsum == rsum:
                    return i
            else :
                lsum = sum(nums[:i])
                rsum = sum(nums[i+1:])
                if lsum == rsum:
                    return i
        return c