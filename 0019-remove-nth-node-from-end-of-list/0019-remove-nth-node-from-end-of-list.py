# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        Head = head
        if head is None:
            return
        if Head.next is None:
            return None
        temp = Head
        c = 0
        while temp is not None:
            c += 1
            temp = temp.next
       
        p = (c+1)-n
        if p == 1:
            return Head.next
        temp = Head
        m = 1
        prev = None
        while temp is not None and m != p:
            prev = temp
            temp = temp.next
            m += 1
        prev.next = temp.next
        
        return Head
        
            

        