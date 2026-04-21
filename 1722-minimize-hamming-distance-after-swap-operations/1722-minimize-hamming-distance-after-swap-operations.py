class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        for i, j in allowedSwaps:
            parent[find(i)] = find(j)
        groups = {}
        for i in range(n):
            p = find(i)
            groups.setdefault(p, []).append(i)
        ans = 0
        for g in groups.values():
            freq = {}
            for i in g:
                freq[source[i]] = freq.get(source[i], 0) + 1
            for i in g:
                if freq.get(target[i], 0):
                    freq[target[i]] -= 1
                else:
                    ans += 1
        return ans