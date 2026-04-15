class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        ans = float('inf')
        for i in range(n):
            if words[i] == target :
                d = abs(i - startIndex)
                ans = min(ans , d , n - d )
        return ans if ans != float('inf') else -1