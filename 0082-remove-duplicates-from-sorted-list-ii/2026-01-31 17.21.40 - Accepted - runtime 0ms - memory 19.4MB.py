# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy=ListNode(None,head)
        prev=dummy
        cur=head
        while cur is not None and cur.next is not None:
            if cur.val==cur.next.val:
                value=cur.val
                while cur is not None and cur.val==value:
                    cur=cur.next
                prev.next=cur
            else:
                prev=cur
                cur=cur.next
        return dummy.next