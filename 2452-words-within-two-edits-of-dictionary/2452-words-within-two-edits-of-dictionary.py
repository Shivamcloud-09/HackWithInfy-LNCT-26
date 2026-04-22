class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        a = []
        for i in queries:
            for j in dictionary:
                d = 0
                for k in range(len(i)):
                    if i[k] != j[k]:
                        d += 1
                if d < 3:
                    a.append(i)
                    break
        return a