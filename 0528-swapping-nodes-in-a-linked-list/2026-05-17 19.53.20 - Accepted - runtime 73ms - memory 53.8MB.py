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
        cur=next=head
        for i in range(1,k):
            cur=cur.next
        for i in range(1,count-k+1):
            next=next.next
        cur.val,next.val=next.val,cur.val
        return head