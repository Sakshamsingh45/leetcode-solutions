# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        if cur!=None:
            od=cur.next
        else:
            od=None
        while od!=None and od.next!=None:
            temp=od.next
            cur.next,temp.next,od.next=temp,cur.next,temp.next
            od=od.next
            cur=cur.next
        return head

