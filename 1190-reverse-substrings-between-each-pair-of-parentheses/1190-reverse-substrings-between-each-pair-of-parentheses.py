class Solution:
    def reverseParentheses(self, s: str) -> str:
        lst = []
        for i in s:
            if i == ")":
                st = ""
                while lst[-1] != "(":
                    st += lst.pop()
                lst.pop()
                for j in st:
                    lst.append(j)
            elif i != "(":
                lst.append(i)
            else:
                lst.append(i)
        return "".join(lst)

