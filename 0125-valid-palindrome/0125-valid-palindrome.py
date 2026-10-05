class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""
        for c in s:
            if c.isalnum():
                a += c.lower()
        if a[:] == a[::-1]:
            return True
        else:
            return False