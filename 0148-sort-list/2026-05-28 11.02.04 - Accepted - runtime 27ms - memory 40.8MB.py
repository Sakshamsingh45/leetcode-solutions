# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nu=[]
        cur=head
        while cur is not None:
            nu.append(cur.val)
            cur=cur.next
        nu.sort()
        cur=head
        i=0
        while cur is not None:
            cur.val=nu[i]
            cur=cur.next
            i+=1
        return head