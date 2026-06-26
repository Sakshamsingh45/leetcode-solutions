# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        leng=0
        cur=head
        while cur is not None:
            leng+=1
            cur=cur.next
        cur=fast=head
        k %= leng
        if k == 0:
            return head
        cur = fast = head
        for _ in range(k):
            fast = fast.next
        while fast.next is not None:
            cur=cur.next
            fast=fast.next
        next=cur.next
        fast.next=head
        cur.next=None
        head=next
        return head
