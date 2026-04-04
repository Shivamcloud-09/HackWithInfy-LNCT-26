class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText
        n = len(encodedText)
        a = n // rows
        r = []
        for i in range(a):
            b = 0
            while b < rows and i < a :
                r.append(encodedText[b * a + i])
                i += 1
                b += 1
        return "".join(r).rstrip()