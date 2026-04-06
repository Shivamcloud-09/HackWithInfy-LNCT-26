class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a = set(nums)
        lst = []
        for i in range(1,len(nums)+1):
            if i not in a:
                lst.append(i)
        return lst