# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        count=0
        cur=head
        while cur is not None:
            count+=1
            cur=cur.next
        k%=count
        cur=fast=head
        if k==0:
            return head
        for i in range(k):
            fast=fast.next
        while fast.next is not None:
            cur=cur.next
            fast=fast.next
        next=cur.next
        fast.next=head
        cur.next=None
        head=next
        return head
