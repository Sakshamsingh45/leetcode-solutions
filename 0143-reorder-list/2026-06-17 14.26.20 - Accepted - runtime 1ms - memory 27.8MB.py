# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=fast=head
        if not head or not head.next:
            return
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next
        mid=slow.next
        slow.next=None
        prev=None
        while mid!=None:
            next=mid.next
            mid.next=prev
            prev=mid
            mid=next
        cur=head
        while cur and prev:
            next1=cur.next
            next2=prev.next
            cur.next=prev
            prev.next=next1
            prev=next2
            cur=next1