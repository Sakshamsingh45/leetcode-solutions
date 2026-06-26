# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        n=0
        while cur is not None:
            n=n*10+cur.val
            cur=cur.next
        n=n*2
        prev=None
        while n!=0:
            temp=n%10
            cur=ListNode(temp)
            cur.next=prev
            prev=cur
            n//=10
        return cur