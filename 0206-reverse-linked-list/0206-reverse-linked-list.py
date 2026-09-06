# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next
        lst = arr[::-1]
        d = ListNode(-1)
        cur = d
        for v in lst:
            cur.next = ListNode(v)
            cur = cur.next
        return d.next