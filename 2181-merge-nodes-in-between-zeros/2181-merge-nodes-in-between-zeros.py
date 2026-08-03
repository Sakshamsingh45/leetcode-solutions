# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head.next
        s=0
        dummy=ListNode(None)
        prev=dummy
        while cur is not None:
            if cur.val!=0:
                s+=cur.val
            else:
                prev.next=ListNode(s)
                prev=prev.next
                s=0
            cur=cur.next
        return dummy.next