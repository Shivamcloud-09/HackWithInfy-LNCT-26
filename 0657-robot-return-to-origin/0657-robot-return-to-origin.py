class Solution:
    def judgeCircle(self, moves: str) -> bool:
        a = moves.count("U")
        b = moves.count("D")
        c = moves.count("R")
        d = moves.count("L")
        return a==b and c==d