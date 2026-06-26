# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        temp=prev=head
        while temp is not None:
            if temp.val==prev.val:
                temp=temp.next
            else:
                prev.next=temp
                prev=temp
                temp=temp.next
        prev.next=None
        return head