# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        lst = []
        def solve(temp):
            if temp is None:
                return [0,0]
            l ,le = solve(temp.left)
            r , re = solve(temp.right)
            a = l + r + 1
            b = le + re + temp.val
            c = b // a
            if temp.val == c:
                lst.append(temp.val)
            return [a,b]
        solve(root)
        return len(lst)
