class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        r = []
        n = len(nums)
        for i in range(n):
            c = -1
            f = False
            for j in range(i+1 , n):
                if nums[j] > nums[i]:
                    c = nums[j]
                    f = True
                    break
            if not f:
                for j in range(0 , i):
                    if nums[j] > nums[i]:
                        c = nums[j]
                        break
            r.append(c)
        return r

            
