# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev=None
        cur=head
        next=cur.next
        while cur is not None:
            cur.next=prev
            prev=cur
            cur=next
            if not next:
                break
            next=next.next
        return prev
        