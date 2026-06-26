# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small=ListNode(0,None)
        large=ListNode(0,None)
        s=small
        l=large
        cur=head
        while cur is not None:
            if cur.val<x:
                s.next=cur
                s=s.next
            else:
                l.next=cur
                l=l.next
            cur=cur.next
        s.next=large.next
        l.next=None
        return small.next