# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while list1 is not None:
            arr.append(list1.val)
            list1 = list1.next
        while list2 is not None:
            arr.append(list2.val)
            list2 = list2.next
        arr.sort()
        d = ListNode(-1)
        cur = d
        for v in arr:
            cur.next = ListNode(v)
            cur = cur.next
        return d.next