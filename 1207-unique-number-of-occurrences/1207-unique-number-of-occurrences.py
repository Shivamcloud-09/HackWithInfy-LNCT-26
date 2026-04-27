class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        f = {}
        lst = []
        n = len(arr)
        for i in arr:
            f[i] = f.get(i,0)+1
        for key , val in f.items():
            lst.append(val)
        return (len(lst)) == len(set(lst))