# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gof(a,b):
            while b:
                a,b=b,a%b
            return a
        cur=head
        while cur and cur.next:
            node=ListNode(gof(cur.val,cur.next.val),cur.next)
            cur.next=node
            cur=node.next
        return head