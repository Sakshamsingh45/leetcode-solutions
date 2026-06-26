# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur=head
        count=0
        while cur is not None:
            count+=1
            cur=cur.next
        cur=head
        for i in range(1,k):
            cur=cur.next
        next=cur
        for i in range(0,count-2*k+1):
            next=next.next
        cur.val,next.val=next.val,cur.val
        return head