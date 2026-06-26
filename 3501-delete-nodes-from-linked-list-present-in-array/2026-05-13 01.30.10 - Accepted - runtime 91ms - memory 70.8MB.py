# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums=set(nums)
        h=prev=ListNode(0)
        prev.next=head
        h.next=head
        cur=head
        while cur!=None:
            if cur.val in nums:
                prev.next=cur.next
                cur=prev
            prev=cur
            cur=cur.next
        return h.next     