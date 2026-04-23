class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
    
        d = defaultdict(list)
        for i, x in enumerate(nums):
            d[x].append(i)

        res = [0] * len(nums)

        for v in d.values():
            total = sum(v)
            left_sum = 0
            
            for i, x in enumerate(v):
                right_sum = total - left_sum - x
                
                left = x*i - left_sum
                right = right_sum - x*(len(v)-i-1)
                
                res[x] = left + right
                left_sum += x

        return res