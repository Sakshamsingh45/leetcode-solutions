# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur=fast=head
        count=0
        mx=float("-inf")
        while fast and fast.next:
            cur=cur.next
            fast=fast.next.next
            count+=1
        fast=cur
        cur=head
        prev=None
        while fast :
            temp=fast.next
            fast.next=prev
            prev=fast
            fast=temp
        l1=head
        l2=prev
        for i in range(count):
            val=l1.val+l2.val
            mx=val if val>mx else mx
            l1=l1.next
            l2=l2.next
        return mx
