# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(None,head)
        count=0
        prev=dummy
        cur=fast=head
        while fast and fast.next:
            prev=prev.next
            cur=cur.next
            fast=fast.next.next
            count+=1
        prev.next=cur.next
        cur.next=None
        return dummy.next