# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head.next
        cur=fast=head
        while  fast!=None and fast.next!=None :
            cur=cur.next
            fast=fast.next.next
        return cur