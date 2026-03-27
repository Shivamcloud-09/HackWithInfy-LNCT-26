class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        lst = [row[:] for row in mat]
        for i in mat:
            n = len(i)
            a = k % n
            if mat.index(i) % 2 == 0:
                i[:] = i[a:] + i[:a]
            else:
                i[:] = i[-a:] + i[:-a]
        if mat == lst :
            return True
        else:
            return False