class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        lst = []
        for i in range(len(A)):
            c = 0
            for x in A[:i+1]:
                if x in B[:i+1]:
                    c += 1
            lst.append(c)
        return lst
