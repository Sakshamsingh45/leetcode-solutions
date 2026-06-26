# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp=l1
        c1=c2=0
        while temp!=None:
            c1=c1*10+temp.val
            temp=temp.next
        temp=l2
        while temp!=None:
            c2=c2*10+temp.val
            temp=temp.next
        ans=c1+c2
        head=cur=ListNode(0)
        for i in str(ans):
            cur.next=ListNode(int(i))
            cur=cur.next

        return head.next

        