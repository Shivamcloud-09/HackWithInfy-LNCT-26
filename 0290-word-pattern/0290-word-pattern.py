class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        lst ={}
        mst ={} 
        for c , w in zip(pattern , words):
            if c in lst and lst[c] != w:
                return False
            if w in mst and mst[w] != c:
                return False
            lst[c] = w
            mst[w] = c
        return True